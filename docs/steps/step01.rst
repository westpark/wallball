.. _step1:

Step 1: Bounce a ball around the screen
=======================================

In this step we're going to put a square "ball" on the screen and
then to make it move, bouncing off each of the walls when it hits them.

Step 1a: Put a ball on the screen
---------------------------------

The Code
~~~~~~~~

.. note:: Normally code which you should type is highlighted in yellow. Since this
          is the first code in the worksheet, you need to type it all in. I haven't
          highlighted it all in yellow!

.. literalinclude:: code/s1a.py

What's happening?
~~~~~~~~~~~~~~~~~

* A ``Ball`` is a PyGame Zero rectangle object. Its position is centred on the size of the
  game window: if the window is made bigger, the ball will still be in the middle.
  When you create a PyGame rectangle object, you give it four numbers: x, y, w, h
  
  **NB** Although the first two numbers are using the :const:`WIDTH` & :const:`HEIGHT` constants, they
  represent the x, y position of the ball.

* The ``draw`` function is a :ref:`special function <pg0-functions>` which PyGame Zero calls to show whatever
  needs to be there on the game screen. In this case, we just clear the screen every
  time and draw the ball.

Change it around
~~~~~~~~~~~~~~~~

* Change the colour of the ball.

  **Hint**: there's a :ref:`list of colours <pg0-colours>` in the PyGame Zero section.

* Change the size of the ball

  **Hint**: the last two numbers inside the ``ball = Ball(...)`` constructor are its initial size.

* Change where the ball appears

  **Hint**: the first two numbers inside the ``ball = Ball(...)`` constructor are its initial position.

* Have the ball appear somewhere different every time

  **Hint**: you can import the ``random`` module and use the function ``randint``
  to select where the ball starts from

Step 1b: Make the ball move
---------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s1b.py
    :diff: code/s1a.py
    :linenos:


What's happening?
~~~~~~~~~~~~~~~~~

* We give the ball a direction and a speed (like a Vector, if you know what that is).

* The `update` function is another :ref:`special function <pg0-functions>` which is called by PyGame Zero on
  every tick of its clock: it's where we calculate how much our different objects
  have moved. You don't put anything on the screen in the ``update`` function, only
  in the ``draw`` function.
  
* ``ball.move_ip`` tells PyGame to change the position of the ball rectangle by
  the requested amount. The "ip" part of that stands for "in-place": it moves
  the ball itself; there  is an equivalent called just ``ball.move`` that returns
  a new ball object which has been moved by the requested amount.

Change it around
~~~~~~~~~~~~~~~~

* Make the ball move faster or slower
* Change the angle at which the ball moves
  
  **Hint**: the angle is determined by the ball's direction which 
  combines an x and a y component.

Step 1c: Make the ball bounce off the walls
-------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s1c.py
    :diff: code/s1b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* In our program :const:`WIDTH` is the width of the window the game is running in
  and :const:`HEIGHT` is its height. Although you can normally give variables like
  this whatever name you liked (such as ``W`` and ``H`` or ``x_extent`` and ``y_extent``),
  when you're using PyGame Zero, the names :const:`WIDTH` and :const:`HEIGHT` have a special
  meaning and must be spelt exactly that way.

* When the edge of the ball reaches the left or right-hand edge of the screen, we
  change its horizontal direction only so it appears to bounce back off the wall.
  
* When the edge of the ball reaches the top or bottom edge of the screen, we
  change its vertical direction only.

Change it around
~~~~~~~~~~~~~~~~

* Make the ball bounce differently on different walls, eg make the angle of reflection
  vary between the top/bottom and left/right walls.
