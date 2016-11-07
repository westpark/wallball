WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
#
# The ball is a red square halfway across the game screen
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

class Bat(ZRect): pass
#
# The bat is a green oblong which starts just along the bottom
# of the screen and halfway across.
#
BAT_W = 150
BAT_H = 15
bat = Bat(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
bat.colour = "green"

def draw():
    #
    # Clear the screen and place the ball at its current position
    #
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(bat, bat.colour)

def on_mouse_move(pos):
    #
    # Make the bat follow the horizontal movement of the mouse.
    #
    x, y = pos
    bat.centrex = x

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
