Step 2: Bounce a ball around the screen
=======================================

In this step we're going to put a square "ball" on the screen and
then to make it move, bouncing off each of the walls when it hits them.

Step 2a: Put a ball on the screen
---------------------------------

The Code
~~~~~~~~

.. literalinclude:: code/s2a.py

What's happening?
~~~~~~~~~~~~~~~~~

* A `Ball` is a PyGame Zero rectangle object. Its position is centred on the size of the
  game window: if the window is made bigger, the ball will still be in the middle.
  When you create a PyGame rectangle object, you give it four numbers: x, y, w, h
  
  *NB Although the first two numbers are using the `WIDTH` & `HEIGHT` constants, they
  represent the x, y position of the ball`*.

* The `draw` function is a special function which PyGame Zero calls to show whatever
  needs to be there on the game screen. In this case, we just clear the screen every
  time and draw the ball.

Change it around
~~~~~~~~~~~~~~~~

* Change the colour of the ball
* Change the size of the ball
* Change where the ball appears
* Have the ball appear somewhere different every time

Step 2b: Make the ball move
---------------------------

The Code
~~~~~~~~

.. literalinclude:: code/s2b.py

What's happening?
~~~~~~~~~~~~~~~~~

* We give the ball a direction and a speed (like a Vector, if you know what that is).

* The `update` function is the other function which is called by PyGame Zero on
  every tick of its clock: it's where we calculate how much our different objects
  have moved. You don't put anything on the screen in the `update` function, only
  in the `draw` function.
  
* `ball.move_ip` tells PyGame to change the position of the ball rectangle by
  the requested amount.

Change it around
~~~~~~~~~~~~~~~~

* Make the ball move faster or slower
* Change the angle at which the ball moves

Step 2c: Make the ball bounce off the walls
-------------------------------------------

The Code
~~~~~~~~

.. literalinclude:: code/s2c.py

What's happening?
~~~~~~~~~~~~~~~~~

* When the edge of the ball reaches the left or right-hand edge of the screen, we
  change its horizontal direction only so it appears to bounce back off the wall.
  
* When the edge of the ball reaches the top or bottom edge of the screen, we
  change its vertical direction only.

Change it around
~~~~~~~~~~~~~~~~

* Make the ball bounce differently on different walls
