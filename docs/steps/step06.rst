.. _step6:

Step 6: Make the game harder and add a scoreboard
=================================================

At this point, the "game" isn't really much of a
game: as long as you don't lose control of the mouse,
you're pretty much guaranteed to knock all the blocks
out. This also means that the score doesn't really have
much meaning since everyone who finishes will score the
same!

In this step, we're going to add several gameplay elements:

* If right mouse key is pressed, the bat and ball will
  both grow smaller and the ball will become faster. They can
  right-click several times up to a limit. The smaller/faster
  the bat/ball are, the higher the score when a brick is
  knocked out.

* If the left mouse key is pressed, the speed/sizes will move
  back towards what they were at the start of the game.

* We will indicate the score on each brick as well as keeping
  track of the running score at the bottom of the screen.

* At the end of the round, we'll have a separate screen showing
  a high score list. (For the moment, without names: just the
  scores).

Step 6a: Show the scores on each brick
--------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s6a.py
    :diff: code/s5c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

This is the easiest of the parts of step 6: we're simply using the ``game``
object to keep track of how much each brick will currently score when it's
knocked out, and we're showing that number on each brick.

Change it around
~~~~~~~~~~~~~~~~

*   Give each brick colour a different score.

    **Hint:** Use a dictionary to map brick colours to scores


Step 6b: Make the game harder / easier
--------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s6b.py
    :diff: code/s6a.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* We create three levels of difficulty, specifying for each one how fast
  the ball moves and how big it is, and how big the bat is. For now, we're
  going to the use the level counter as the brick score.

* When the mouse buttons are pressed, we go down or up through the levels,
  not allowing the level to go below zero nor to go beyond the levels we've
  specified. The check ``if game.current_level < len(levels)`` checks that
  we're not going to go beyond the number of levels we have *whatever that
  number is*. We could just have checked for three levels (because that's
  how many we know we have). But this way, we can add some more levels of
  difficulty, or remove some, and the code will work without any other
  changes.

* Since we'll be writing the same code at the beginning of the game and
  every times a user moves through the levels, we factor it out into its
  own function, called ``set_up_level``.

Change it around
~~~~~~~~~~~~~~~~

* Add more levels and play with the ones which are there

* Show the current level in the status window along with the score

* Allow the brick score to vary with the levels

* Allow use of the up- and down-arrow keys on the keyboard to change levels.
  Likewise allow the left- and right-arrow keys to control the bat.


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