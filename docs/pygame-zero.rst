.. _pg0:

PyGame Zero
===========

PyGame Zero is a wrapper around PyGame so you don't have to do quite
so much work. PyGame Zero objects are PyGame objects. PyGame Zero
defines a default game loop with some standard handlers and lets
you get on with the game logic. Once you outgrow its simplicity you
can easily switch to "proper" PyGame.

When you run an *empty* PyGame Zero file with the ``pgzrun`` command, this code (roughly) 
is already running for you behind the scenes::

    import pygame

    pygame.init()

    size = 800, 600
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and \
                    event.mod & (pygame.KMOD_CTRL | pygame.KMOD_META):
                    sys.exit()
        
        screen.fill(pygame.Color("black"))
        pygame.display.flip()
        clock.tick(60)

.. _pg0-constants:

Magic Constants
---------------

PyGame Zero defines a few constants (which much be spelt exactly as they are
below) which have a special meaning. 

* :const:`WIDTH` determines how wide the game window is
* :const:`HEIGHT` determines how high the game window is
* :const:`TITLE` is the text which will be in the titlebar of the game window
* :const:`ICON` is the path to an image file which will be used as the icon for the game window

Magic Functions
---------------

PyGame Zero defines a few functions which you can write and which are
called in a particular way as part of the game loop.

.. _pg0-functions:

..  py:function:: update

    In this function you should perform any work which involves changing the positions, sizes,
    images &c. of objects which will be drawn in the `draw` function.
    
    Do *not* draw/blit anything to the screen here: that should be done in the :func:`draw` function

..  py:function:: draw

    Draw whatever's needed to the screen.
    
    Do not do calculations here: those should be done in the :func:`update` function

.. _pg0-events:

..  py:function:: on_mouse_down(pos, button)
    
    Called when a mouse button is pressed.
    Provides pos as x, y and the number of the button pressed
    
..  py:function:: on_mouse_up(pos, button)
    
    Called when a mouse button is released.
    Provides pos as x, y and the number of the button pressed

..  py:function:: on_mouse_move(pos, rel, buttons)
    
    Called when the mouse is moved
    Provides pos as x, y; rel as the relative movement dx, dy; and buttons which were pressed

..  py:function:: on_key_down(key, mod)
    
    Called when a key is pressed
    Provides: key as a PyGame integer; mod as a bitmask of modifiers

..  py:function:: on_key_up(key, mod)
    
    Called when a key is released
    Provides: key as a PyGame integer; mod as a bitmask of modifiers

Mouse Buttons, Keys & Modifiers
-------------------------------

Mouse Buttons
~~~~~~~~~~~~~

All these are part of the `mouse` object.

* ``LEFT``
* ``MIDDLE``
* ``RIGHT``
* ``WHEEL_UP``
* ``WHEEL_DOWN``

Keys
~~~~

All these are part of the `keys` object.

* Numbers are: :const:`keys.K_1`, :const:`keys.K_2`, &c.
* Letters are: :const:`keys.A`, :const:`keys.B`, &c.
* Movement keys are: :const:`keys.UP`, :const:`keys.DOWN`, :const:`keys.LEFT`, :const:`keys.RIGHT`, :const:`keys.HOME`, :const:`keys.END`, :const:`keys.PAGEUP`, :const:`keys.PAGEDOWN`
* Function keys are: :const:`keys.F1`, :const:`keys.F2`, &c.
* Most other keys are their full spoken name in caps, eg :const:`keys.RIGHTBRACKET`, :const:`keys.QUESTION`, :const:`keys.AT` &c.

Modifiers
~~~~~~~~~

All these are part of the `keymods` object.

* Shifts are: :const:`keymods.SHIFT`, :const:`keymods.LSHIFT`, :const:`keymods.RSHIFT`
* Ctrls are: :const:`keymods.CTRL`, :const:`keymods.LCTRL`, :const:`keymods.RCTRL`
* Alts are: :const:`keymods.ALT`, :const:`keymods.LALT`, :const:`keymods.RALT`

.. _pg0-colours:

Colours
-------

Colours can be any of:

* An (R, G, B) sequence, eg ``(255, 0, 0)`` for solid red
* An HTML colour name, eg ``"red"``
* An HTML hex colour string, eg ``"#FF0000"``

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