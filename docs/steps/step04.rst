.. _step4:

Step 4: Show a running score
============================

This is a small step in concept: keep count of how many bricks have
been knocked out and show that score underneath the game window.

But it involves two changes:

* Keeping track of the state of the game -- in this case, the score.
* Putting the gameplay inside a window and other information outside it

First we'll push the gameplay inside a window, in two steps. Then
we'll add a status line and keep track of the score.

Step 4a: Create a gameplay window
------------------------------------

..  note::

    At the end of this step, the game will still be showing across
    the entire window but the new gameplay window will show where
    it will be showing at the end of the next step.

.. image:: images/step-s4a.gif
   :scale: 66 %


The Code
~~~~~~~~

..  literaldiff:: code/s4a.py
    :diff: code/s3c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We're creating a rectangle to hold the gameplay window which is
  is 50 pixels smaller than the screen which holds the entire game.

* To create a blue filling and a white border, we draw a filled-in
  rectangle in blue and then a slightly larger, unfilled rectangle
  in white which fits around it.

Change it around
~~~~~~~~~~~~~~~~

* Change the colours of the gameplay window
* Make the gameplay window not be centred on the screen.

  **Hint:** The line which "inflates" the gameplay rectangle by 50 pixels
  in each direction is just a shortcut for playing with its `width` and
  `height` and `x` and `y` attributes. You can change them directly.

Step 4b: Move the gameplay inside the gameplay window
-----------------------------------------------------

.. image:: images/step-s4b.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s4b.py
    :diff: code/s4a.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

This is quite a busy step, but a lot of the changes are mechanical substitutions.

*   In short, wherever we were previously assuming that we were playing within
    the whole width of the game screen, we now have to assume that we are
    playing only within the gameplay window. So, for example, checking whether
    the ball has hit the left-hand edge of the screen (``ball.left <= 0``) now
    has to check instead whether we've hit the left-hand edge of the gameplay
    window (``ball.left <= GAME_WINDOW.left``).

*   One particular change is to keep the bat within the gameplay
    window. By default, the mouse will stay within the game screen so we
    didn't have to do anything to stop the bat going too far to the left or right.
    Now, though, if we don't "clamp" the bat within the gameplay window, it would
    start to move outside its borders if the mouse is moved too far. You can
    see this change in the ``on_mouse_move`` code.

Change it around
~~~~~~~~~~~~~~~~

* Allow the bat to move outside the gameplay window to see what happens
* Have the bricks occupy a smaller width than the entire width of the
  gameplay window.


Step 4c: Add a running score count
----------------------------------

.. image:: images/step-s4c.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s4c.py
    :diff: code/s4b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

We're introducing the concept of game state: a programming object which keeps
track of various aspects of the game. In this step, we're just tracking the
score; in the next step, we'll use this to introduce the idea of different
screens (a "welcome" screen, a "scoreboard" screen etc.).

* We create a global game object whose only attribute is a score,
  which we initialise to zero.

* We add a status window: another on-screen rectangle at the bottom
  of the display. We adjust the size of the gameplay window to fit
  alongside it.

* To keep track of the score, we simply add one to the score every time
  a brick is knocked out.

* The `screen.draw.text` function is a very flexible way of getting text
  onto the screen.

Change it around
~~~~~~~~~~~~~~~~

* Have each brick colour give a different score

  **Hint**: `bricks.pop` returns the brick you've just popped. You can
  get a brick's colour from its `.colour` attribute.

* Play around with the text: make it left-aligned, a different colour,
  a different font, &c.

