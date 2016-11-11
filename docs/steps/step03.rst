.. _step3:

Step 3: Add bricks for the ball to knock out
============================================

In this step we're going to put a row of "bricks" along the top of the
game screen, each one a different colour. When the ball hits a brick,
the brick disappears. When all the bricks have been knocked out, the
player has won.

Step 3a: Put one brick on the screen
------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s3a.py
    :diff: code/s2d.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* The brick is another PyGame rectangle. At first, we're only going to create one of it.
  Later, we'll use it like a potato print to generate several bricks in a row.

* Since we want the bricks to fit evenly across the screen, we decide how many we want
  (`N_BRICKS`) and then divide the screen width (`WIDTH`) by that many to get the width 
  of each brick (`BRICK_W`). We could have done it the other way round: decide how wide 
  our brick should be and then seen how many could fit across the screen.

* To keep the brick proportions similar if we change the screen size, we make the height
  of each brick (`BRICK_H`) a quarter of its width (`BRICK_W`).

* To keep things simple in this step, we just create one brick at the top-left corner
  of the screen. (And it's blue because... why not?). In the next step we'll get rid
  of this one brick and create a row of them.

Change it around
~~~~~~~~~~~~~~~~

* Change the colour of the brick
* Make the brick appear at the right of the screen

  **Hint:** You can position the left-hand edge of the brick one brick-width away
  (`BRICK_W`) from the right-hand edge of the screen (`WIDTH`).

Step 3b: Put eight bricks across the screen
-------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s3b.py
    :diff: code/s3a.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

There's quite a bit going on in this step: we're multiplying our one brick by eight
and looping round a list of possible colours.

* `BRICK_COLOURS` is a sequence of colour names which is called a "list" in Python.
  You can add as many colour names to it as you like. The list of possible colours
  is quite long (cf https://en.wikipedia.org/wiki/X11_color_names) but you can
  guess some obvious ones, and there's a shorter list in the PyGame Zero section at
  the end of these worksheets.
  
* From lines 46 to 52 we are creating a list of bricks. Each brick is made from the
  `Brick` class we created previously, but each one has a different position and a
  different colour.

* Some of the lines start with "## DELETE"; these are the lines we used to create one
  brick on the previous step which we're now going to delete.

* A "for loop" in Python starts with a "for ... in ...:" and then every line which
  should happen as part of the same loop is intended (pushed in to the right) by
  the same amount. As soon as Python sees a line which is back out to the left again,
  it treats it as separate from the loop.

* Line 51 selects the brick colour by picking the next colour from the list of
  colours and then looping back to the beginning when it reaches the end. (That's
  what the "% len(...)" part is doing. This means that you can have as many or as
  few colours as you like with as many or as few bricks as you like without having
  to match the number of colours with the number of bricks.
  
  The "%" thing is called a modulo operator. It gives you what's left over when
  you divide something by something else.

* Lines 61 to 63 are using the list of bricks and drawing them, each at its own
  position and with its own colour.


Change it around
~~~~~~~~~~~~~~~~

* Change the number of bricks
* Change how high each brick is
* Add or remove some colours
* Make each brick a randomly-chosen colour

  **Hint:** You will need to import the `random` module and use the `random.choice` function.

Step 3c: Have the ball knock out bricks until none is left
----------------------------------------------------------

The Code
~~~~~~~~

..  literaldiff:: code/s3c.py
    :diff: code/s3b.py
    :linenos:

What's happening?
~~~~~~~~~~~~~~~~~

* `collidelist` checks whether one rectangle has collided with *any* of a list of
  rectangles. It returns the position in the list of the rectangle which was the
  point of collision. If there was no collision, it returns -1.
  
  Since our ball is a rectangle and our bricks are a list of rectangles, this gives
  us an easy way to work out which brick was hit by the ball (if any). If one is
  hit (`to_kill >= 0`) we drop that brick from our list (`bricks.pop`) and bounce
  the ball.
  
  Now that the brick is not in the list, it will not be drawn the next time we
  redraw the screen and it will appear to have knocked out.

* The games ends in success when there are no bricks left. The line `if not bricks:`
  is Python shorthand for saying: if the list of bricks is empty -- ie if there are
  no bricks left.

Change it around
~~~~~~~~~~~~~~~~

* Have the ball change colour according to which brick it's knocked out

  **Hint:** When you detect the collision between the ball and one of the bricks,
  before popping the brick from the list of bricks, copy its colour to the ball's
  colour.

