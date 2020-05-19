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
ball.direction = 1, 1
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
left_bat = Bat(0, HEIGHT - BAT_H, BAT_W, BAT_H)
left_bat.colour = "green"
right_bat = Bat(WIDTH - BAT_W, HEIGHT - BAT_H, BAT_W, BAT_H)
right_bat.colour = "green"
bats = [left_bat, right_bat]

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
    for b in bats:
        screen.draw.filled_rect(b, b.colour)
    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos, buttons):
    #
    # Make the bat follow the horizontal movement of the mouse.
    #
    x, y = pos
    left, middle, right = buttons
    if left:
        left_bat.centerx = x
        if left_bat.colliderect(right_bat):
            left_bat.right = right_bat.left - 1
    if right:
        right_bat.centerx = x
        if right_bat.colliderect(left_bat):
            right_bat.left = left_bat.right - 1

def update():
    #
    # Move the ball along its current direction at its current speed
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    #
    # Bounce the ball off the bat
    #
    if ball.collidelist(bats) > -1:
        ball.direction = dx, -dy

    #
    # If the ball hits a brick, kill that brick and
    # bounce the ball.
    #
    to_kill = ball.collidelist(bricks)
    if to_kill >= 0:
        bricks.pop(to_kill)
        ball.direction = dx, -dy

    #
    # Now that we have left & right bats, if the ball
    # hits either wall, you lose.
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