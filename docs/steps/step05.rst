.. _step4:

Step 5: Start and restart the game
==================================

Up to now, the game has started when you run it and closed when
you either win or lose. In this step, we'll add a new context:
waiting for the game to start for the first time, or to restart
after a game has completed.

This involves introducing the idea of a status for the game: either
"Starting": waiting for the game to begin; or "Running": playing the
game. Depending on which status is current, we will show different
things on the screen and react differently to keypresses, mouse
movements etc.

Step 5a: Add and display a Running status
-----------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s5a.py
    :diff: code/s4c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We add a ``status`` attribute to the existing ``game`` object is
  initially set to "Running".
* We add the game status to the status display below the game, pushing
  the score to the left to make room.


Step 5b: Move the gameplay inside the gameplay window
-----------------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s5b.py
    :diff: code/s5a.py
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

