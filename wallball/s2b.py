WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
#
# The ball is a square red block at position (200, 200)
#
ball = Ball(200, 200, 30, 30)
ball.colour = "red"
ball.direction = 1, 1
ball.speed = 3

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)

def update():
    #
    # Move the ball along its current direction
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)
