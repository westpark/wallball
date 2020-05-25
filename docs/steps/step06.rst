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

.. image:: images/step-s6a.gif
   :scale: 66 %

The Code
~~~~~~~~

..  literaldiff:: code/s6a.py
    :diff: code/s5c.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

This is the easiest of the parts of step 6: we're simply using the ``game``
object to keep track of how much each brick will currently score when it's
knocked out, and we're showing that number on each brick. When a brick is
knocked out, the game score increases by that brick's score. (Which is always
1!)

Change it around
~~~~~~~~~~~~~~~~

*   Give each brick colour a different score.

    **Hint:** Use a dictionary to map brick colours to scores


Step 6b: Make the game harder / easier
--------------------------------------

.. image:: images/step-s6b.gif
   :scale: 66 %

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

  *NB In Python, the first item in a list is Number 0, the second item is
  Number 1 and so on. There are good reasons for this, but it takes some
  getting used to.*

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


Step 6c: Show the top 10 scores
-------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s6c.py
    :diff: code/s6b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* As part of the overall `game` object we set up a scoreboard, initially empty.
  The `scoreboard` object is, for the moment, a Python list to which we will
  add the score as each game completes.

* If the game is waiting to start (ie the status is "Starting") then show the
  scoreboard in place of the gameplay window. We're keeping this simple: since
  we know there will be no more than 10 entries, we're dividing the window
  into 12 slices, the bottom 10 of which will contain the scores.

* Finally, when each game completes -- when no bricks remain -- then take
  the score at that point and add it to the list of scores.

Change it around
~~~~~~~~~~~~~~~~

*   Do a Top 5 or a Top 20 rather than a Top 10

    **Hint:** Within the `draw_scoreboard` function, create a variable
    which specifies how many scores you want to show; use that, suitably
    adjusted, whenever an exact number appears through the rest of the
    function.

*   Keep track of the time as well as the score to provide a tie-breaker

    **Hint:** Instead of holding the score as a number in the `scoreboard`
    object, hold a 2-tuple instead containing the score and the number of
    seconds.
