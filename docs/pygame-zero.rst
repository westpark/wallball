.. _pg0:

PyGame Zero
===========

Magic Constants
---------------

* `WIDTH` determines how wide the game window is
* `HEIGHT` determines how high the game window is
* `TITLE` is the text which will be in the titlebar of the game window
* `ICON` is the path to an image file which will be used as the icon for the game window

Magic Functions
---------------

.. _pg0-functions:

**update**
    In this function perform any work which involves changing the positions, sizes,
    images &c. of objects which will be drawn in the `draw` function.
    
    Do *not* draw/blit anything to the screen here: that should be done in the `draw` function

**draw**
    Draw whatever's needed to the screen.
    
    Do not do calculations here: those should be done in the `update` function

.. _pg0-events:

**on_mouse_down(pos, button)**
    Called when a mouse button is pressed.
    Provides pos as x, y and the number of the button pressed
    
**on_mouse_up(pos, button)**
    Called when a mouse button is released.
    Provides pos as x, y and the number of the button pressed

**on_mouse_move(pos, rel, buttons)**
    Called when the mouse is moved
    Provides pos as x, y; rel as the relative movement dx, dy; and buttons which were pressed

**on_key_down(key, mod)**
    Called when a key is pressed
    Provides: key as a PyGame integer; mod as a bitmask of modifiers

**on_key_up(key, mod)**
    Called when a key is released
    Provides: key as a PyGame integer; mod as a bitmask of modifiers

Mouse Buttons, Keys & Modifiers
-------------------------------

Mouse Buttons
~~~~~~~~~~~~~

All these are part of the `mouse` object.

* `LEFT`
* `MIDDLE`
* `RIGHT`
* `WHEEL_UP`
* `WHEEL_DOWN`

Keys
~~~~

All these are part of the `keys` object.

* Numbers are: `keys.K_1`, `keys.K_2`, &c.
* Letters are: `keys.A`, `keys.B`, &c.
* Movement keys are: `keys.UP`, `keys.DOWN`, `keys.LEFT`, `keys.RIGHT`, `keys.HOME`, `keys.END`, `keys.PAGEUP`, `keys.PAGEDOWN`
* Function keys are: `keys.F1`, `keys.F2`, &c.
* Most other keys are their full spoken name in caps, eg `keys.RIGHTBRACKET`, `keys.QUESTION`, `keys.AT` &c.

Modifiers
~~~~~~~~~

All these are part of the `keymods` object.

* Shifts are: `keymods.SHIFT`, `keymods.LSHIFT`, `keymods.RSHIFT`
* Ctrls are: `keymods.CTRL`, `keymods.LCTRL`, `keymods.RCTRL`
* Alts are: `keymods.ALT`, `keymods.LALT`, `keymods.RALT`

.. _pg0-colours:

Colours
-------

Colours can be any of:

* An (R, G, B) sequence, eg (255, 0, 0) for solid red
* An HTML colour name, eg "red"
* An HTML hex colour string, eg #FF0000

Some examples
~~~~~~~~~~~~~

* AliceBlue
* beige
* black
* blue
* BlueViolet
* brown
* CadetBlue
* chartreuse
* coral
* CornflowerBlue
* cornsilk
* cyan
* DarkGreen
* DarkOliveGreen
* DarkOrange
* DarkOrchid
* DarkSalmon
* DarkSlateBlue
* DarkViolet
* DeepSkyBlue
* DodgerBlue
* firebrick
* FloralWhite
* ForestGreen
* gold
* grey
* green
* GreenYellow
* HotPink
* ivory
* khaki
* lavender
* LawnGreen
* light
* LightBlue
* LimeGreen
* linen
* magenta
* maroon
* MidnightBlue
* MintCream
* NavyBlue
* orange
* OrangeRed
* orchid
* PaleGreen
* PaleTurquoise
* plum
* PowderBlue
* purple
* red
* RoyalBlue
* SeaGreen
* SkyBlue
* SlateGray
* thistle
* tomato
* turquoise
* violet
* white
* yellow