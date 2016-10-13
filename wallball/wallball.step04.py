WIDTH = 640
HEIGHT = 480

#
# The ball is a square red block which starts in the middle
# of the screen moving towards the lower-right.
#
ball = Rect(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.direction = 5, -5
ball.colour = "red"

#
# The bat is a green oblong which starts just above the bottom
# of the screen and halfway across.
#
bat = Rect(WIDTH / 2, 0.96 * HEIGHT, 150, 15)
bat.colour = "green"

def draw():
    """Redraw the entire screen:
    
    * Clear the background
    * Draw the ball
    * Draw the bat
    """
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(bat, bat.colour)

def on_mouse_move(pos):
    """Make the bat follow the horizontal movement of the mouse.
    Make sure it doesn't run off the left or right of the screen
    """
    x, y = pos
    bat.centrex = x
