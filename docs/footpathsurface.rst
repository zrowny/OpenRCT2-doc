.. _footpathsurface:

Footpath Surface
========================================

Note that many of these objects have none of these properties set, so their JSON files don't have to even include the `properties` object.

Properties
----------

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/isQueue
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/noSlopeRailings
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/editorOnly

Example
-------

.. code-block:: json

    "properties": {
        "isQueue": true,
        "noSlopeRailings": true
    }