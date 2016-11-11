.. _step2:

Step 2: Make the ball bounce off the bat
========================================

In this step we're going to put an oblong "bat" along the bottom of the
screen. It will move left and right when the player moves the mouse.
When the ball hits the bat it will bounce off it.

Finally, now that we have a bat in place, the player will die if the ball
reaches the bottom edge of the screen.

Step 2a: Put a bat on the screen
--------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s2a.py
    :diff: code/s1c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We make the bat in the same way as the ball: a coloured rectangle, only with a different
  shape and a different colour.
  
* We draw it in the same way as well, inside the `draw` function.

Change it around
~~~~~~~~~~~~~~~~

* Change the colour of the bat
* Change the size of the bat
* Change where the bat starts

Step 2b: Control the bat with the mouse
---------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s2b.py
    :diff: code/s2a.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* When the mouse is moved, PyGame Zero automatically calls a function called
  `on_mouse_move` and passes in the current position of the mouse. We're only
  interested in the horizontal movement, so we pick out the x-coordinate.
  
* By setting the bat's x-centre to the same as the mouse's x-coordinate whenever
  the mouse moves, we make the bat move horizontally with the mouse.

Change it around
~~~~~~~~~~~~~~~~

* Make the bat move left & right according to the up and down movement of the mouse

  **Hint:** The mouse position has two components: x & y -- guess which one you want to use?
  
* Make the bat move up and down as well as left and right

  **Hint:** The bat -- like any PyGame rectangle as a centerx and a centery attribute
  
* Make the bat move only when one of the buttons is pressed

  **Hint:** As well as an `on_mouse_move` event, PyGame Zero has `on_mouse_down`
  and `on_mouse_up` events, which pass in the mouse position and which button was pressed.

Step 2c: Make the ball bounce off the bat
-----------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s2c.py
    :diff: code/s2b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* The colliderect function detects when one rectangle (the ball) has collided
  with another rectangle (the bat). As soon as this happens, we reverse the
  vertical direction of the ball (its y-direction) and it appears to "bounce"
  off the bat.

Change it around
~~~~~~~~~~~~~~~~

* Make the ball go backwards when it hits the bat

  **Hint:** At the moment, we only change the ball's y-direction when we
  detect a collision with the bat.
  
* Make the ball go randomly faster or slower when it hits the bat

Step 2d: The player dies if the ball hits the bottom of the screen
------------------------------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s2d.py
    :diff: code/s2c.py
    :linenos:
