.. _step5:

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


Step 5b: Have the game pause before starting
--------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s5b.py
    :diff: code/s5a.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We make sure that certain pieces of code only run when the game is Running,
  not when it's waiting to start.

* We add one new piece of functionality: if the game is Starting
  (ie waiting to start) we wait until the Space key is pressed and
  then change the status to Running, causing the other parts of the
  program to kick in.

Change it around
~~~~~~~~~~~~~~~~

* Choose a different key to make the game start

* Display a message in the status window to indicate which key should be
  pressed.


Step 5c: Allow the game to restart once it's complete
-----------------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s5c.py
    :diff: code/s5b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We move into its own function all the changes needed to restart the game.

* When Space is pressed, we reset the game before switching to Running mode

* When the game completes (win or lose) we switch back to Starting mode
  rather than dropping straight out.

Change it around
~~~~~~~~~~~~~~~~

* Add a "Kill" key which, when pressed, aborts the game and waits to restart.

* In  the status line, display the most recent result (win or lose) before
  restarting.