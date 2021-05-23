OpenRCT2 JSON Objects
========================================

Basic fields
------------

All OpenRCT2 JSON objects have a "header" analogous to the DAT header. It contains the following fields (* indicates a required field):

.. jsonschema:: json/OpenRCT2JSONObjectHead.json
    :lift_title: off



Example


.. literalinclude:: examples/rct2.scenery_small.tck.json
    :language: json
    :force: 

Object Types
------------

This is a list of object types. See the respective pages for more information

.. toctree::
    :maxdepth: 1
    :titlesonly:

    parkentrance
    footpath
    footpathrailings
    footpathsurface
    music
    ride