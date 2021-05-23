.. _ride:

Ride
========================================

Since stalls are considered rides as well, this page is split up into three parts. First are properties for :ref:`allrides`. After that are the properties specific to shops/stalls vs those for actual rides.

If `type` is `food_stall`, `drink_stall`, `shop`, `information_kiosk`, `toilets`, `cash_machine`, `first_aid` (i.e., a shop or stall), use properties for :ref:`shop`. Otherwise, use properties for :ref:`actualride`.


.. _allrides:

All Ride Objects
-------------------------------

Properties
~~~~~~~~~~

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/type
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/category
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/carColours


.. _shop:

Stalls/Shops Only
-------------------------

Properties
~~~~~~~~~~

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/sells
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/disablePainting

Example
~~~~~~~

.. code-block:: json
    :caption: rct2.ride.bnoodles

    "properties": {
        "type": "food_stall",
        "category": "stall",
        "sells": "beef_noodles",
        "disablePainting": true,
        "carColours": [
            [
                ["black", "black", "black"]
            ]
        ]
    }

.. _actualride:

Rides Only
------------------------

Properties
~~~~~~~~~~

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/buildMenuPriority
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/maxHeight
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/swingMode
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/rotationMode
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/ratingMultipler
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/minCarsPerTrain
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/maxCarsPerTrain
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/carsPerFlatRide
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/numEmptyCars
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/defaultCar
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/tabCar
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/tabScale
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/headCars
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/tailCars
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/cars

Flags
~~~~~

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/noInversions
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/noBanking
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/playDepartSound
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/playSplashSound
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/playSplashSoundSlide
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/hasShelter
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/limitAirTimeBonus
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/disableBreakdown
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/noCollisionCrashes
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/disablePainting



Cars
~~~~

.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/carItem
.. jsonschema:: json/OpenRCT2JSONObjectDefinitions.json#/definitions/carColours