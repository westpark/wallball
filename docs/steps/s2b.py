WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
#
# The ball is a square red block halfway across the game screen
#
ball = Ball(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.colour = "red"
#
# The ball moves one step right and one step down each tick
#
ball.direction = 1, 1
#
# The ball moves at a speed of 3 steps each tick
#
ball.speed = 3

def draw():
    #
    # Clear the screen and place the ball at its current position
    #
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)

def update():
    #
    # Move the ball along its current direction at its current speed
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)
