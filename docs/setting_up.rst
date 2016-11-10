Setting Up
==========

Before we start programming, we need to make sure everything's in place for us to write
our code and run it.

Create a working directory
--------------------------

* Run a terminal prompt

* If there isn't one, create a directory called `wallball`::

    mkdir wallball

* Switch to that directory::

    cd wallball

* Make sure pgzrun, the PyGame Zero runner, is available::
    
    which pgzrun

* Leave the terminal prompt open; we'll use it to run the game

Create an empty file
--------------------

* Start IDLE3 and select File > New
  
  (Or use some other editor which you prefer)

* File > Save As > `~/wallball/<name>.py`

  (Don't actually put <name>: put your name in)

Run the game
------------

* Go to the terminal prompt and type::

    pgzrun <name>.py
  
  So if it was my game, I'd type::
  
    pgzrun tim.py
  
.. note:: Whenever you need to run the game, you don't need to type that in again;
          just press the up-arrow key on the keyboard and the last command will be
          selected. Then just press the <Enter> key to run the command.