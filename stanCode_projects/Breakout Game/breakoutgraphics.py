"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Here is the basic version of breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # pre-setting
        self.ball_r = ball_radius
        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.paddle_off = paddle_offset
        self.num_row = brick_rows
        self.num_col = brick_cols
        self.brick_w = brick_width
        self.brick_h = brick_height
        self.brick_off = brick_offset
        self.brick_space = brick_spacing
        self.title = title

        # Create a graphical window, with some extra space
        self.window_w = self.num_col * (self.brick_w + self.brick_space) - self.brick_space
        self.window_h = self.brick_off + 3 * (self.num_row * (self.brick_h + self.brick_space) - self.brick_space)
        self.window = GWindow(width=self.window_w, height=self.window_h, title=self.title)

        # Create a paddle and place it at the middle bottom of window, with some extra space
        self.paddle = GRect(self.paddle_w, self.paddle_h)
        self.paddle.filled = True
        self.paddle.x = (self.window_w - self.paddle_w) / 2
        self.paddle.y = self.window_h - (self.paddle_h + self.paddle_off)
        self.window.add(self.paddle)

        # Center a filled ball and place it at the middle of window
        self.ball = GOval(self.ball_r * 2, self.ball_r * 2)
        self.ball.filled = True
        self.ball.x = self.window_w/2 - self.ball_r
        self.ball.y = self.window_h/2 - self.ball_r
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = self.set_ball_dx()
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.to_start = False
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(self.num_row):
            for j in range(self.num_col):
                brick = GRect(self.brick_w, self.brick_h)
                brick.filled = True

                # color setting for bricks
                if i+1 <= 2:
                    brick.fill_color = 'red'
                elif 2 < i+1 <= 4:
                    brick.fill_color = 'orange'
                elif 4 < i+1 <= 6:
                    brick.fill_color = 'yellow'
                elif 6 < i+1 <= 8:
                    brick.fill_color = 'green'
                elif 8 < i+1 <= 10:
                    brick.fill_color = 'blue'
                else:
                    brick.fill_color = 'purple'

                brick.x = (self.brick_w + self.brick_space) * j
                brick.y = self.brick_off + (self.brick_h + self.brick_space) * i
                self.window.add(brick)

        # other setting
        self.num_bricks = self.num_row * self.num_col
        self.bricks_bottom = self.brick_off + (self.brick_h + self.brick_space) * self.num_row
        self.lives_label = GLabel("X lives left!")
        self.lives_label.color = 'blue'
        self.lives_label.font = 'Verdana-40-bold-italic'

    def start_game(self, mouse):
        # Turn to_start to 'True' once the mouse is clicked, to test whether the game starts or not.
        self.to_start = True
        return self.to_start

    def paddle_move(self, mouse):
        # The midpoint of paddle follows while mouse moves.
        if self.window_w - self.paddle_w / 2 <= mouse.x:                         # paddle touches right wall
            self.paddle.x = self.window_w - self.paddle_w
        elif self.paddle_w / 2 < mouse.x < self.window_w - self.paddle_w / 2:  # paddle between two walls
            self.paddle.x = mouse.x - self.paddle_w / 2
        else:                                                                   # paddle touches left wall
            self.paddle.x = 0

    # Setter
    def set_ball_dx(self):
        # Randomly set a dx from 1 to MAX_X_SPEED.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    # Getter
    def get_ball_dx(self):
        return self.__dx

    # Getter
    def get_ball_dy(self):
        return self.__dy

    def detect_bump(self):
        # detect whether ball bumps into the bricks or the paddle or not
        r = self.ball_r
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.if_brick_remove(self.ball.x, self.ball.y)
            return True
        if self.window.get_object_at(self.ball.x, self.ball.y + 2 * r) is not None:
            self.if_brick_remove(self.ball.x, self.ball.y + 2 * r)
            return True
        if self.window.get_object_at(self.ball.x + 2 * r, self.ball.y) is not None:
            self.if_brick_remove(self.ball.x + 2 * r, self.ball.y)
            return True
        if self.window.get_object_at(self.ball.x + 2 * r, self.ball.y + 2 * r) is not None:
            self.if_brick_remove(self.ball.x + 2 * r, self.ball.y + 2 * r)
            return True

    def if_brick_remove(self, brick_x, brick_y):
        if brick_y <= self.bricks_bottom:
            brick_to_remove = self.window.get_object_at(brick_x, brick_y)
            self.window.remove(brick_to_remove)
            self.num_bricks -= 1
            print(self.num_bricks)

    def show_lives_left(self):
        self.lives_label.x = (self.window_w - self.lives_label.width) / 2
        self.lives_label.y = (self.window_h - self.lives_label.height) / 2
        self.window.add(self.lives_label)

    def reset_ball(self):
        self.ball.x = self.window_w / 2 - self.ball_r
        self.ball.y = self.window_h / 2 - self.ball_r
        self.to_start = False

    def game_over(self):
        self.window.clear()
        label = GLabel("Game over!")
        label.color = 'red'
        label.font = 'Verdana-40-bold-italic'
        self.window.add(label, (self.window_w - label.width)/2, (self.window_h - label.height)/2)

    def game_win(self):
        self.window.clear()
        label = GLabel("You win!")
        label.color = 'green'
        label.font = 'Verdana-40-bold-italic'
        self.window.add(label, (self.window_w - label.width) / 2, (self.window_h - label.height) / 2)
