WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
#
# The ball is a red square halfway across the game screen
#
ball = Ball(0, 0, 30, 30)
ball.center = WIDTH / 2, HEIGHT / 2
ball.colour = "red"
#
# The ball moves one step right and one step down each tick
#
ball.direction = 1.0, 1.0
#
# The ball moves at a speed of 3 steps each tick
#
ball.speed = 3

class Bat(ZRect): pass
#
# The bat is a green oblong which starts just along the bottom
# of the screen and halfway across.
#
BAT_W = 150
BAT_H = 15
bat = Bat(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
bat.colour = "green"

class Brick(ZRect): pass
#
# The brick is a rectangle one eight the width of the game screen
# and one quarter high as it is wide.
#
N_BRICKS = 8
BRICK_W = WIDTH / N_BRICKS
BRICK_H = BRICK_W / 4
BRICK_COLOURS = ["purple", "lightgreen", "lightblue", "orange"]
#
# Create <N_BRICKS> blocks, filling the full width of the screen.
# Each brick is as high as a quarter of its width, so they remain
# proportional as the number of blocks or the screen size changes.
#
# The brick colours cycle through <BRICK_COLOURS>
#
bricks = []
for n_brick in range(N_BRICKS):
    brick = Brick(n_brick * BRICK_W, 0, BRICK_W, BRICK_H)
    brick.colour = BRICK_COLOURS[n_brick % len(BRICK_COLOURS)]
    bricks.append(brick)

def draw():
    #
    # Clear the screen and place the ball at its current position
    #
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(bat, bat.colour)
    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    #
    # Make the bat follow the horizontal movement of the mouse.
    #
    x, y = pos
    bat.centerx = x

def update():
    #
    # Move the ball along its current direction at its current speed
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    #
    # Bounce the ball off the bat
    # The direction and angle of the ball will vary according
    # to how long the bat the ball hits
    #
    if ball.colliderect(bat):
        dballx = (ball.centerx - bat.centerx) / (bat.width / 2)
        ball.direction = dballx, -dy

    #
    # If the ball hits a brick, kill that brick and
    # bounce the ball.
    #
    to_kill = ball.collidelist(bricks)
    if to_kill >= 0:
        bricks.pop(to_kill)
        ball.direction = dx, -dy

    #
    # Bounce the ball off the left or right walls
    #
    if ball.right >= WIDTH or ball.left <= 0:
        ball.direction = -dx, dy

    #
    # If the ball hits the bottom of the screen, you lose
    #
    if ball.bottom >= HEIGHT:
        exit()

    #
    # Bounce the ball off the top wall
    #
    if ball.top <= 0:
        ball.direction = dx, -dy

    #
    # If there are no bricks left, you win
    #
    if not bricks:
        exit()