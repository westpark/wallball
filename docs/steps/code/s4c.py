WIDTH = 640
HEIGHT = 480

class Game(object): pass
game = Game()
game.status = "running"

STATUS_H = 60
GAME_VIEW = ZRect(0, 0, WIDTH, HEIGHT - STATUS_H)
GAME_VIEW.inflate_ip(-2, -2)
VIEW_COLOUR = "darkblue"
GAME_FRAME = ZRect(GAME_VIEW)
GAME_FRAME.inflate_ip(+2, +2)
FRAME_COLOUR = "white"

class Ball(ZRect): pass
#
# The ball is a red square halfway across the game screen
#
ball = Ball(GAME_VIEW.center, (30, 30))
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
bat = Bat(GAME_VIEW.centerx, GAME_VIEW.bottom - BAT_H, BAT_W, BAT_H)
bat.colour = "green"

class Brick(ZRect): pass
#
# The brick is a rectangle one eight the width of the game screen
# and one quarter high as it is wide.
#
N_BRICKS = 8
BRICK_W = GAME_VIEW.width / N_BRICKS
BRICK_H = BRICK_W / 4
BRICK_COLOURS = "purple", "lightgreen", "lightblue", "orange"
#
# Create <N_BRICKS> blocks, filling the full width of the screen. 
# Each brick is as high as a quarter of its width, so they remain
# proportional as the number of blocks or the screen size changes.
#
# The brick colours cycle through <BRICK_COLOURS>
#
bricks = []
for n_brick in range(N_BRICKS):
    brick = Brick(GAME_VIEW.left + (n_brick * BRICK_W), GAME_VIEW.top, BRICK_W, BRICK_H)
    brick.colour = BRICK_COLOURS[n_brick % len(BRICK_COLOURS)]
    bricks.append(brick)

def draw():
    #
    # Clear the screen and place the ball at its current position
    #
    screen.clear()
    screen.draw.filled_rect(GAME_VIEW, VIEW_COLOUR)
    screen.draw.rect(GAME_FRAME, FRAME_COLOUR)
    screen.draw.text(
        "Status: %s" % game.status, 
        topleft = (GAME_VIEW.left, GAME_VIEW.bottom + 4)
    )
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(bat, bat.colour)
    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    #
    # Make the bat follow the horizontal movement of the mouse.
    #
    x, y = pos
    bat.centrex = x
    bat.clamp_ip(GAME_VIEW)

def update():
    #
    # Move the ball along its current direction at its current speed
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    #
    # Bounce the ball off the bat
    #
    if ball.colliderect(bat):
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
    # Bounce the ball off the left or right walls
    #
    if ball.right >= GAME_VIEW.right or ball.left <= GAME_VIEW.left:
        ball.direction = -dx, dy

    #
    # If the ball hits the bottom of the screen, you lose
    #
    if ball.bottom >= GAME_VIEW.bottom:
        exit()
    
    #
    # Bounce the ball off the top wall
    #
    if ball.top <= GAME_VIEW.top:
        ball.direction = dx, -dy

    #
    # If there are no bricks left, you win
    #
    if not bricks:
        exit()
