.. _music:

Music
========================================

Properties
----------

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/originalStyleId
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/rideTypes
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/tracks

Examples
--------

.. code-block:: json
    :caption: rct2.music.organ

    "properties": {
        "originalStyleId": 27,
        "tracks": [
            {
                "source": "$RCT2:DATA/css41.dat",
                "name": "Toccata",
                "composer": "Charles-Marie Widor"
            }
        ]
    }

.. code-block:: json
    :caption: rct2.music.fairground
    :force: 

    "properties": {
        "rideTypes": ["merry_go_round"],
        "tracks": [
            {
                "source": "$RCT2:DATA/css4.dat",
                "name": "Die Regimentskinder (Children of the regiment)",
                "composer": "Julius Fučík"
            },
            [...]
            {
                "source": "$RCT2:DATA/css15.dat",
                "name": "Waltz Medley",
                "composer": "Johann Strauss jr."
            }
        ]
    }