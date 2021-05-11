# OpenRCT2 JSON Object Format
{: .no_toc }

<details open>
  <summary markdown='span'>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

# [Required] id
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] id</strong>

</summary>
<blockquote>

**Type:** `string`

**Description:** OpenRCT2 id of the object. This should be formatted as "objectsource.objectname" or similar. This value MUST be unique for all objects.

</blockquote>
</details>

# [Required] authors
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] authors</strong>

</summary>
<blockquote>

**Type:** `array of string`

**Description:** Array containing the authors of the object

| Each item of this array must be | Description                        |
| ------------------------------- | ---------------------------------- |
| [items](#authors_items)         | The name of (one of) the author(s) |
|                                 |                                    |

## items

**Type:** `string`

**Description:** The name of (one of) the author(s)

**Examples:** 

```json
[
    "spacek531"
]
```
```json
[
    "Chris Sawyer",
    "Simon Foster"
]
```

</blockquote>
</details>

# version
{: .d-none }

<details>
<summary markdown='span'><strong>version</strong>

</summary>
<blockquote>

**Type:** `string`

**Description:** Version of the object

**Example:** 

```json
"1.0"
```

</blockquote>
</details>

# ~~originalId~~
{: .d-none }

<details>
<summary markdown='span'><strong>~~originalId~~</strong>

</summary>
<blockquote>

| **Type**       | `string`                                              |
| -------------- | ----------------------------------------------------- |
| **Deprecated** | ![badge](https://img.shields.io/badge/Deprecated-red) |
|                |                                                       |

**Description:** [Deprecated for new objects]. Represents the original DAT header. The three sections are the flags, name, and checksum. This shouldn't be used for new (not converted) objects

**Examples:** 

```json
"00000000|RMCT2   |00003000"
```
```json
"0A188A80|4X4     |0DB8676C"
```

</blockquote>
</details>

# sourceGame
{: .d-none }

<details>
<summary markdown='span'><strong>sourceGame</strong>

</summary>
<blockquote>

**Description:** The source(s) of the object. Either a single string or an array containing each source

<blockquote>

| Any of                                          |
| ----------------------------------------------- |
| [Source String](#sourceGame_anyOf_i0)           |
| [Array of Source Strings](#sourceGame_anyOf_i1) |
|                                                 |

## Source String
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
Source String    </strong>
</summary>

<blockquote>

**Type:** `enum (of string)`

Must be one of:
* "rct1"
* "rct1aa"
* "rct1ll"
* "rct2"
* "rct2ww"
* "rct2tt"
* "official"
* "custom"

</blockquote>

</details>

## Array of Source Strings
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
Array of Source Strings    </strong>
</summary>

<blockquote>

**Type:** `array`

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [sourceString](#sourceGame_anyOf_i1_items) | -           |
|                                            |             |

### sourceString

**Type:** `enum (of string)`

Must be one of:
* "rct1"
* "rct1aa"
* "rct1ll"
* "rct2"
* "rct2ww"
* "rct2tt"
* "official"
* "custom"

</blockquote>

</details>

</blockquote>

</blockquote>
</details>

# [Required] objectType
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] objectType</strong>

</summary>
<blockquote>

**Type:** `enum (of string)`

**Description:** The type of the object

Must be one of:
* "ride"
* "footpath"
* "footpath_banner"
* "footpath_item"
* "scenery_small"
* "scenery_large"
* "scenery_wall"
* "scenery_group"
* "park_entrance"
* "water"
* "terrain_surface"
* "terrain_edge"
* "station"
* "music"
* "footpath_surface"
* "footpath_railings"

</blockquote>
</details>

# images
{: .d-none }

<details>
<summary markdown='span'><strong>images</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** The location of images for the object

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#images_items)          | -           |
|                                 |             |

## items

<blockquote>

| Any of                           |
| -------------------------------- |
| [item 0](#images_items_anyOf_i0) |
| [item 1](#images_items_anyOf_i1) |
|                                  |

### item 0
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
item 0    </strong>
</summary>

<blockquote>

**Description:** An explanation about the purpose of this instance.

#### path
{: .d-none }

<details>
<summary markdown='span'><strong>path</strong>

</summary>
<blockquote>

**Type:** `string`

**Description:** An explanation about the purpose of this instance.

</blockquote>
</details>

#### x
{: .d-none }

<details>
<summary markdown='span'><strong>x</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** An explanation about the purpose of this instance.

</blockquote>
</details>

#### y
{: .d-none }

<details>
<summary markdown='span'><strong>y</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** An explanation about the purpose of this instance.

</blockquote>
</details>

</blockquote>

</details>

### item 1
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
item 1    </strong>
</summary>

<blockquote>

**Type:** `string`

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
""
```

</blockquote>

</details>

</blockquote>

**Example:** 

```json
[
    {
        "path": "images/preview.png",
        "x": 0,
        "y": 0
    },
    ""
]
```

</blockquote>
</details>

# strings
{: .d-none }

<details>
<summary markdown='span'><strong>strings</strong>

</summary>
<blockquote>

**Description:** Contains the various strings used for the object

## name
{: .d-none }

<details>
<summary markdown='span'><strong>name</strong>

</summary>
<blockquote>

**Description:** Contains the name of the object in all the different supported languages

### en-GB
{: .d-none }

<details>
<summary markdown='span'><strong>en-GB</strong>

</summary>
<blockquote>

**Type:** `string`

</blockquote>
</details>

**Example:** 

```json
{
    "en-GB": "Single Rail Roller Coaster Trains"
}
```

</blockquote>
</details>

## description
{: .d-none }

<details>
<summary markdown='span'><strong>description</strong>

</summary>
<blockquote>

**Description:** Contains a short description of the object in all the different supported languages

### en-GB
{: .d-none }

<details>
<summary markdown='span'><strong>en-GB</strong>

</summary>
<blockquote>

**Type:** `string`

</blockquote>
</details>

**Example:** 

```json
{
    "en-GB": "Riders ride single file on a narrow monorail track as they race through tight inversions and direction changes"
}
```

</blockquote>
</details>

## capacity
{: .d-none }

<details>
<summary markdown='span'><strong>capacity</strong>

</summary>
<blockquote>

**Description:** For rides, this contains text describing the capacity in all the different supported languages

### en-GB
{: .d-none }

<details>
<summary markdown='span'><strong>en-GB</strong>

</summary>
<blockquote>

**Type:** `string`

</blockquote>
</details>

**Example:** 

```json
{
    "en-GB": "1 passenger per car"
}
```

</blockquote>
</details>

**Example:** 

```json
{
    "name": {
        "en-GB": "Single Rail Roller Coaster Trains"
    },
    "description": {
        "en-GB": "Riders ride single file on a narrow monorail track as they race through tight inversions and direction changes"
    },
    "capacity": {
        "en-GB": "1 passenger per car"
    }
}
```

</blockquote>
</details>

# properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

**Description:** This object contains all the properties of the object

</blockquote>
</details>

<blockquote>

# If Park Entrance
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Park Entrance    </strong>
</summary>

```If (objectType = "park_entrance")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### [Required] scrollingMode
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] scrollingMode</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Scrolling mode of the sign

</blockquote>
</details>

#### [Required] textHeight
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] textHeight</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Height of the sign text

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</details>

# If Footpath
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Footpath    </strong>
</summary>

```If (objectType = "footpath")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### [Required] supportType
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] supportType</strong>

</summary>
<blockquote>

| **Type**    | `enum (of string or integer)` |
| ----------- | ----------------------------- |
| **Default** | `"box"`                       |
|             |                               |

**Description:** Type of supports used for path (0=Box,1=Pole)

Must be one of:
* "pole"
* "box"
* 1
* 0

</blockquote>
</details>

#### [Required] scrollingMode
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] scrollingMode</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Scrolling mode of the sign

</blockquote>
</details>

#### noSlopeRailings
{: .d-none }

<details>
<summary markdown='span'><strong>noSlopeRailings</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if path has no railings on slopes

</blockquote>
</details>

#### hasSupportImages
{: .d-none }

<details>
<summary markdown='span'><strong>hasSupportImages</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if object has images for path supports

</blockquote>
</details>

#### hasElevatedPathImages
{: .d-none }

<details>
<summary markdown='span'><strong>hasElevatedPathImages</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if object has images for elevated path

</blockquote>
</details>

#### editorOnly
{: .d-none }

<details>
<summary markdown='span'><strong>editorOnly</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if path is normally only available in the scenario editor

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</details>

# If Footpath Railings
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Footpath Railings    </strong>
</summary>

```If (objectType = "footpath_railings")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### [Required] supportType
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] supportType</strong>

</summary>
<blockquote>

| **Type**    | `enum (of string or integer)` |
| ----------- | ----------------------------- |
| **Default** | `"box"`                       |
|             |                               |

**Description:** Type of supports used for path (0=Box,1=Pole)

Must be one of:
* "pole"
* "box"
* 1
* 0

</blockquote>
</details>

#### [Required] scrollingMode
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] scrollingMode</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Scrolling mode of the sign

</blockquote>
</details>

#### colour
{: .d-none }

<details>
<summary markdown='span'><strong>colour</strong>

</summary>
<blockquote>

**Type:** `enum (of string)`

**Description:** Object color

Must be one of:
* "black"
* "grey"
* "white"
* "dark_purple"
* "light_purple"
* "bright_purple"
* "dark_blue"
* "light_blue"
* "icy_blue"
* "teal"
* "aquamarine"
* "saturated_green"
* "dark_green"
* "moss_green"
* "bright_green"
* "olive_green"
* "dark_olive_green"
* "bright_yellow"
* "yellow"
* "dark_yellow"
* "light_orange"
* "dark_orange"
* "light_brown"
* "saturated_brown"
* "dark_brown"
* "salmon_pink"
* "bordeaux_red"
* "saturated_red"
* "bright_red"
* "dark_pink"
* "bright_pink"
* "light_pink"

</blockquote>
</details>

#### hasSupportImages
{: .d-none }

<details>
<summary markdown='span'><strong>hasSupportImages</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if object has images for path supports

</blockquote>
</details>

#### hasElevatedPathImages
{: .d-none }

<details>
<summary markdown='span'><strong>hasElevatedPathImages</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if object has images for elevated path

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</details>

# If Footpath Surface
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Footpath Surface    </strong>
</summary>

```If (objectType = "footpath_surface")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### isQueue
{: .d-none }

<details>
<summary markdown='span'><strong>isQueue</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if path surface is for a queue

</blockquote>
</details>

#### noSlopeRailings
{: .d-none }

<details>
<summary markdown='span'><strong>noSlopeRailings</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if path has no railings on slopes

</blockquote>
</details>

#### editorOnly
{: .d-none }

<details>
<summary markdown='span'><strong>editorOnly</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** True if path is normally only available in the scenario editor

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</details>

# If Music
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Music    </strong>
</summary>

```If (objectType = "music")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### originalStyleId
{: .d-none }

<details>
<summary markdown='span'><strong>originalStyleId</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Original Music Style ID (used for most music except for merry_go_round). Original list:  
```
MUSIC_STYLE_DODGEMS_BEAT,  
MUSIC_STYLE_FAIRGROUND_ORGAN,  
MUSIC_STYLE_ROMAN_FANFARE,  
MUSIC_STYLE_ORIENTAL,  
MUSIC_STYLE_MARTIAN,  
MUSIC_STYLE_JUNGLE_DRUMS,  
MUSIC_STYLE_EGYPTIAN,  
MUSIC_STYLE_TOYLAND,  
MUSIC_STYLE_CIRCUS_SHOW,  
MUSIC_STYLE_SPACE,  
MUSIC_STYLE_HORROR,  
MUSIC_STYLE_TECHNO,  
MUSIC_STYLE_GENTLE,  
MUSIC_STYLE_SUMMER,  
MUSIC_STYLE_WATER,  
MUSIC_STYLE_WILD_WEST,  
MUSIC_STYLE_JURASSIC,  
MUSIC_STYLE_ROCK,  
MUSIC_STYLE_RAGTIME,  
MUSIC_STYLE_FANTASY,  
MUSIC_STYLE_ROCK_STYLE_2,  
MUSIC_STYLE_ICE,  
MUSIC_STYLE_SNOW,  
MUSIC_STYLE_CUSTOM_MUSIC_1,  
MUSIC_STYLE_CUSTOM_MUSIC_2,  
MUSIC_STYLE_MEDIEVAL,  
MUSIC_STYLE_URBAN,  
MUSIC_STYLE_ORGAN,  
MUSIC_STYLE_MECHANICAL,  
MUSIC_STYLE_MODERN,  
MUSIC_STYLE_PIRATES,  
MUSIC_STYLE_ROCK_STYLE_3,  
MUSIC_STYLE_CANDY_STYLE  
```

</blockquote>
</details>

#### rideTypes
{: .d-none }

<details>
<summary markdown='span'><strong>rideTypes</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** Array of ride types this music can be used for. If this is not included, then music is available for all rides except merry-go-round

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [item 0](#allOf_i4_then_properties_rideTypes_items_i0) | -           |
|                                                        |             |

##### item 0

**Type:** `enum (of string)`

Must be one of:
* "spiral_rc"
* "stand_up_rc"
* "suspended_swinging_rc"
* "inverted_rc"
* "junior_rc"
* "miniature_railway"
* "monorail"
* "mini_suspended_rc"
* "boat_hire"
* "wooden_wild_mouse"
* "steeplechase"
* "car_ride"
* "launched_freefall"
* "bobsleigh_rc"
* "observation_tower"
* "looping_rc"
* "dinghy_slide"
* "mine_train_rc"
* "chairlift"
* "corkscrew_rc"
* "maze"
* "spiral_slide"
* "go_karts"
* "log_flume"
* "river_rapids"
* "dodgems"
* "swinging_ship"
* "swinging_inverter_ship"
* "food_stall"
* "drink_stall"
* "shop"
* "merry_go_round"
* "information_kiosk"
* "toilets"
* "ferris_wheel"
* "motion_simulator"
* "3d_cinema"
* "top_spin"
* "space_rings"
* "reverse_freefall_rc"
* "lift"
* "vertical_drop_rc"
* "cash_machine"
* "twist"
* "haunted_house"
* "first_aid"
* "circus"
* "ghost_train"
* "twister_rc"
* "wooden_rc"
* "side_friction_rc"
* "steel_wild_mouse"
* "multi_dimension_rc"
* "flying_rc"
* "virginia_reel"
* "splash_boats"
* "mini_helicopters"
* "lay_down_rc"
* "suspended_monorail"
* "reverser_rc"
* "heartline_twister_rc"
* "mini_golf"
* "giga_rc"
* "roto_drop"
* "flying_saucers"
* "crooked_house"
* "monorail_cycles"
* "compact_inverted_rc"
* "water_coaster"
* "air_powered_vertical_rc"
* "inverted_hairpin_rc"
* "magic_carpet"
* "submarine_ride"
* "river_rafts"
* "enterprise"
* "inverted_impulse_rc"
* "mini_rc"
* "mine_ride"
* "lim_launched_rc"
* "hypercoaster"
* "hyper_twister"
* "monster_trucks"
* "spinning_wild_mouse"
* "classic_mini_rc"
* "hybrid_rc"
* "single_rail_rc"

</blockquote>
</details>

#### [Required] tracks
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] tracks</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** Array of the tracks included in this music object (usually just one, but merry_go_round, for example, has multiple)

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</details>

# If Ride
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Ride    </strong>
</summary>

```If (objectType = "ride")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

#### [Required] type
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] type</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** Array of ride types of this object. Currently only up to 3 are used

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 0](#allOf_i5_then_properties_type_items_i0) | -           |
|                                                   |             |

##### item 0

**Type:** `enum (of string)`

Must be one of:
* "spiral_rc"
* "stand_up_rc"
* "suspended_swinging_rc"
* "inverted_rc"
* "junior_rc"
* "miniature_railway"
* "monorail"
* "mini_suspended_rc"
* "boat_hire"
* "wooden_wild_mouse"
* "steeplechase"
* "car_ride"
* "launched_freefall"
* "bobsleigh_rc"
* "observation_tower"
* "looping_rc"
* "dinghy_slide"
* "mine_train_rc"
* "chairlift"
* "corkscrew_rc"
* "maze"
* "spiral_slide"
* "go_karts"
* "log_flume"
* "river_rapids"
* "dodgems"
* "swinging_ship"
* "swinging_inverter_ship"
* "food_stall"
* "drink_stall"
* "shop"
* "merry_go_round"
* "information_kiosk"
* "toilets"
* "ferris_wheel"
* "motion_simulator"
* "3d_cinema"
* "top_spin"
* "space_rings"
* "reverse_freefall_rc"
* "lift"
* "vertical_drop_rc"
* "cash_machine"
* "twist"
* "haunted_house"
* "first_aid"
* "circus"
* "ghost_train"
* "twister_rc"
* "wooden_rc"
* "side_friction_rc"
* "steel_wild_mouse"
* "multi_dimension_rc"
* "flying_rc"
* "virginia_reel"
* "splash_boats"
* "mini_helicopters"
* "lay_down_rc"
* "suspended_monorail"
* "reverser_rc"
* "heartline_twister_rc"
* "mini_golf"
* "giga_rc"
* "roto_drop"
* "flying_saucers"
* "crooked_house"
* "monorail_cycles"
* "compact_inverted_rc"
* "water_coaster"
* "air_powered_vertical_rc"
* "inverted_hairpin_rc"
* "magic_carpet"
* "submarine_ride"
* "river_rafts"
* "enterprise"
* "inverted_impulse_rc"
* "mini_rc"
* "mine_ride"
* "lim_launched_rc"
* "hypercoaster"
* "hyper_twister"
* "monster_trucks"
* "spinning_wild_mouse"
* "classic_mini_rc"
* "hybrid_rc"
* "single_rail_rc"

</blockquote>
</details>

#### category
{: .d-none }

<details>
<summary markdown='span'><strong>category</strong>

</summary>
<blockquote>

**Type:** `string`

**Description:** [Deprecated] Ride category is now determined from the type

**Example:** 

```json
"rollercoaster"
```

</blockquote>
</details>

#### maxHeight
{: .d-none }

<details>
<summary markdown='span'><strong>maxHeight</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Maximum height of the ride (if not set, or set to 0, uses the hardcoded value for the ridetype)

</blockquote>
</details>

#### [Required] carColours
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] carColours</strong>

</summary>
<blockquote>

**Type:** `array of array`

**Description:** An array of preset color schemes for the ride. Currently, a ride can either have multiple presets (up to 254) with a single color scheme each (which are randomly chosen from when a ride is built), or it can have a single preset that has different color schemes for each train (car?).   
Note: If there is more than one preset, only the first color scheme in each preset is used.

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_properties_carColours_items) | -           |
|                                                     |             |

##### items

**Type:** `array of array`

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_properties_carColours_items_items) | -           |
|                                                           |             |

##### items

**Type:** `array`

| Each item of this array must be                                     | Description  |
| ------------------------------------------------------------------- | ------------ |
| [colour](#allOf_i5_then_properties_carColours_items_items_items_i0) | Object color |
| [colour](#allOf_i5_then_properties_carColours_items_items_items_i1) | Object color |
| [colour](#allOf_i5_then_properties_carColours_items_items_items_i2) | Object color |
|                                                                     |              |

##### colour

**Type:** `enum (of string)`

**Description:** Object color

Must be one of:
* "black"
* "grey"
* "white"
* "dark_purple"
* "light_purple"
* "bright_purple"
* "dark_blue"
* "light_blue"
* "icy_blue"
* "teal"
* "aquamarine"
* "saturated_green"
* "dark_green"
* "moss_green"
* "bright_green"
* "olive_green"
* "dark_olive_green"
* "bright_yellow"
* "yellow"
* "dark_yellow"
* "light_orange"
* "dark_orange"
* "light_brown"
* "saturated_brown"
* "dark_brown"
* "salmon_pink"
* "bordeaux_red"
* "saturated_red"
* "bright_red"
* "dark_pink"
* "bright_pink"
* "light_pink"

##### colour

**Type:** `enum (of string)`

**Description:** Object color

Must be one of:
* "black"
* "grey"
* "white"
* "dark_purple"
* "light_purple"
* "bright_purple"
* "dark_blue"
* "light_blue"
* "icy_blue"
* "teal"
* "aquamarine"
* "saturated_green"
* "dark_green"
* "moss_green"
* "bright_green"
* "olive_green"
* "dark_olive_green"
* "bright_yellow"
* "yellow"
* "dark_yellow"
* "light_orange"
* "dark_orange"
* "light_brown"
* "saturated_brown"
* "dark_brown"
* "salmon_pink"
* "bordeaux_red"
* "saturated_red"
* "bright_red"
* "dark_pink"
* "bright_pink"
* "light_pink"

##### colour

**Type:** `enum (of string)`

**Description:** Object color

Must be one of:
* "black"
* "grey"
* "white"
* "dark_purple"
* "light_purple"
* "bright_purple"
* "dark_blue"
* "light_blue"
* "icy_blue"
* "teal"
* "aquamarine"
* "saturated_green"
* "dark_green"
* "moss_green"
* "bright_green"
* "olive_green"
* "dark_olive_green"
* "bright_yellow"
* "yellow"
* "dark_yellow"
* "light_orange"
* "dark_orange"
* "light_brown"
* "saturated_brown"
* "dark_brown"
* "salmon_pink"
* "bordeaux_red"
* "saturated_red"
* "bright_red"
* "dark_pink"
* "bright_pink"
* "light_pink"

**Example:** 

```json
[
    [
        [
            "bright_red",
            "white",
            "light_brown"
        ]
    ],
    [
        [
            "dark_green",
            "bright_green",
            "white"
        ]
    ]
]
```

</blockquote>
</details>

#### buildMenuPriority
{: .d-none }

<details>
<summary markdown='span'><strong>buildMenuPriority</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For rides that do no list their subtypes separately, this number describes the priority order for which subtype should show for the generic ride type in the build menu. Of all the subtypes that are available and researched, whichever has the highest buildMenuPriority will show as representative of the generic ride type.

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 255 |
|              |          |

</blockquote>
</details>

#### noInversions
{: .d-none }

<details>
<summary markdown='span'><strong>noInversions</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride does not support inversions

</blockquote>
</details>

#### noBanking
{: .d-none }

<details>
<summary markdown='span'><strong>noBanking</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride does not support banking

</blockquote>
</details>

#### playDepartSound
{: .d-none }

<details>
<summary markdown='span'><strong>playDepartSound</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride plays a departure sound when departing the station. depending on sound_range setting, plays Tram or Train departing sound.

</blockquote>
</details>

#### playSplashSound
{: .d-none }

<details>
<summary markdown='span'><strong>playSplashSound</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride should play a splashing sound on down to flat elements

</blockquote>
</details>

#### playSplashSoundSlide
{: .d-none }

<details>
<summary markdown='span'><strong>playSplashSoundSlide</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride should play a splashing sound when entering a water channel, for water coasters. Has no effect if playSplashSound is enabled.  
Note: Internally, water channel track is coded as "covered" track, so if this flag is set for a ride running on a track that supports covered pieces, it will play a splash sound when entering a covered section of track.

</blockquote>
</details>

#### hasShelter
{: .d-none }

<details>
<summary markdown='span'><strong>hasShelter</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride is covered (for example, monorail cars are covered)  
Note that there are some ride types in vanilla RCT2 that seem to have this bit set illogically. Pickup-trucks did not have this set, and the uncovered ski lift cars did have these set. These have been changed in OpenRCT2 to make more sense.

</blockquote>
</details>

#### limitAirTimeBonus
{: .d-none }

<details>
<summary markdown='span'><strong>limitAirTimeBonus</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride should have a hard cap on how much bonus it gets from airtime. This is only set for heartline-twister coasters, and makes it so that a max of ~2 seconds of airtime can give an excitement bonus.

</blockquote>
</details>

#### disableBreakdown
{: .d-none }

<details>
<summary markdown='span'><strong>disableBreakdown</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride does not break down

</blockquote>
</details>

#### noCollisionCrashes
{: .d-none }

<details>
<summary markdown='span'><strong>noCollisionCrashes</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride does not crash when vehicles collide

</blockquote>
</details>

#### disablePainting
{: .d-none }

<details>
<summary markdown='span'><strong>disablePainting</strong>

</summary>
<blockquote>

| **Type**    | `boolean` |
| ----------- | --------- |
| **Default** | `false`   |
|             |           |

**Description:** Flagged if the ride does not support recolouring

</blockquote>
</details>

</blockquote>
</details>

### If (properties.type[] contains "food_stall", "drink_stall", "shop", "information_kiosk", "toilets", "cash_machine", "first_aid")
<blockquote>

**Description:** For a shop/facility

#### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### [Required] sells
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] sells</strong>

</summary>
<blockquote>

**Type:** `array or string`

**Description:** The item(s) sold by the shop

<blockquote>

| Any of                                                  |
| ------------------------------------------------------- |
| [item 0](#allOf_i5_then_then_properties_sells_anyOf_i0) |
| [item 1](#allOf_i5_then_then_properties_sells_anyOf_i1) |
|                                                         |

##### item 0
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
item 0    </strong>
</summary>

<blockquote>

**Type:** `enum (of string)`

Must be one of:
* "burger"
* "chips"
* "ice_cream"
* "candyfloss"
* "pizza"
* "popcorn"
* "hot_dog"
* "tentacle"
* "toffee_apple"
* "doughnut"
* "chicken"
* "pretzel"
* "funnel_cake"
* "beef_noodles"
* "fried_rice_noodles"
* "wonton_soup"
* "meatball_soup"
* "sub_sandwich"
* "cookie"
* "roast_sausage"
* "drink"
* "coffee"
* "lemonade"
* "chocolate"
* "iced_tea"
* "fruit_juice"
* "soybean_milk"
* "sujeonggwa"
* "balloon"
* "toy"
* "map"
* "photo"
* "umbrella"
* "voucher"
* "hat"
* "tshirt"
* "sunglasses"

</blockquote>

</details>

##### item 1
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
item 1    </strong>
</summary>

<blockquote>

</blockquote>

</details>

</blockquote>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

### Else (i.e.  properties.type[] doesn't contain "food_stall", "drink_stall", "shop", "information_kiosk", "toilets", "cash_machine", "first_aid")
<blockquote>

**Description:** For an actual ride

#### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### swingMode
{: .d-none }

<details>
<summary markdown='span'><strong>swingMode</strong>

</summary>
<blockquote>

| **Type**    | `enum (of integer)` |
| ----------- | ------------------- |
| **Default** | `0`                 |
|             |                     |

**Description:** If set to 1 or 2, indicates alternate swing modes that are used for some rides

Must be one of:
* 0
* 1
* 2

</blockquote>
</details>

##### rotationMode
{: .d-none }

<details>
<summary markdown='span'><strong>rotationMode</strong>

</summary>
<blockquote>

| **Type**    | `enum (of integer)` |
| ----------- | ------------------- |
| **Default** | `0`                 |
|             |                     |

**Description:** If set to 1, indicates alternate rotation modes used for twist, if set to 2, indicates alternate rotation mode used for enterprise

Must be one of:
* 0
* 1
* 2

</blockquote>
</details>

##### ratingMultipler
{: .d-none }

<details>
<summary markdown='span'><strong>ratingMultipler</strong>

</summary>
<blockquote>

**Description:** Additional rating multiplier(s) for this specific ride subtype (this is separate from the rating multipliers that are hardcoded for each ride type)

##### excitement
{: .d-none }

<details>
<summary markdown='span'><strong>excitement</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### intensity
{: .d-none }

<details>
<summary markdown='span'><strong>intensity</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### nausea
{: .d-none }

<details>
<summary markdown='span'><strong>nausea</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

</blockquote>
</details>

##### minCarsPerTrain
{: .d-none }

<details>
<summary markdown='span'><strong>minCarsPerTrain</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `1`       |
|             |           |

**Description:** Minimum number of cars that can be in a train

**Example:** 

```json
4
```

</blockquote>
</details>

##### maxCarsPerTrain
{: .d-none }

<details>
<summary markdown='span'><strong>maxCarsPerTrain</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `1`       |
|             |           |

**Description:** Maximum number of cars that can be in a train

**Example:** 

```json
12
```

</blockquote>
</details>

##### carsPerFlatRide
{: .d-none }

<details>
<summary markdown='span'><strong>carsPerFlatRide</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `255`     |
|             |           |

**Description:** The number of cars, for a flat ride

</blockquote>
</details>

##### numEmptyCars
{: .d-none }

<details>
<summary markdown='span'><strong>numEmptyCars</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `0`       |
|             |           |

**Description:** The number of "zero" cars in the train. That is, cars that do not hold any guests

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
|              |        |

</blockquote>
</details>

##### defaultCar
{: .d-none }

<details>
<summary markdown='span'><strong>defaultCar</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `0`       |
|             |           |

**Description:** Index of the car that should be used as the default car for this ride. In other words, this is the normal car that appears throughout the train wherever there isn't a special (i.e. front or rear) car  
0 if not specified

**Example:** 

```json
1
```

</blockquote>
</details>

##### tabCar
{: .d-none }

<details>
<summary markdown='span'><strong>tabCar</strong>

</summary>
<blockquote>

| **Type**    | `number` |
| ----------- | -------- |
| **Default** | `0`      |
|             |          |

**Description:** The index of the car that should show in the gui tab for this ride (0 if not specified)

</blockquote>
</details>

##### tabScale
{: .d-none }

<details>
<summary markdown='span'><strong>tabScale</strong>

</summary>
<blockquote>

**Type:** `number`

**Description:** If <= 0.5, this will scale the size of the tab preview in half

</blockquote>
</details>

##### headCars
{: .d-none }

<details>
<summary markdown='span'><strong>headCars</strong>

</summary>
<blockquote>

**Type:** `array of integer or number`

**Description:** The index(es) of up to three cars that should be used to fill the front of a train

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [items](#allOf_i5_then_else_properties_headCars_items) | -           |
|                                                        |             |

##### items

**Type:** `integer`

**Example:** 

```json
0
```

</blockquote>
</details>

##### tailCars
{: .d-none }

<details>
<summary markdown='span'><strong>tailCars</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Index of the car that should be used as the tail car, if any (the code supports listing an array instead of just a single index here, but currently only the first index listed is used)

</blockquote>
</details>

##### [Required] cars
{: .d-none }

<details>
<summary markdown='span'><strong>[Required] cars</strong>

</summary>
<blockquote>

**Description:** The cars in this ride

<blockquote>

| Any of                                                               |
| -------------------------------------------------------------------- |
| [A car object](#allOf_i5_then_else_properties_cars_anyOf_i0)         |
| [Array of car objects](#allOf_i5_then_else_properties_cars_anyOf_i1) |
|                                                                      |

##### A car object
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
A car object    </strong>
</summary>

<blockquote>

##### rotationFrameMask
{: .d-none }

<details>
<summary markdown='span'><strong>rotationFrameMask</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** A bitmask indicating which rotation frames this car has, for rendering spinning car in the UI?

**Example:** 

```json
31
```

</blockquote>
</details>

##### spacing
{: .d-none }

<details>
<summary markdown='span'><strong>spacing</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The space taken up by this car (I have no idea what the units are tbh)

**Example:** 

```json
146000
```

</blockquote>
</details>

##### mass
{: .d-none }

<details>
<summary markdown='span'><strong>mass</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Mass of this car

**Example:** 

```json
650
```

</blockquote>
</details>

##### tabOffset
{: .d-none }

<details>
<summary markdown='span'><strong>tabOffset</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** If used, adds a vertical offset to this car when rendered in the UI

</blockquote>
</details>

##### numSeats
{: .d-none }

<details>
<summary markdown='span'><strong>numSeats</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Number of seats that this car holds

**Example:** 

```json
1
```

</blockquote>
</details>

##### seatsInPairs
{: .d-none }

<details>
<summary markdown='span'><strong>seatsInPairs</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, indicates that guests sit in this car in pairs

</blockquote>
</details>

##### spriteWidth
{: .d-none }

<details>
<summary markdown='span'><strong>spriteWidth</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite width for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### spriteHeightNegative
{: .d-none }

<details>
<summary markdown='span'><strong>spriteHeightNegative</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite height below the origin for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### spriteHeightPositive
{: .d-none }

<details>
<summary markdown='span'><strong>spriteHeightPositive</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite height above the origin for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### animation
{: .d-none }

<details>
<summary markdown='span'><strong>animation</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `0`       |
|             |           |

**Description:** Indicates a special animation mode to use for this car.  

1: Miniature Railway  
2: Swan boats  
3: Canoes  
4: Row boats  
5: Water tricycles  
6: Observation tower  
7: Helicars  
8: Monorail cycles  
9: Multidimensional Coaster

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |
|              |        |

</blockquote>
</details>

##### baseNumFrames
{: .d-none }

<details>
<summary markdown='span'><strong>baseNumFrames</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The number of frames (angles) of rotation when this car is flat. This number is always calculated now so it shouldn't be specified

</blockquote>
</details>

##### numImages
{: .d-none }

<details>
<summary markdown='span'><strong>numImages</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The total number of sprites for this car. This number is always calculated now so it shouldn't be specified

</blockquote>
</details>

##### numSeatRows
{: .d-none }

<details>
<summary markdown='span'><strong>numSeatRows</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
1
```

</blockquote>
</details>

##### spinningInertia
{: .d-none }

<details>
<summary markdown='span'><strong>spinningInertia</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### spinningFriction
{: .d-none }

<details>
<summary markdown='span'><strong>spinningFriction</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### frictionSoundId
{: .d-none }

<details>
<summary markdown='span'><strong>frictionSoundId</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
57
```

</blockquote>
</details>

##### logFlumeReverserVehicleType
{: .d-none }

<details>
<summary markdown='span'><strong>logFlumeReverserVehicleType</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
0
```

</blockquote>
</details>

##### soundRange
{: .d-none }

<details>
<summary markdown='span'><strong>soundRange</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### doubleSoundFrequency
{: .d-none }

<details>
<summary markdown='span'><strong>doubleSoundFrequency</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### poweredAcceleration
{: .d-none }

<details>
<summary markdown='span'><strong>poweredAcceleration</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### poweredMaxSpeed
{: .d-none }

<details>
<summary markdown='span'><strong>poweredMaxSpeed</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### carVisual
{: .d-none }

<details>
<summary markdown='span'><strong>carVisual</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### effectVisual
{: .d-none }

<details>
<summary markdown='span'><strong>effectVisual</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### drawOrder
{: .d-none }

<details>
<summary markdown='span'><strong>drawOrder</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
7
```

</blockquote>
</details>

##### numVerticalFramesOverride
{: .d-none }

<details>
<summary markdown='span'><strong>numVerticalFramesOverride</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** When VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES is set, this value overrides the calculated value

</blockquote>
</details>

##### loadingPositions
{: .d-none }

<details>
<summary markdown='span'><strong>loadingPositions</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** A list of the different loading positions for this car

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingPositions_items) | -           |
|                                                                              |             |

##### items

**Type:** `array of integer or integer`

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingPositions_items_items) | -           |
|                                                                                    |             |

##### items

**Type:** `integer`

</blockquote>
</details>

##### loadingWaypoints
{: .d-none }

<details>
<summary markdown='span'><strong>loadingWaypoints</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** A list of the different loading waypoints guests should use for this car

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingWaypoints_items) | -           |
|                                                                              |             |

##### items

**Type:** `array of integer or integer`

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingWaypoints_items_items) | -           |
|                                                                                    |             |

##### items

**Type:** `integer`

</blockquote>
</details>

##### numSegments
{: .d-none }

<details>
<summary markdown='span'><strong>numSegments</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** If loadingWaypoints is used, the number of segments

</blockquote>
</details>

##### frames
{: .d-none }

<details>
<summary markdown='span'><strong>frames</strong>

</summary>
<blockquote>

**Description:** A list of the different sets of sprites that this car has

##### flat
{: .d-none }

<details>
<summary markdown='span'><strong>flat</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for flat track

</blockquote>
</details>

##### gentleSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for gentle slopes

</blockquote>
</details>

##### steepSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>steepSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for steep slopes

</blockquote>
</details>

##### verticalSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>verticalSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for vertical slopes

</blockquote>
</details>

##### diagonalSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>diagonalSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for diagonal slopes

</blockquote>
</details>

##### flatBanked
{: .d-none }

<details>
<summary markdown='span'><strong>flatBanked</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked, flat track

</blockquote>
</details>

##### inlineTwists
{: .d-none }

<details>
<summary markdown='span'><strong>inlineTwists</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for inline twists

</blockquote>
</details>

##### flatToGentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>flatToGentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for flat track to banked gentle sloped track

</blockquote>
</details>

##### diagonalGentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>diagonalGentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for diagonal banked to unbanked, gentle sloped track transitions

</blockquote>
</details>

##### gentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked to unbanked, gentle sloped track transitions

</blockquote>
</details>

##### gentleSlopeBankedTurns
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopeBankedTurns</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked gentle sloping turns

</blockquote>
</details>

##### flatToGentleSlopeWhileBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>flatToGentleSlopeWhileBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked flat track to banked gentle slope

</blockquote>
</details>

##### corkscrews
{: .d-none }

<details>
<summary markdown='span'><strong>corkscrews</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for corkscrews

</blockquote>
</details>

##### restraintAnimation
{: .d-none }

<details>
<summary markdown='span'><strong>restraintAnimation</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for restraints opening and closing

</blockquote>
</details>

##### curvedLiftHill
{: .d-none }

<details>
<summary markdown='span'><strong>curvedLiftHill</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for a curved lift-hill

</blockquote>
</details>

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_POWERED_RIDE_UNRESTRICTED_GRAVITY
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_POWERED_RIDE_UNRESTRICTED_GRAVITY</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on powered vehicles that do not slow down when going down a hill

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_NO_UPSTOP_WHEELS
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_NO_UPSTOP_WHEELS</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_MINI_GOLF
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_MINI_GOLF</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_4
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_4</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_5
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_5</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_HAS_INVERTED_SPRITE_SET
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_HAS_INVERTED_SPRITE_SET</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on vehicles that support running inverted for extended periods of time, i.e. the Flying, Lay-down and Multi-dimension RCs.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_DODGEM_INUSE_LIGHTS
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_DODGEM_INUSE_LIGHTS</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** When set the vehicle has an additional frame for when in use. Used only by dodgems.

</blockquote>
</details>

##### ~~VEHICLE_ENTRY_FLAG_ALLOW_DOORS_DEPRECATED~~
{: .d-none }

<details>
<summary markdown='span'><strong>~~VEHICLE_ENTRY_FLAG_ALLOW_DOORS_DEPRECATED~~</strong>

</summary>
<blockquote>

| **Type**       | `boolean`                                             |
| -------------- | ----------------------------------------------------- |
| **Deprecated** | ![badge](https://img.shields.io/badge/Deprecated-red) |
|                |                                                       |

**Description:** [Deprecated] Not used any more since every vehicle will now work with doors

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_2
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_2</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_10
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_10</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_11
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_11</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Setting this will cause the game to use numVerticalFramesOverride instead of calculating it

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_13
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_13</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SPINNING_ADDITIONAL_FRAMES
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SPINNING_ADDITIONAL_FRAMES</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** 16x additional frames for vehicle. A spinning item with additional frames must always face forward to load/unload. Spinning without can load/unload at 4 rotations.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_LIFT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_LIFT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_1
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_1</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SWINGING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SWINGING</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SPINNING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SPINNING</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_POWERED
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_POWERED</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_RIDERS_SCREAM
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_RIDERS_SCREAM</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_21
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_21</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Swinging coaster??

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_BOAT_HIRE_COLLISION_DETECTION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_BOAT_HIRE_COLLISION_DETECTION</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_VEHICLE_ANIMATION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_VEHICLE_ANIMATION</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on animated vehicles like the Multi-dimension coaster trains, Miniature Railway locomotives and Helicycles.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_RIDER_ANIMATION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_RIDER_ANIMATION</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_25
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_25</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SLIDE_SWING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SLIDE_SWING</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on dingy slides. They have there own swing value calculations and have a different amount of images.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_CHAIRLIFT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_CHAIRLIFT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_WATER_RIDE
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_WATER_RIDE</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on rides where water would provide continuous propulsion

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_GO_KART
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_GO_KART</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_DODGEM_CAR_PLACEMENT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_DODGEM_CAR_PLACEMENT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

</blockquote>

</details>

##### Array of car objects
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
Array of car objects    </strong>
</summary>

<blockquote>

**Type:** `array`

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [carItem](#allOf_i5_then_else_properties_cars_anyOf_i1_items) | -           |
|                                                               |             |

##### carItem

##### rotationFrameMask
{: .d-none }

<details>
<summary markdown='span'><strong>rotationFrameMask</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** A bitmask indicating which rotation frames this car has, for rendering spinning car in the UI?

**Example:** 

```json
31
```

</blockquote>
</details>

##### spacing
{: .d-none }

<details>
<summary markdown='span'><strong>spacing</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The space taken up by this car (I have no idea what the units are tbh)

**Example:** 

```json
146000
```

</blockquote>
</details>

##### mass
{: .d-none }

<details>
<summary markdown='span'><strong>mass</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Mass of this car

**Example:** 

```json
650
```

</blockquote>
</details>

##### tabOffset
{: .d-none }

<details>
<summary markdown='span'><strong>tabOffset</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** If used, adds a vertical offset to this car when rendered in the UI

</blockquote>
</details>

##### numSeats
{: .d-none }

<details>
<summary markdown='span'><strong>numSeats</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** Number of seats that this car holds

**Example:** 

```json
1
```

</blockquote>
</details>

##### seatsInPairs
{: .d-none }

<details>
<summary markdown='span'><strong>seatsInPairs</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, indicates that guests sit in this car in pairs

</blockquote>
</details>

##### spriteWidth
{: .d-none }

<details>
<summary markdown='span'><strong>spriteWidth</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite width for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### spriteHeightNegative
{: .d-none }

<details>
<summary markdown='span'><strong>spriteHeightNegative</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite height below the origin for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### spriteHeightPositive
{: .d-none }

<details>
<summary markdown='span'><strong>spriteHeightPositive</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** For manually entering the sprite height above the origin for this car. This is only used if VEHICLE_ENTRY_FLAG_10 is set, which seems to only be for non-tracked-rides (?), otherwide this value is calculated.

</blockquote>
</details>

##### animation
{: .d-none }

<details>
<summary markdown='span'><strong>animation</strong>

</summary>
<blockquote>

| **Type**    | `integer` |
| ----------- | --------- |
| **Default** | `0`       |
|             |           |

**Description:** Indicates a special animation mode to use for this car.  

1: Miniature Railway  
2: Swan boats  
3: Canoes  
4: Row boats  
5: Water tricycles  
6: Observation tower  
7: Helicars  
8: Monorail cycles  
9: Multidimensional Coaster

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |
|              |        |

</blockquote>
</details>

##### baseNumFrames
{: .d-none }

<details>
<summary markdown='span'><strong>baseNumFrames</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The number of frames (angles) of rotation when this car is flat. This number is always calculated now so it shouldn't be specified

</blockquote>
</details>

##### numImages
{: .d-none }

<details>
<summary markdown='span'><strong>numImages</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** The total number of sprites for this car. This number is always calculated now so it shouldn't be specified

</blockquote>
</details>

##### numSeatRows
{: .d-none }

<details>
<summary markdown='span'><strong>numSeatRows</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
1
```

</blockquote>
</details>

##### spinningInertia
{: .d-none }

<details>
<summary markdown='span'><strong>spinningInertia</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### spinningFriction
{: .d-none }

<details>
<summary markdown='span'><strong>spinningFriction</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### frictionSoundId
{: .d-none }

<details>
<summary markdown='span'><strong>frictionSoundId</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
57
```

</blockquote>
</details>

##### logFlumeReverserVehicleType
{: .d-none }

<details>
<summary markdown='span'><strong>logFlumeReverserVehicleType</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
0
```

</blockquote>
</details>

##### soundRange
{: .d-none }

<details>
<summary markdown='span'><strong>soundRange</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### doubleSoundFrequency
{: .d-none }

<details>
<summary markdown='span'><strong>doubleSoundFrequency</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### poweredAcceleration
{: .d-none }

<details>
<summary markdown='span'><strong>poweredAcceleration</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### poweredMaxSpeed
{: .d-none }

<details>
<summary markdown='span'><strong>poweredMaxSpeed</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### carVisual
{: .d-none }

<details>
<summary markdown='span'><strong>carVisual</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### effectVisual
{: .d-none }

<details>
<summary markdown='span'><strong>effectVisual</strong>

</summary>
<blockquote>

**Type:** `integer`

</blockquote>
</details>

##### drawOrder
{: .d-none }

<details>
<summary markdown='span'><strong>drawOrder</strong>

</summary>
<blockquote>

**Type:** `integer`

**Example:** 

```json
7
```

</blockquote>
</details>

##### numVerticalFramesOverride
{: .d-none }

<details>
<summary markdown='span'><strong>numVerticalFramesOverride</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** When VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES is set, this value overrides the calculated value

</blockquote>
</details>

##### loadingPositions
{: .d-none }

<details>
<summary markdown='span'><strong>loadingPositions</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** A list of the different loading positions for this car

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingPositions_items) | -           |
|                                                                              |             |

##### items

**Type:** `array of integer or integer`

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingPositions_items_items) | -           |
|                                                                                    |             |

##### items

**Type:** `integer`

</blockquote>
</details>

##### loadingWaypoints
{: .d-none }

<details>
<summary markdown='span'><strong>loadingWaypoints</strong>

</summary>
<blockquote>

**Type:** `array`

**Description:** A list of the different loading waypoints guests should use for this car

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingWaypoints_items) | -           |
|                                                                              |             |

##### items

**Type:** `array of integer or integer`

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [items](#allOf_i5_then_else_properties_cars_anyOf_i0_loadingWaypoints_items_items) | -           |
|                                                                                    |             |

##### items

**Type:** `integer`

</blockquote>
</details>

##### numSegments
{: .d-none }

<details>
<summary markdown='span'><strong>numSegments</strong>

</summary>
<blockquote>

**Type:** `integer`

**Description:** If loadingWaypoints is used, the number of segments

</blockquote>
</details>

##### frames
{: .d-none }

<details>
<summary markdown='span'><strong>frames</strong>

</summary>
<blockquote>

**Description:** A list of the different sets of sprites that this car has

##### flat
{: .d-none }

<details>
<summary markdown='span'><strong>flat</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for flat track

</blockquote>
</details>

##### gentleSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for gentle slopes

</blockquote>
</details>

##### steepSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>steepSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for steep slopes

</blockquote>
</details>

##### verticalSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>verticalSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for vertical slopes

</blockquote>
</details>

##### diagonalSlopes
{: .d-none }

<details>
<summary markdown='span'><strong>diagonalSlopes</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for diagonal slopes

</blockquote>
</details>

##### flatBanked
{: .d-none }

<details>
<summary markdown='span'><strong>flatBanked</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked, flat track

</blockquote>
</details>

##### inlineTwists
{: .d-none }

<details>
<summary markdown='span'><strong>inlineTwists</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for inline twists

</blockquote>
</details>

##### flatToGentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>flatToGentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for flat track to banked gentle sloped track

</blockquote>
</details>

##### diagonalGentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>diagonalGentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for diagonal banked to unbanked, gentle sloped track transitions

</blockquote>
</details>

##### gentleSlopeBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopeBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked to unbanked, gentle sloped track transitions

</blockquote>
</details>

##### gentleSlopeBankedTurns
{: .d-none }

<details>
<summary markdown='span'><strong>gentleSlopeBankedTurns</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked gentle sloping turns

</blockquote>
</details>

##### flatToGentleSlopeWhileBankedTransitions
{: .d-none }

<details>
<summary markdown='span'><strong>flatToGentleSlopeWhileBankedTransitions</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for banked flat track to banked gentle slope

</blockquote>
</details>

##### corkscrews
{: .d-none }

<details>
<summary markdown='span'><strong>corkscrews</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for corkscrews

</blockquote>
</details>

##### restraintAnimation
{: .d-none }

<details>
<summary markdown='span'><strong>restraintAnimation</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for restraints opening and closing

</blockquote>
</details>

##### curvedLiftHill
{: .d-none }

<details>
<summary markdown='span'><strong>curvedLiftHill</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** If set, this car has sprites for a curved lift-hill

</blockquote>
</details>

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_POWERED_RIDE_UNRESTRICTED_GRAVITY
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_POWERED_RIDE_UNRESTRICTED_GRAVITY</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on powered vehicles that do not slow down when going down a hill

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_NO_UPSTOP_WHEELS
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_NO_UPSTOP_WHEELS</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_MINI_GOLF
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_MINI_GOLF</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_4
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_4</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_5
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_5</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_HAS_INVERTED_SPRITE_SET
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_HAS_INVERTED_SPRITE_SET</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on vehicles that support running inverted for extended periods of time, i.e. the Flying, Lay-down and Multi-dimension RCs.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_DODGEM_INUSE_LIGHTS
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_DODGEM_INUSE_LIGHTS</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** When set the vehicle has an additional frame for when in use. Used only by dodgems.

</blockquote>
</details>

##### ~~VEHICLE_ENTRY_FLAG_ALLOW_DOORS_DEPRECATED~~
{: .d-none }

<details>
<summary markdown='span'><strong>~~VEHICLE_ENTRY_FLAG_ALLOW_DOORS_DEPRECATED~~</strong>

</summary>
<blockquote>

| **Type**       | `boolean`                                             |
| -------------- | ----------------------------------------------------- |
| **Deprecated** | ![badge](https://img.shields.io/badge/Deprecated-red) |
|                |                                                       |

**Description:** [Deprecated] Not used any more since every vehicle will now work with doors

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_2
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_2</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_10
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_10</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_11
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_11</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Setting this will cause the game to use numVerticalFramesOverride instead of calculating it

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_13
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_13</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SPINNING_ADDITIONAL_FRAMES
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SPINNING_ADDITIONAL_FRAMES</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** 16x additional frames for vehicle. A spinning item with additional frames must always face forward to load/unload. Spinning without can load/unload at 4 rotations.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_LIFT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_LIFT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_1
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_1</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SWINGING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SWINGING</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SPINNING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SPINNING</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_POWERED
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_POWERED</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_RIDERS_SCREAM
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_RIDERS_SCREAM</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_21
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_21</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Swinging coaster??

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_BOAT_HIRE_COLLISION_DETECTION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_BOAT_HIRE_COLLISION_DETECTION</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_VEHICLE_ANIMATION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_VEHICLE_ANIMATION</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on animated vehicles like the Multi-dimension coaster trains, Miniature Railway locomotives and Helicycles.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_RIDER_ANIMATION
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_RIDER_ANIMATION</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_25
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_25</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_SLIDE_SWING
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_SLIDE_SWING</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on dingy slides. They have there own swing value calculations and have a different amount of images.

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_CHAIRLIFT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_CHAIRLIFT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_WATER_RIDE
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_WATER_RIDE</strong>

</summary>
<blockquote>

**Type:** `boolean`

**Description:** Set on rides where water would provide continuous propulsion

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_GO_KART
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_GO_KART</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

##### VEHICLE_ENTRY_FLAG_DODGEM_CAR_PLACEMENT
{: .d-none }

<details>
<summary markdown='span'><strong>VEHICLE_ENTRY_FLAG_DODGEM_CAR_PLACEMENT</strong>

</summary>
<blockquote>

**Type:** `boolean`

</blockquote>
</details>

</blockquote>

</details>

</blockquote>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</blockquote>

</details>

# If Scenery Group
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Scenery Group    </strong>
</summary>

```If (objectType = "scenery_group")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_1"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Footpath Banner
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Footpath Banner    </strong>
</summary>

```If (objectType = "footpath_banner")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_2"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Footpath Item
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Footpath Item    </strong>
</summary>

```If (objectType = "footpath_item")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_3"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Large Scenery
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Large Scenery    </strong>
</summary>

```If (objectType = "scenery_large")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_4"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Small Scenery
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Small Scenery    </strong>
</summary>

```If (objectType = "scenery_small")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_5"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Wall
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Wall    </strong>
</summary>

```If (objectType = "scenery_wall")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_6"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Station
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Station    </strong>
</summary>

```If (objectType = "station")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_7"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Terrain Edge
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Terrain Edge    </strong>
</summary>

```If (objectType = "terrain_edge")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_8"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Terrain Surface
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Terrain Surface    </strong>
</summary>

```If (objectType = "terrain_surface")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_9"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

# If Water
{: .d-none }

<details>
<summary markdown='span'>
    <strong>
If Water    </strong>
</summary>

```If (objectType = "water")```
<blockquote>

### properties
{: .d-none }

<details>
<summary markdown='span'><strong>properties</strong>

</summary>
<blockquote>

##### <a name="autogenerated_heading_10"></a>The following properties are required
* textHeight
* scrollingMode

</blockquote>
</details>

</blockquote>

</details>

</blockquote>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-05-11 at 02:14:03 -0400