WIDTH = 640
HEIGHT = 480

#
# Create a series of difficulty levels, specifying
# the speed & size of the ball and the width of the bat.
#
levels = [
    {"speed" : 3, "ball_size" : (30, 30), "bat_width" : 150},
    {"speed" : 4, "ball_size" : (24, 24), "bat_width" : 100},
    {"speed" : 5, "ball_size" : (12, 12), "bat_width" : 72},
]

class Game(object): pass
game = Game()
game.score = 0
game.status = "Starting"
game.score_per_brick = 1
game.current_level = 0
game.scoreboard = []

#
# Create a status display, as wide as the screen and 60 pixels high.
# It's placed at the bottom of the screen
#
STATUS_DISPLAY = ZRect(0, HEIGHT - 60, WIDTH, 60)

#
# Create a game window which is as wide as the screen but allows
# a status display underneath
#
GAME_WINDOW = ZRect(0, 0, WIDTH, HEIGHT - STATUS_DISPLAY.height - 1)
GAME_WINDOW.background_colour = "darkblue"
GAME_WINDOW.frame_colour = "white"

class Ball(ZRect): pass
#
# The ball is a red square halfway across the game window
#
ball_size = levels[game.current_level]['ball_size']
ball = Ball(GAME_WINDOW.center, ball_size)
ball.colour = "red"
#
# The ball moves one step right and one step down each tick
#
ball.direction = 1, 1
#
# The ball moves at a speed of 3 steps each tick
#
ball.speed = levels[game.current_level]['speed']

class Bat(ZRect): pass
#
# The bat is a green oblong which starts just along the bottom
# of the game window and halfway across.
#
BAT_W = levels[game.current_level]['bat_width']
BAT_H = BAT_W / 10
bat = Bat(GAME_WINDOW.centerx, GAME_WINDOW.bottom - BAT_H, BAT_W, BAT_H)
bat.colour = "green"

class Brick(ZRect): pass
#
# The brick is a rectangle one eight the width of the game window
# and one quarter high as it is wide.
#
N_BRICKS = 8
BRICK_W = GAME_WINDOW.width / N_BRICKS
BRICK_H = BRICK_W / 4
BRICK_COLOURS = ["purple", "lightgreen", "lightblue", "orange"]
#
# The brick colours cycle through <BRICK_COLOURS>
#
bricks = []

def reset_game():
    #
    # At the beginning of the game, centre the ball on the game window
    # and position the bat halfway across the game window and and sliding
    # along its bottom edge.
    #
    ball.center = GAME_WINDOW.center
    bat.center = (GAME_WINDOW.centerx, GAME_WINDOW.bottom - BAT_H)
    #
    # Create <N_BRICKS> blocks, filling the full width of the game window.
    # Each brick is as high as a quarter of its width, so they remain
    # proportional as the number of blocks or the screen size changes.
    #
    bricks.clear()
    for n_brick in range(N_BRICKS):
        brick = Brick(
            GAME_WINDOW.left + (n_brick * BRICK_W), GAME_WINDOW.top,
            BRICK_W, BRICK_H
        )
        brick.colour = BRICK_COLOURS[n_brick % len(BRICK_COLOURS)]
        bricks.append(brick)
    game.current_level = 0
    set_up_level()

def set_up_level():
    level = levels[game.current_level]
    ball.speed = level['speed']
    ball.size = level['ball_size']
    bat.width = level['bat_width']
    bat.height = bat.width / 10
    game.score_per_brick = 1 + game.current_level

def draw_scoreboard():
    top_10_scores = sorted(game.scoreboard, reverse=True)[:10]


def draw():
    #
    # Clear the screen, draw the game window and place the ball at its current position
    #
    screen.clear()
    #
    # Draw the game window and a frame around it
    #
    screen.draw.filled_rect(GAME_WINDOW, GAME_WINDOW.background_colour)
    screen.draw.rect(GAME_WINDOW.inflate(+2, +2), GAME_WINDOW.frame_colour)

    #
    # Fill in the status window
    #
    if game.status == "Starting":
        #
        # If the game is waiting to start indicate how to start
        #
        screen.draw.text("Press SPACE to start", center=STATUS_DISPLAY.center)

    elif game.status == "Running":
        #
        # If the game is running show the current status, centred inside the status area
        #
        screen.draw.text("Score: %d" % game.score, left=STATUS_DISPLAY.left + 4, centery=STATUS_DISPLAY.centery)
        screen.draw.text("Status: %s" % game.status, right=STATUS_DISPLAY.right - 4, centery=STATUS_DISPLAY.centery)

    #
    # Fill in the gameplay window
    #
    if game.status == "Starting":
        #
        # If the game is waiting to start, show the current high scoreboard
        #
        draw_scoreboard()

    elif game.status == "Running":
        screen.draw.filled_rect(ball, ball.colour)
        screen.draw.filled_rect(bat, bat.colour)
        for brick in bricks:
            screen.draw.filled_rect(brick, brick.colour)
            screen.draw.textbox("%s" % game.score_per_brick, brick)

def on_mouse_move(pos):
    #
    # Make the bat follow the horizontal movement of the mouse.
    # Ensure that the bat does not move outside the game window.
    #
    if game.status == "Running":
        x, y = pos
        bat.centerx = x
        bat.clamp_ip(GAME_WINDOW)

def on_mouse_down(button):
    #
    # If the right button is pressed make the game more difficult
    # by shrinking the bat and the ball and increasing the speed.
    # If the left button is pressed, make it easier again.
    # The score on each brick goes up or down corresponding to
    # how much harder / easier the game is.
    #
    if button == mouse.RIGHT:
        if game.current_level < len(levels):
            game.current_level += 1
    elif button == mouse.LEFT:
        if game.current_level > 0:
            game.current_level -= 1
    set_up_level ()

def on_key_down(key):
    if game.status == "Starting":
        if key == keys.SPACE:
            reset_game()
            game.status = "Running"

def update():
    if game.status == "Running":
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
            game.score += game.score_per_brick
            ball.direction = dx, -dy

        #
        # Bounce the ball off the left or right walls
        #
        if ball.right >= GAME_WINDOW.right or ball.left <= GAME_WINDOW.left:
            ball.direction = -dx, dy

        #
        # If the ball hits the bottom wall, you lose
        #
        if ball.bottom >= GAME_WINDOW.bottom:
            game.status = "Starting"

        #
        # Bounce the ball off the top wall
        #
        if ball.top <= GAME_WINDOW.top:
            ball.direction = dx, -dy

        #
        # If there are no bricks left, you win
        #
        if not bricks:
            game.scoreboard.append(game.score)
            game.status = "Starting"