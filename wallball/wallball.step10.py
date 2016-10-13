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

N_BLOCKS = 8
BLOCK_W = WIDTH / N_BLOCKS
BLOCK_H = BLOCK_W / 4
BLOCK_COLOURS = "purple", "lightgreen", "lightblue", "orange"

#
# Create <N_BLOCKS> blocks, filling the full width of the screen. 
# Each block is as high as a quarter of its width, so they remain
# proportional as the number of blocks or the screen size changes.
#
# The block colours cycle through <BLOCK_COLOURS>
#
blocks = []
for n_block in range(N_BLOCKS):
    block = Rect(n_block * BLOCK_W, 0, BLOCK_W, BLOCK_H)
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
    #
    # Move the ball along its current direction
    #
    dx, dy = ball.direction
    ball.move_ip(dx, dy)

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

