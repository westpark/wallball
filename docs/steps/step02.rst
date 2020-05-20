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

**At the end of Step 2a you will see:** a green bat along the bottom of the
screen. It won't move yet, and it won't stop the ball.

.. image:: images/step-s2a.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s2a.py
    :diff: code/s1c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We make the bat in the same way as the ball: a coloured rectangle, only with a different
  shape and a different colour.

* We draw it in the same way as well, inside the ``draw`` function.

Change it around
~~~~~~~~~~~~~~~~

* Change the colour of the bat
* Change the size of the bat
* Change where the bat starts

Step 2b: Control the bat with the mouse
---------------------------------------

**At the end of Step 2b you will see:** the bat being moved by the mouse. It
still won't stop the ball which will bounce off the floor

.. image:: images/step-s2b.gif
   :scale: 66 %

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

  **Hint:** The bat -- like any PyGame rectangle -- has a centerx and a centery attribute

* Make the bat move only when one of the buttons is pressed

  **Hint:** As well as an :func:`on_mouse_move` event, PyGame Zero has :func:`on_mouse_down`
  and :func:`on_mouse_up` events, which pass in the mouse position and which button was pressed.

Step 2c: Make the ball bounce off the bat
-----------------------------------------

**At the end of Step 2c you will see:** the ball bouncing off the bat. The ball
can still bounce off the floor

.. image:: images/step-s2c.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s2c.py
    :diff: code/s2b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* The ``colliderect`` function detects when one rectangle (the ball) has collided
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

**At the end of Step 2d you will see:** the game end if the ball hits the
floor instead of bouncing off the bat

.. image:: images/step-s2d.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s2d.py
    :diff: code/s2c.py
    :linenos:
