# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'OpenRCT2 doc'
copyright = '2021, OpenRCT2'
author = 'OpenRCT2'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx-jsonschema'
]

jsonschema_options = {
    # 'lift_description': True,
    'lift_definitions': True,
    #'lift_title': False
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'titles_only': False
}

html_style = "css/custom.css"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

import importlib
import json
## PATCH `sphinx-jsonschema`
#  to render `example` fields correctly schema properties
#
def _patched_sphinx_jsonschema_examples(self, examples):
    
    text = '.. code-block:: json\n\n\t'
    rows = []
    # rows.extend(self._render_any_value(text + json.JSONEncoder(examples)))
    e = json.JSONEncoder(indent=2)
    if isinstance(examples, list):
        for v in examples:
            rows.extend(self._render_any_value(text + e.encode(v).replace('\n','\n\t') + '\n'))
    rows = self._prepend(self._cell('examples'), rows)
    return rows

sjs_wide_format = importlib.import_module("sphinx-jsonschema.wide_format")
sjs_wide_format.WideFormat._examples = _patched_sphinx_jsonschema_examples

def _objectproperties(self, schema, key):
        # process the `properties` key of the object type
        # used for `properties`, `patternProperties` and
        # `definitions`.
        rows = []

        if key in schema:
            if key != 'properties':
                rows.append(self._line(self._cell(key)))

            for prop in schema[key].keys():
                # insert spaces around the regexp OR operator
                # allowing the regexp to be split over multiple lines.
                proplist = prop.split('|')
                dispprop = self._escape(' | '.join(proplist))
                bold = '**'
                if 'required' in schema:
                    if prop in schema['required']:
                        dispprop += '*'
                label = self._cell('- ' + bold + dispprop + bold)

                if isinstance(schema[key][prop], dict):
                    obj = schema[key][prop]
                    rows.extend(self._dispatch(obj, label)[0])
                else:
                    rows.append(self._line(label, self._cell(schema[key][prop])))
            del schema[key]
        return rows

sjs_wide_format.WideFormat._objectproperties = _objectproperties

def _objecttype(self, schema):
        # create description and type rows
        rows = self._simpletype(schema)
        rows2 = []
        
        rows2.extend(self._objectproperties(schema, 'properties'))
        rows2.extend(self._objectproperties(schema, 'patternProperties'))
        rows2.extend(self._bool_or_object(schema, 'additionalProperties'))
        rows2.extend(self._dependencies(schema, 'dependencies'))
        rows2.extend(self._kvpairs(schema, self.KV_OBJECT))
        if rows != [] and rows2 != []:
            rows.append(self._line(self._cell('')))
        rows.extend(rows2)
        return rows

sjs_wide_format.WideFormat._objecttype = _objecttype

def _complexstructures(self, schema):
        rows = []

        for k in self.COMBINATORS:
            # combinators belong at this level as alternative to type
            if k in schema:
                items = []
                for s in schema[k]:
                    content = self._dispatch(s)[0]
                    if content:
                        if items:
                            items.append(self._line(self._cell('')))
                            items.append(self._line(self._cell('')))
                            items.append(self._line(self._cell('')))
                        items.extend(content)
                if items:
                    rows.extend(self._prepend(self._cell(k), items))
                del schema[k]

        for k in self.SINGLEOBJECTS:
            # combinators belong at this level as alternative to type
            if k in schema:
                rows.extend(self._dispatch(schema[k], self._cell(k))[0])
                del schema[k]

        if self.CONDITIONAL[0] in schema:
            # only if 'if' in schema there would be a needs to go through if, then & else
            items = []
            for k in self.CONDITIONAL:
                if k in schema:
                    content = self._dispatch(schema[k])[0]
                    if content:
                        items.append(self._prepend(self._cell(k), content))
                    del schema[k]
            if len(items) >= 2:
                for item in items:
                    rows.extend(item)

        return rows

sjs_wide_format.WideFormat._complexstructures = _complexstructures

def _simpletype(self, schema):
        rows = []

        if (not self.options['lift_title'] or self.nesting > 1):
            if 'title' in schema:
                rows.append(self._line(self._cell('*' + schema['title'] + '*')))
                del schema['title']

        self._check_description(schema, rows)

        if 'type' in schema:
            t = schema['type']
            if type(t) == list:
                t = '*' + '*/*'.join(t) + '*'
            else:
                t = '*' + t + '*'
            rows.append(
                self._line(self._cell('type: ' + t)))
            del schema['type']

        if 'enum' in schema:
            rows.append(
                self._line(
                    self._cell('enum'),
                    self._cell(', '.join(
                        [sjs_wide_format.str_unicode(e) for e in schema['enum']]))))
            del schema['enum']

        if 'examples' in schema:
            rows.extend(self._examples(schema['examples']))
            del schema['examples']

        rows.extend(self._kvpairs(schema, self.KV_SIMPLE))
        return rows

sjs_wide_format.WideFormat._simpletype = _simpletype