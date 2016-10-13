WIDTH = 800
HEIGHT = 600

class Ball(ZRect): pass
#
# The ball is a square red block which starts in the middle
# of the screen moving towards the lower-right.
#
BALL_W = 30
BALL_H = BALL_W
ball = Ball(WIDTH / 2, HEIGHT / 2, BALL_W, BALL_H)
ball.direction = 1, 1
ball.speed = 1
ball.colour = "red"

class Bat(ZRect): pass
#
# The bat is a green oblong which starts just above the bottom
# of the screen and halfway across.
#
BAT_W = 150
BAT_H = 15
bat = Bat(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
bat.colour = "green"

N_BLOCKS = 8
BLOCK_W = WIDTH / N_BLOCKS
BLOCK_H = BLOCK_W / 4
BLOCK_COLOURS = "purple", "lightgreen", "lightblue", "orange"

class Block(ZRect): pass
#
# Create <N_BLOCKS> blocks, filling the full width of the screen. 
# Each block is as high as a quarter of its width, so they remain
# proportional as the number of blocks or the screen size changes.
#
# The block colours cycle through <BLOCK_COLOURS>
#
blocks = []
for n_block in range(N_BLOCKS):
    block = Block(n_block * BLOCK_W, 0, BLOCK_W, BLOCK_H)
    block.colour = BLOCK_COLOURS[n_block % len(BLOCK_COLOURS)]
    blocks.append(block)

def draw_blocks():
    """Draw all the remaining blocks on the screen, each in its
    own colour and at its own position. Any blocks which have
    been "killed" won't be in the list and so won't be drawn.
    """
    for block in blocks:
        screen.draw.filled_rect(block, block.colour)

def draw():
    """Redraw the entire screen:
    
    * Clear the background
    * Draw the ball
    * Draw the bat
    """
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(bat, bat.colour)
    draw_blocks()

def on_mouse_move(pos):
    """Make the bat follow the horizontal movement of the mouse.
    Make sure it doesn't run off the left or right of the screen
    """
    x, y = pos
    bat.centrex = x

def update():
    """Move the ball and then determine what effect its new position has
    """
    dt = 1
    #
    # Move the ball along its current direction
    #
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx * dt, ball.speed * dy * dt)

    #
    # If the ball hits a rectangle, kill that rectangle and
    # bounce the ball.
    #
    to_kill = ball.collidelist(blocks)
    if to_kill >= 0:
        sounds.block.play()
        blocks.pop(to_kill)
        ball.direction = dx, -dy

    #
    # Bounce the ball off the right or left walls
    #
    if ball.right >= WIDTH or ball.left <= 0:
        sounds.blip.play()
        ball.direction = -dx, dy

    #
    # Bounce the ball off the bat
    #
    if ball.colliderect(bat):
        sounds.blip.play()
        ball.direction = dx, -dy

    #
    # Bounce the ball off the top wall
    #
    if ball.top <= 0:
        sounds.blip.play()
        ball.direction = dx, -dy

    #
    # If the ball hits the bottom of the screen, you lose
    #
    if ball.bottom >= HEIGHT:
        sounds.die.play()
        exit()
    
    #
    # If there are no blocks left, you win
    #
    if not blocks:
        sounds.win.play()
        exit()
