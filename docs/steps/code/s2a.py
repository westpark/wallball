WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
#
# The ball is a square red block halfway across the game screen
#
ball = Ball(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.colour = "red"

def draw():
    #
    # Clear the screen and place the ball at its current position
    #
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
