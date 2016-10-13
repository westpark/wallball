WIDTH = 640
HEIGHT = 480

#
# The ball is a square red block which starts in the middle
# of the screen moving towards the lower-right.
#
ball = Rect(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.direction = 5, -5
ball.colour = "red"

def draw():
    """Redraw the entire screen:
    
    * Clear the background
    * Draw the ball
    """
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
