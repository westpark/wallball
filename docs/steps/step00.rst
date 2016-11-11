.. _step0:

Step 0: Create an empty game
----------------------------

In this step we're going to create a game which does nothing, just to make
sure we have everything ready to run.

The Code
~~~~~~~~

.. literalinclude:: code/s0.py

That's it. You just need an empty file. That's the simplest possible "game"
you can build with PyGame Zero. 

What's happening here?
~~~~~~~~~~~~~~~~~~~~~~

In fact, PyGame Zero is doing a lot of work on your behalf. If this
were a "real" PyGame program, in order to get a window which did nothing
and which closed when you pressed Ctrl+Q, you'd have to write a dozen lines
of code. If you want to see what that would look like, look at the PyGame
Zero primer.

That's just to get the game to do nothing! Eventually you'll need something
which PyGame Zero doesn't provide and which PyGame itself does and then
you'll start to write code directly in PyGame. PyGame Zero is deliberately
limited.

Change it around
~~~~~~~~~~~~~~~~

Although all you have is an empty screen with nothing moving on it,
you can still change a few things. If you want to change the size of
the game window, add the following lines to the top of your program::

    WIDTH = 640
    HEIGHT = 480

and if you want to give the game window a title, add this line::

    TITLE = "Wall Ball"

Obviously you can choose your own size and your own title.

