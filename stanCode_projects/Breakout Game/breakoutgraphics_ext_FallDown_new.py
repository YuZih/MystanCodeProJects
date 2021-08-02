"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-------------------
Name: Yuzu
I have created 3 types of game. Have fun and enjoy it!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import math
import random
from playsound import playsound
import pygame

# Common Constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).

PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

BALL_RADIUS = 10  # Radius of the ball (in pixels).
BALL_RADIUS_NEW = 15  # New radius of the ball (in pixels).
INITIAL_Y_SPEED = 10  # Initial vertical speed for the ball.
MAX_X_SPEED = 10  # Maximum initial horizontal speed for the ball.

NUM_LIVES = 3  # Number of attempts
FRAME_RATE = 1000 / 120  # 120 frames per second

# global variable for classical game
classical_score = 0

# global variable for eight diagram game
eight_diagram_score = 0

# Special Constants for flower game
FLOWER_DENSE = 10  # Density of flowers. better: 30

# global variable for flower game
flower_score = 0


class BreakoutGraphics:

    def __init__(self, title='Breakout_ext'):
        # music part
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized

        # Create a graphical window
        self.window_w = 1280
        self.window_h = 720
        self.window = GWindow(width=self.window_w, height=self.window_h, title=title)

        # Default initial velocity for the ball
        self.__dx = self.set_ball_dx()
        self.__dy = INITIAL_Y_SPEED

        # common setting
        self.to_start = False
        self.lives_label = GLabel("X lives left!")
        self.lives_label.color = 'skyblue'
        self.lives_label.font = 'Verdana-70-bold-italic'
        self.counting_click = 0

        # enter opening animation
        self.opening_animation()

    """
    The following is for the opening animation.
    """
    # Opening animation pre-setting
    def opening_animation(self):
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.load('bgm_open_end.mp3')
        pygame.mixer.music.play(-1)

        background = GImage('opening_background_earth_horizon.jpg')
        self.window.add(background)

        game_name_shadow = GLabel('BREAKOUT WORLD')
        game_name_shadow.color = 'grey'
        game_name_shadow.font = 'Courier-' + '120' + '-bold'
        self.window.add(game_name_shadow, self.window.width / 2 - game_name_shadow.width / 2 + 8, 358)

        game_name = GLabel('BREAKOUT WORLD')
        game_name.color = 'white'
        game_name.font = 'Courier-' + '120' + '-bold'
        self.window.add(game_name, self.window.width / 2 - game_name.width / 2, 350)

        box = GRect(self.window.width / 2, self.window.height / 10)
        box.color = 'white'
        self.window.add(box, self.window.width / 2 - box.width / 2, self.window.height * 0.8 - box.height / 2)

        loading = GLabel('LOADING')
        loading.color = 'red'
        loading.font = 'Courier-' + '60' + '-bold-italic'
        self.window.add(loading, self.window.width / 2 - loading.width / 2, box.y)
        loading_brick = GLabel('Add concrete to make bricks')
        loading_brick.color = 'grey'
        loading_brick.font = 'Verdana-25'
        loading_paddle = GLabel('Create a flexible board')
        loading_paddle.color = 'grey'
        loading_paddle.font = 'Verdana-25'
        loading_ball = GLabel('Make a solid ball')
        loading_ball.color = 'grey'
        loading_ball.font = 'Verdana-25'
        planting_tree = GLabel('Plant the seeds of a cherry tree')
        planting_tree.color = 'grey'
        planting_tree.font = 'Verdana-25'
        give_water = GLabel('Water some cherry trees')
        give_water.color = 'grey'
        give_water.font = 'Verdana-25'
        wait_bloom = GLabel('Waiting for the cherry blossoms to bloom')
        wait_bloom.color = 'grey'
        wait_bloom.font = 'Verdana-25'
        draw_eight_diagram = GLabel('Draw an eight diagram')
        draw_eight_diagram.color = 'grey'
        draw_eight_diagram.font = 'Verdana-25'
        fail_to_draw = GLabel('Failed...recreate an eight diagram')
        fail_to_draw.color = 'grey'
        fail_to_draw.font = 'Verdana-25'
        induce_tai_chi = GLabel('Insert Tai Chi')
        induce_tai_chi.color = 'grey'
        induce_tai_chi.font = 'Verdana-25'
        fortune_seeing = GLabel('Predict scores of SC101 courses...Failed')
        fortune_seeing.color = 'grey'
        fortune_seeing.font = 'Verdana-25'
        prepare_start_game = GLabel('Ready to start game')
        prepare_start_game.color = 'grey'
        prepare_start_game.font = 'Verdana-25'

        # zoom out of game name
        for i in range(25):
            game_name.font = 'Courier-' + str(int(220 - i * 4)) + '-bold'
            game_name_shadow.font = 'Courier-' + str(int(220 - i * 4)) + '-bold'
            pause(25)

        # loading part
        for i in range(99):
            strip = GRect(box.width * 0.01 * i, self.window.height / 11)
            strip.filled = True
            strip.fill_color = 'grey'
            self.window.add(strip, box.x + box.width * 0.005, box.y + box.height / 2 - strip.height / 2)
            pause(random.randint(1, 250))
            if i == 1:
                self.window.add(loading_brick, self.window.width / 2 - loading_brick.width / 2,
                                box.y + box.height + loading_brick.height * 1.8)
            elif i == 9:
                self.window.remove(loading_brick)
                self.window.add(loading_paddle, self.window.width / 2 - loading_paddle.width / 2,
                                box.y + box.height + loading_paddle.height * 1.8)
            elif i == 18:
                self.window.remove(loading_paddle)
                self.window.add(loading_ball, self.window.width / 2 - loading_ball.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 27:
                self.window.remove(loading_ball)
                self.window.add(planting_tree, self.window.width / 2 - planting_tree.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 36:
                self.window.remove(planting_tree)
                self.window.add(give_water, self.window.width / 2 - give_water.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 45:
                self.window.remove(give_water)
                self.window.add(wait_bloom, self.window.width / 2 - wait_bloom.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 54:
                self.window.remove(wait_bloom)
                self.window.add(draw_eight_diagram, self.window.width / 2 - draw_eight_diagram.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 63:
                self.window.remove(draw_eight_diagram)
                self.window.add(fail_to_draw, self.window.width / 2 - fail_to_draw.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 72:
                self.window.remove(fail_to_draw)
                self.window.add(induce_tai_chi, self.window.width / 2 - induce_tai_chi.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 81:
                self.window.remove(induce_tai_chi)
                self.window.add(fortune_seeing, self.window.width / 2 - fortune_seeing.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)
            elif i == 90:
                self.window.remove(fortune_seeing)
                self.window.add(prepare_start_game, self.window.width / 2 - prepare_start_game.width / 2,
                                box.y + box.height + loading_ball.height * 1.8)

        # loading completed
        strip = GRect(box.width * 0.99, self.window.height / 11)
        strip.filled = True
        strip.fill_color = 'green'
        self.window.add(strip, box.x + box.width * 0.005, box.y + box.height / 2 - strip.height / 2)
        self.window.remove(loading)
        self.window.remove(prepare_start_game)
        self.start_game_button = GLabel('START GAME')
        self.start_game_button.color = 'white'
        self.start_game_button.font = 'Courier-' + '60' + '-bold-italic'
        self.window.add(self.start_game_button, self.window.width / 2 - self.start_game_button.width / 2, box.y)
        onmouseclicked(self.start_opening_background)
        for i in range(100):
            self.start_game_button.color = 'red'
            pause(40)
            self.start_game_button.color = 'magenta'
            pause(40)
            self.start_game_button.color = 'blue'
            pause(40)

    # Click to show the opening background
    def start_opening_background(self, event):
        if self.start_game_button.x < event.x < self.start_game_button.x + self.start_game_button.width \
                and self.start_game_button.y - self.start_game_button.height < event.y < self.start_game_button.y:
            self.window.clear()
            self.opening_background()
            playsound('click_mode_sound.mp3', block=False)

    # Opening background setting
    def opening_background(self):
        background = GImage('choosing_mode_background.png')
        self.window.add(background)

        self.label_mode2_shadow = GLabel('Japanese')
        self.label_mode2_shadow.color = 'black'
        self.label_mode2_shadow.font = 'Verdana-70-bold-italic'
        self.window.add(self.label_mode2_shadow, (self.window.width - self.label_mode2_shadow.width) / 2 + 5,
                        (self.window.height + self.label_mode2_shadow.height) / 2 + 5)

        self.label_mode2 = GLabel('Japanese')
        self.label_mode2.color = 'yellow'
        self.label_mode2.font = 'Verdana-70-bold-italic'
        self.window.add(self.label_mode2, (self.window.width - self.label_mode2.width) / 2,
                        (self.window.height + self.label_mode2.height) / 2)

        self.label_mode1_shadow = GLabel('Classical')
        self.label_mode1_shadow.color = 'black'
        self.label_mode1_shadow.font = 'Verdana-' + '70' + '-bold-italic'
        self.window.add(self.label_mode1_shadow, (self.window.width - self.label_mode1_shadow.width) / 2 + 5,
                        (self.window.height + self.label_mode1_shadow.height) / 2 - self.label_mode2.height * 2 + 5)

        self.label_mode1 = GLabel('Classical')
        self.label_mode1.color = 'red'
        self.label_mode1.font = 'Verdana-' + '70' + '-bold-italic'
        self.window.add(self.label_mode1, (self.window.width - self.label_mode1.width) / 2,
                        (self.window.height + self.label_mode1.height) / 2 - self.label_mode2.height * 2)

        self.label_mode3_shadow = GLabel('Chinese')
        self.label_mode3_shadow.color = 'black'
        self.label_mode3_shadow.font = 'Verdana-70-bold-italic'
        self.window.add(self.label_mode3_shadow, (self.window.width - self.label_mode3_shadow.width) / 2 + 5,
                        (self.window.height + self.label_mode3_shadow.height) / 2 + self.label_mode2.height * 2 + 5)

        self.label_mode3 = GLabel('Chinese')
        self.label_mode3.color = 'blue'
        self.label_mode3.font = 'Verdana-70-bold-italic'
        self.window.add(self.label_mode3, (self.window.width - self.label_mode3.width) / 2,
                        (self.window.height + self.label_mode3.height) / 2 + self.label_mode2.height * 2)

        # Exit button setting
        self.label_exit_shadow = GLabel('Exit')
        self.label_exit_shadow.color = 'black'
        self.label_exit_shadow.font = 'Verdana-35-bold-italic'
        self.window.add(self.label_exit_shadow, (self.window.width - self.label_exit_shadow.width) / 2 + 5,
                        (self.window.height + self.label_exit_shadow.height) / 2 + self.label_mode2.height * 4 + 5)
        self.label_exit = GLabel('Exit')
        self.label_exit.color = 'white'
        self.label_exit.font = 'Verdana-35-bold-italic'
        self.window.add(self.label_exit, (self.window.width - self.label_exit.width)/2,
                        (self.window.height + self.label_exit.height)/2 + self.label_mode2.height * 4)

        onmouseclicked(self.start_mode)

    # choose which mode to play
    def start_mode(self, event):
        if self.label_mode1.x < event.x < self.label_mode1.x + self.label_mode1.width \
                and self.label_mode1.y - self.label_mode1.height < event.y < self.label_mode1.y:
            playsound('click_mode_sound.mp3', block=False)
            self.window.clear()
            self.start_classical_mode()
        elif self.label_mode2.x < event.x < self.label_mode2.x + self.label_mode2.width \
                and self.label_mode2.y - self.label_mode2.height < event.y < self.label_mode2.y:
            playsound('click_mode_sound.mp3', block=False)
            self.window.clear()
            self.start_japanese_mode()
        elif self.label_mode3.x < event.x < self.label_mode3.x + self.label_mode3.width \
                and self.label_mode3.y - self.label_mode3.height < event.y < self.label_mode3.y:
            playsound('click_mode_sound.mp3', block=False)
            self.window.clear()
            self.start_chinese_mode()
        elif self.label_exit.x < event.x < self.label_exit.x + self.label_exit.width \
                and self.label_exit.y - self.label_exit.height < event.y < self.label_exit.y:
            playsound('click_mode_sound.mp3', block=False)
            self.window.close()

    """
    The following is methods that is common used.
    """
    # create a ball with default position
    def creating_ball(self):
        # Center a filled ball and place it at the middle of window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.x = self.window_w / 2 - BALL_RADIUS
        self.ball.y = self.window_h / 2 - BALL_RADIUS
        self.window.add(self.ball)

    # create a ball (new) with another default position
    def creating_ball_new(self):
        # Center a filled ball(new) and place it at the middle of window
        self.ball_new = GOval(BALL_RADIUS_NEW * 2, BALL_RADIUS_NEW * 2)
        self.ball_new.filled = True
        self.ball_new.x = self.window_w / 2 - BALL_RADIUS_NEW
        self.ball_new.y = self.window_h / 2 - BALL_RADIUS_NEW
        self.window.add(self.ball_new)

    # reset the position of ball with default position
    def reset_ball(self):
        self.ball.x = self.window.width / 2 - BALL_RADIUS
        self.ball.y = self.window.height / 2 - BALL_RADIUS
        self.to_start = False

    # reset the position of ball with another default position
    def reset_ball_new(self):
        self.ball_new.x = self.window.width / 2 - BALL_RADIUS_NEW
        self.ball_new.y = 600
        self.to_start = False

    # Click to start game
    def start_game(self, mouse):
        # Turn to_start to 'True' once the mouse is clicked, to test whether the game starts or not.
        self.to_start = True
        return self.to_start

    # Setter for dx setting
    def set_ball_dx(self):
        # Randomly set a dx from 5 to MAX_X_SPEED.
        self.__dx = random.randint(5, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    # Getter for dx getting
    def get_ball_dx(self):
        return self.__dx

    # Getter for dy getting
    def get_ball_dy(self):
        return self.__dy

    # Creating a paddle
    def creating_paddle(self):
        self.paddle = GRect(PADDLE_WIDTH * 3, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.x = (self.window_w - PADDLE_WIDTH) / 2
        self.paddle.y = self.window_h - (PADDLE_HEIGHT + PADDLE_OFFSET)
        self.window.add(self.paddle)

    # Control the movement of paddle
    def paddle_move(self, mouse):
        # The midpoint of paddle follows while mouse moves.
        if self.window.width - self.paddle.width / 2 < mouse.x:  # paddle touches right wall
            self.paddle.x = self.window.width - self.paddle.width
        elif self.paddle.width / 2 < mouse.x <= self.window.width - self.paddle.width / 2:  # paddle between two walls
            self.paddle.x = mouse.x - self.paddle.width / 2
        else:  # paddle touches left wall
            self.paddle.x = 0

    def show_lives_left(self):
        self.rect_for_lives = GRect(self.lives_label.width * 1.3, self.lives_label.height * 2)
        self.rect_for_lives.color = 'skyblue'
        self.rect_for_lives.filled = True
        self.rect_for_lives.fill_color = 'skyblue'
        self.rect_for_lives.x = (self.window.width - self.rect_for_lives.width) / 2
        self.rect_for_lives.y = (self.window.height - self.rect_for_lives.height) / 2
        self.window.add(self.rect_for_lives)

        self.rect_for_lives2 = GRect(self.lives_label.width * 1.2, self.lives_label.height * 1.5)
        self.rect_for_lives2.color = 'white'
        self.rect_for_lives2.filled = True
        self.rect_for_lives2.fill_color = 'white'
        self.rect_for_lives2.x = (self.window.width - self.rect_for_lives2.width) / 2
        self.rect_for_lives2.y = (self.window.height - self.rect_for_lives2.height) / 2
        self.window.add(self.rect_for_lives2)

        self.lives_label.x = (self.window.width - self.lives_label.width) / 2
        self.lives_label.y = (self.window.height + self.lives_label.height) / 2
        self.window.add(self.lives_label)

    def game_over(self):
        self.label_over = GLabel("GAME OVER")
        self.label_over.color = 'indianred'
        self.label_over.font = 'Verdana-70-bold-italic'
        self.rect1_over = GRect(self.label_over.width * 1.1, self.label_over.height * 1.5)
        self.rect1_over.color = 'white'
        self.rect1_over.filled = True
        self.rect1_over.fill_color = 'white'
        self.rect2_over = GRect(self.label_over.width * 1.2, self.label_over.height * 2)
        self.rect2_over.color = 'white'
        self.rect2_over.filled = True
        self.rect2_over.fill_color = 'indianred'
        self.window.add(self.rect2_over, (self.window.width - self.rect2_over.width) / 2,
                        (self.window.height - self.rect2_over.height) / 2)
        self.window.add(self.rect1_over, (self.window.width - self.rect1_over.width) / 2,
                        (self.window.height - self.rect1_over.height) / 2)
        self.window.add(self.label_over, (self.window.width - self.label_over.width) / 2,
                        (self.window.height + self.label_over.height) / 2)
        pause(FRAME_RATE)
        playsound('game_over_sound.mp3', block=False)

        # play-again setting
        self.play_again = GLabel('Play again!')
        self.play_again.color = 'green'
        self.play_again.font = 'Verdana-45-bold-italic'
        self.window.add(self.play_again, (self.window.width - self.play_again.width) / 2,
                        self.label_over.y + self.label_over.height * 1.5)

        # music
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.unload()
        pygame.mixer.music.load('bgm_open_end.mp3')
        pygame.mixer.music.play(-1)

        self.to_start = False
        global classical_score
        classical_score = 0
        global eight_diagram_score
        eight_diagram_score = 0
        global flower_score
        flower_score = 0
        onmouseclicked(self.return_to_opening_background)

    def game_win(self):
        self.label_win = GLabel("YOU WIN")
        self.label_win.color = 'sage'
        self.label_win.font = 'Verdana-70-bold-italic'
        self.rect1_win = GRect(self.label_win.width * 1.1, self.label_win.height * 1.5)
        self.rect1_win.color = 'white'
        self.rect1_win.filled = True
        self.rect1_win.fill_color = 'white'
        self.rect2_win = GRect(self.label_win.width * 1.2, self.label_win.height * 2)
        self.rect2_win.color = 'white'
        self.rect2_win.filled = True
        self.rect2_win.fill_color = 'lightsage'
        self.window.add(self.rect2_win, (self.window.width - self.rect2_win.width) / 2,
                        (self.window.height - self.rect2_win.height) / 2)
        self.window.add(self.rect1_win, (self.window.width - self.rect1_win.width) / 2,
                        (self.window.height - self.rect1_win.height) / 2)
        self.window.add(self.label_win, (self.window.width - self.label_win.width) / 2,
                        (self.window.height + self.label_win.height) / 2)
        pause(FRAME_RATE)
        playsound('game_win_sound.mp3', block=False)

        # play-again setting
        self.play_again = GLabel('Play again!')
        self.play_again.color = 'green'
        self.play_again.font = 'Verdana-35-bold-italic'
        self.window.add(self.play_again, (self.window.width - self.play_again.width) / 2,
                        self.label_win.y + self.label_win.height * 1.5)

        # music
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.load('bgm_open_end.mp3')
        pygame.mixer.music.play(-1)

        self.to_start = False
        global classical_score
        classical_score = 0
        global eight_diagram_score
        eight_diagram_score = 0
        global flower_score
        flower_score = 0

        onmouseclicked(self.return_to_opening_background)

    def return_to_opening_background(self, event):
        if self.play_again.x <= event.x <= self.play_again.x + self.play_again.width and \
                self.play_again.y - self.play_again.height <= event.y <= self.play_again.y:
            playsound('click_mode_sound.mp3', block=False)
            self.opening_background()

    def counting_click_times(self, event):
        self.counting_click += 1

    """"
    The following is for classical version breakout.
    """
    def start_classical_mode(self):
        # pre-setting for classical game
        self.bricks_bottom = BRICK_OFFSET + (BRICK_HEIGHT + BRICK_SPACING) * BRICK_ROWS
        self.star_list = []
        onmouseclicked(self.counting_click_times)
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.load('bgm_classical_mode.mp3')
        pygame.mixer.music.play(-1)

        classical_instruction = GImage('how_to_play_classical.png')
        self.window.add(classical_instruction)
        pause(FRAME_RATE * 600)
        self.window.remove(classical_instruction)

        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_game)
        lives = NUM_LIVES
        vy = self.get_ball_dy()
        vx = self.get_ball_dx()

        # background for classical game
        self.background_classical = GImage('background_classical.jpg')
        self.window.add(self.background_classical)

        # heart setting for classical game
        self.heart1_classical = GImage('heart_classical.png')
        self.heart2_classical = GImage('heart_classical.png')
        self.heart3_classical = GImage('heart_classical.png')
        self.window.add(self.heart1_classical, 330, 673)
        self.window.add(self.heart2_classical, 280, 673)
        self.window.add(self.heart3_classical, 230, 673)

        # paddle setting for classical game
        self.creating_paddle()
        self.paddle.fill_color = 'white'

        # ball setting for classical game
        self.creating_ball_new()
        self.ball_new.y = 600
        self.ball_new.fill_color = 'white'

        # Draw bricks for classical game
        self.num_brick_classical = 0
        for i in range(BRICK_ROWS):
            for j in range(int(self.window.width / (BRICK_WIDTH + BRICK_SPACING)) - 2):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True

                # color setting for bricks
                if i + 1 <= 2:
                    brick.fill_color = 'red'
                elif 2 < i + 1 <= 4:
                    brick.fill_color = 'orange'
                elif 4 < i + 1 <= 6:
                    brick.fill_color = 'yellow'
                elif 6 < i + 1 <= 8:
                    brick.fill_color = 'green'
                elif 8 < i + 1 <= 10:
                    brick.fill_color = 'blue'
                else:
                    brick.fill_color = 'purple'

                brick.x = (BRICK_WIDTH + BRICK_SPACING) * j + 50
                brick.y = BRICK_OFFSET + (BRICK_HEIGHT + BRICK_SPACING) * i
                self.window.add(brick)
                self.num_brick_classical += 1

        # score board setting
        global classical_score
        self.classical_score_board = GLabel('Score: ' + str(classical_score))
        self.classical_score_board.color = 'grey'
        self.classical_score_board.font = 'Verdana-35-bold-italic'
        self.window.add(self.classical_score_board, 10, 710)

        # ball moves
        while True:
            pause(FRAME_RATE)
            if lives > 0 and self.num_brick_classical > 0:

                # first-click to start game
                if self.to_start is True:
                    self.ball_new.move(vx, vy)

                    # stars randomly fall and then being removed
                    star_to_remove = []
                    for i in range(len(self.star_list)):
                        self.star_list[i].move(0, 5)
                        if (self.paddle.x < self.star_list[i].x < self.paddle.x + self.paddle.width) and \
                                (self.paddle.y < self.star_list[i].y + self.star_list[i].height):
                            star_to_remove.append(i)
                            classical_score += 10
                            self.window.remove(self.star_list[i])
                            playsound('breakout_sound.mp3', block=False)
                            self.classical_score_board.text = 'Score: ' + str(classical_score)
                        elif self.star_list[i].y > self.window.height:
                            star_to_remove.append(i)
                    for i in reversed(star_to_remove):
                        self.star_list.pop(i)

                    # rebound when ball bumps into bricks or the paddle
                    if self.detect_bump_classical() is True:

                        # when near bricks
                        if self.ball_new.y < self.window.height * 2 / 3:
                            vy = - vy  # change the vertical direction of ball

                        # when near paddle and distance from top of paddle to bottom of ball is less than dy
                        # let ball not run along the paddle
                        elif self.ball_new.y + self.ball_new.height - self.paddle.y < self.get_ball_dy():
                            vy = - vy  # change the vertical direction of ball
                            playsound('bounce_sound.mp3', block=False)

                    # when ball touches the left and right side of wall
                    if self.ball_new.x <= 0 or (self.ball_new.x + self.ball_new.width) > self.window.width:
                        vx += random.randint(-1, 1)     # randomly adjust the value of vx
                        vx = - vx  # change the horizontal direction of ball

                    # when ball touches the upper side of wall
                    if self.ball_new.y <= 0:
                        vy = - vy  # change the vertical direction of ball

                    # when ball falls down out of window
                    elif self.ball_new.y >= self.window.height:
                        lives -= 1
                        if lives > 0:
                            # remove heart
                            if lives == 2:
                                self.window.remove(self.heart1_classical)
                            elif lives == 1:
                                self.window.remove(self.heart2_classical)

                            # show how many lives left
                            pause(FRAME_RATE * 50)
                            self.lives_label.text = str(lives) + ' lives left!'
                            self.show_lives_left()

                            # add heart back
                            if lives == 2:
                                self.window.add(self.heart1_classical)
                            elif lives == 1:
                                self.window.add(self.heart2_classical)
                            pause(FRAME_RATE * 150)

                            # remove heart again
                            self.window.remove(self.lives_label)
                            self.window.remove(self.rect_for_lives)
                            self.window.remove(self.rect_for_lives2)
                            if lives == 2:
                                self.window.remove(self.heart1_classical)
                            elif lives == 1:
                                self.window.remove(self.heart2_classical)

                            pause(FRAME_RATE * 50)
                            self.reset_ball_new()
                            pause(FRAME_RATE * 100)
            else:
                break

        # when win
        if self.num_brick_classical == 0:
            self.window.remove(self.ball_new)
            pause(FRAME_RATE * 50)
            pygame.mixer.music.stop()
            self.game_win()
            self.num_brick_classical = 0
            self.label_win.color = 'white'
            self.rect1_win.color = 'darkgreen'
            self.rect1_win.fill_color = 'darkgreen'
            self.rect2_win.color = 'white'
            self.rect2_win.fill_color = 'white'

        # when lose
        elif lives == 0:
            self.window.remove(self.heart3_classical)
            self.window.remove(self.ball_new)
            pause(FRAME_RATE * 50)
            pygame.mixer.music.stop()
            self.game_over()
            self.num_brick_classical = 0
            self.label_over.color = 'white'
            self.rect1_over.color = 'darkred'
            self.rect1_over.fill_color = 'darkred'
            self.rect2_over.color = 'white'
            self.rect2_over.fill_color = 'white'

    # detecting bump for classical game
    def detect_bump_classical(self):
        # detect whether ball bumps into the bricks or the paddle or not
        r = BALL_RADIUS_NEW
        detected_1 = self.window.get_object_at(self.ball_new.x, self.ball_new.y)
        detected_2 = self.window.get_object_at(self.ball_new.x, self.ball_new.y + 2 * r)
        detected_3 = self.window.get_object_at(self.ball_new.x + 2 * r, self.ball_new.y)
        detected_4 = self.window.get_object_at(self.ball_new.x + 2 * r, self.ball_new.y + 2 * r)

        if detected_1 is not None:
            if detected_1 is not self.background_classical and detected_1 is not self.classical_score_board:
                if detected_1 is not self.heart1_classical:
                    if detected_1 is not self.heart2_classical:
                        if detected_1 is not self.heart3_classical:
                            if detected_1 not in self.star_list:
                                self.if_brick_remove(self.ball_new.x, self.ball_new.y)
                                return True
        if detected_2 is not None:
            if detected_2 is not self.background_classical and detected_2 is not self.classical_score_board:
                if detected_2 is not self.heart1_classical:
                    if detected_2 is not self.heart2_classical:
                        if detected_2 is not self.heart3_classical:
                            if detected_2 not in self.star_list:
                                self.if_brick_remove(self.ball_new.x, self.ball_new.y + 2 * r)
                                return True
        if detected_3 is not None:
            if detected_3 is not self.background_classical and detected_3 is not self.classical_score_board:
                if detected_3 is not self.heart1_classical:
                    if detected_3 is not self.heart2_classical:
                        if detected_3 is not self.heart3_classical:
                            if detected_3 not in self.star_list:
                                self.if_brick_remove(self.ball_new.x + 2 * r, self.ball_new.y)
                                return True
        if detected_4 is not None:
            if detected_4 is not self.background_classical and detected_4 is not self.classical_score_board:
                if detected_4 is not self.heart1_classical:
                    if detected_4 is not self.heart2_classical:
                        if detected_4 is not self.heart3_classical:
                            if detected_4 not in self.star_list:
                                self.if_brick_remove(self.ball_new.x + 2 * r, self.ball_new.y + 2 * r)
                                return True

    # If detected item is a brick, then remove it.
    def if_brick_remove(self, brick_x, brick_y):
        if brick_y <= BRICK_OFFSET + (BRICK_HEIGHT * BRICK_ROWS) + (BRICK_SPACING * (BRICK_ROWS - 1)):
            brick_to_remove = self.window.get_object_at(brick_x, brick_y)
            playsound('breakout_sound.mp3', block=False)

            # stars will randomly fall down
            if random.randint(0, 5) == 1:
                a = random.randint(0, 3)
                if a == 0:
                    self.star_list.append(GImage('Mars.png'))
                if a == 1:
                    self.star_list.append(GImage('Uranus.png'))
                if a == 2:
                    self.star_list.append(GImage('Saturn.png'))
                if a == 3:
                    self.star_list.append(GImage('Sun.png'))
                self.window.add(self.star_list[-1], brick_x, brick_y)

            self.window.remove(brick_to_remove)
            self.num_brick_classical -= 1
            global classical_score
            classical_score += 2  # total classical score is 560
            self.classical_score_board.text = 'Score: ' + str(classical_score)

    """
    The following is for eight_diagram version breakout.
    Some methods used below have already defined as above.
    """
    # control paddle movement only for eight-diagram game
    def paddle_move_eight_diagram(self, event):
        if self.to_start is True:
            x = event.x - self.window.width / 2
            y = event.y - self.window.height / 2
            if self.direction_of_paddle is not False:
                self.window.remove(self.paddle_eight_diagram[self.direction_of_paddle][0])
            if y < -abs(x):
                self.window.add(self.paddle_eight_diagram[0][0], self.paddle_eight_diagram[0][1],
                                self.paddle_eight_diagram[0][2])
                self.direction_of_paddle = 0
            elif y > abs(x):
                self.window.add(self.paddle_eight_diagram[1][0], self.paddle_eight_diagram[1][1],
                                self.paddle_eight_diagram[1][2])
                self.direction_of_paddle = 1
            elif x > abs(y):
                self.window.add(self.paddle_eight_diagram[2][0], self.paddle_eight_diagram[2][1],
                                self.paddle_eight_diagram[2][2])
                self.direction_of_paddle = 2
            elif x < -abs(y):
                self.window.add(self.paddle_eight_diagram[3][0], self.paddle_eight_diagram[3][1],
                                self.paddle_eight_diagram[3][2])
                self.direction_of_paddle = 3
        else:
            self.window.remove(self.paddle_eight_diagram[self.direction_of_paddle][0])
            self.direction_of_paddle = False

    # start to play eight-diagram game
    def start_chinese_mode(self):
        onmouseclicked(self.counting_click_times)


        onmouseclicked(self.start_game)

        # instruction
        eight_diagram_instruction = GImage('how_to_play_eight.png')
        self.window.add(eight_diagram_instruction)
        pause(FRAME_RATE * 600)
        self.window.remove(eight_diagram_instruction)

        # background music for chinese mode
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.load('bgm_chinese_mode.mp3')
        pygame.mixer.music.play(-1)
        self.num_bricks_chinese = 32
        lives = NUM_LIVES
        vy = 3
        vx = 2

        # creating 4 paddles for eight-diagram game
        self.direction_of_paddle = False
        self.paddle_eight_diagram = []
        self.paddle_n = []
        self.paddle_e = []
        self.paddle_s = []
        self.paddle_w = []
        self.paddle_n.append(GRect(180, 10))
        self.paddle_n[0].filled = True
        self.paddle_n[0].fill_color = 'black'
        self.paddle_e.append(GRect(10, 180))
        self.paddle_e[0].filled = True
        self.paddle_e[0].fill_color = 'black'
        self.paddle_s.append(GRect(180, 10))
        self.paddle_s[0].filled = True
        self.paddle_s[0].fill_color = 'black'
        self.paddle_w.append(GRect(10, 180))
        self.paddle_w[0].filled = True
        self.paddle_w[0].fill_color = 'black'
        self.paddle_n += [self.window.width / 2 - self.paddle_s[0].width / 2,
                          self.window.height / 2 - 50 - self.paddle_s[0].height]
        self.paddle_s += [self.window.width / 2 - self.paddle_s[0].width / 2, self.window.height / 2 + 50]
        self.paddle_e += [self.window.width / 2 + 50, self.window.height / 2 - self.paddle_w[0].height / 2]
        self.paddle_w += [self.window.width / 2 - self.paddle_w[0].width - 50,
                          self.window.height / 2 - self.paddle_w[0].height / 2]
        self.paddle_eight_diagram += [self.paddle_n, self.paddle_s, self.paddle_e, self.paddle_w]

        # creating background for eight-diagram game
        self.background_eight_diagram = GImage('background_eight_diagram.png')
        self.window.add(self.background_eight_diagram)

        # heart setting for eight-diagram game
        self.heart_chinese1 = GImage('heart_chinese.png')
        self.window.add(self.heart_chinese1, 1100, 60)
        self.heart_chinese2 = GImage('heart_chinese.png')
        self.window.add(self.heart_chinese2, 1150, 60)
        self.heart_chinese3 = GImage('heart_chinese.png')
        self.window.add(self.heart_chinese3, 1200, 60)

        # creating brick for eight-diagram game
        radius = self.window.height / 2.8
        for j in range(8):
            for i in range(4):
                brick = GPolygon()
                brick.add_vertex(((radius - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(
                    math.radians(-21 + j * 45)) + self.window.width / 2,
                                  (radius - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(
                                      math.radians(-21 + j * 45)) + self.window.height / 2))
                brick.add_vertex(((radius - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(
                    math.radians(21 + j * 45)) + self.window.width / 2,
                                  (radius - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(
                                      math.radians(21 + j * 45)) + self.window.height / 2))
                brick.add_vertex(((radius - BRICK_HEIGHT - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(
                    math.radians(21 + j * 45)) + self.window.width / 2,
                                  (radius - BRICK_HEIGHT - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(
                                      math.radians(21 + j * 45)) + self.window.height / 2))
                brick.add_vertex(((radius - BRICK_HEIGHT - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(
                    math.radians(-21 + j * 45)) + self.window.width / 2,
                                  (radius - BRICK_HEIGHT - i * (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(
                                      math.radians(-21 + j * 45)) + self.window.height / 2))
                brick.filled = True
                brick.fill_color = 'black'
                self.window.add(brick)

        # creating ball for eight-diagram game
        self.creating_ball()
        self.ball.move(random.randint(-100, 100), 100)

        # creating boundary for eight-diagram game
        self.eight_diagram_frame = GPolygon()
        for j in range(8):
            self.eight_diagram_frame.add_vertex(
                ((radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(math.radians(-22.5 + j * 45))
                 + self.window.width / 2,
                 (radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(math.radians(-22.5 + j * 45))
                 + self.window.height / 2))
        for j in range(8):
            self.eight_diagram_frame.add_vertex(
                (radius * math.cos(math.radians(-22.5 + j * 45)) + self.window.width / 2,
                 radius * math.sin(math.radians(-22.5 + j * 45)) + self.window.height / 2))
        self.eight_diagram_frame.filled = True
        self.eight_diagram_frame.color = 'gold'
        self.eight_diagram_frame.fill_color = 'gold'
        self.window.add(self.eight_diagram_frame)

        self.eight_diagram_frame1 = GPolygon()
        self.eight_diagram_frame1.add_vertex(
            ((radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(math.radians(-22.5 - 45)) + self.window.width / 2,
             (radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(
                 math.radians(-22.5 - 45)) + self.window.height / 2))
        self.eight_diagram_frame1.add_vertex(
            ((radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.cos(math.radians(-22.5)) + self.window.width / 2,
             (radius + (BRICK_HEIGHT + BRICK_SPACING)) * math.sin(math.radians(-22.5)) + self.window.height / 2))
        self.eight_diagram_frame1.add_vertex(
            (radius * math.cos(math.radians(-22.5)) + self.window.width / 2,
             radius * math.sin(math.radians(-22.5)) + self.window.height / 2))
        self.eight_diagram_frame1.add_vertex(
            (radius * math.cos(math.radians(-67.5)) + self.window.width / 2,
             radius * math.sin(math.radians(-67.5)) + self.window.height / 2))
        self.eight_diagram_frame1.filled = True
        self.eight_diagram_frame1.color = 'gold'
        self.eight_diagram_frame1.fill_color = 'gold'
        self.window.add(self.eight_diagram_frame1)

        # score board setting
        self.eight_diagram_score_board = GLabel('Score: ' + str(eight_diagram_score))
        self.eight_diagram_score_board.color = 'black'
        self.eight_diagram_score_board.font = 'Verdana-28-bold-italic'
        self.window.add(self.eight_diagram_score_board, 1100, 60)

        # ball moves
        while True:
            pause(FRAME_RATE)
            onmousemoved(self.paddle_move_eight_diagram)
            if lives > 0 and self.num_bricks_chinese > 0:

                # first-click to start game
                if self.to_start is True:
                    self.ball.move(vx, vy)

                    # rebound when ball bumps into bricks or the paddle, with specific directions
                    if self.detect_bump_eight_diagram() is not False:
                        (x, y) = self.detect_bump_eight_diagram()

                        # if brick, then remove
                        if self.window.get_object_at(x, y) is not self.eight_diagram_frame and \
                                self.window.get_object_at(x, y) is not self.eight_diagram_frame1:
                            self.if_brick_remove_eight_diagram(x, y)

                        # when near boundary, add some randomness
                        elif self.window.get_object_at(x, y) is self.eight_diagram_frame or \
                                self.window.get_object_at(x, y) is self.eight_diagram_frame1:
                            vx += random.randint(-1, 1)

                        # when near bricks
                        if (x - self.window.width / 2) ** 2 + (y - self.window.height / 2) ** 2 > 170 ** 2:
                            degree_a = math.asin(-(y - self.window.height / 2) / math.sqrt(
                                (x - self.window.width / 2) ** 2 + (y - self.window.height / 2) ** 2))
                            degree_b = math.acos((x - self.window.width / 2) / math.sqrt(
                                (x - self.window.width / 2) ** 2 + (
                                        y - self.window.height / 2) ** 2))
                            if math.pi * 3 / 8 < degree_b <= math.pi * 5 / 8:
                                vy = - vy
                            elif -math.pi * 1 / 8 <= degree_a <= math.pi * 1 / 8:
                                vx = -vx
                            elif (math.pi * 5 / 8 < degree_b <= math.pi * 7 / 8 and
                                  math.pi * 1 / 8 < degree_a <= math.pi * 3 / 8) or \
                                    (math.pi * 1 / 8 < degree_b <= math.pi * 3 / 8
                                     and -math.pi * 3 / 8 < degree_a <= -math.pi * 1 / 8):
                                a = vx
                                b = vy
                                vx = -b
                                vy = -a
                            elif (math.pi * 5 / 8 < degree_b <= math.pi * 7 / 8 and
                                  -math.pi * 3 / 8 < degree_a <= -math.pi * 1 / 8) or \
                                    (math.pi * 1 / 8 < degree_b <= math.pi * 3 / 8 and
                                     math.pi * 1 / 8 < degree_a <= math.pi * 3 / 8):
                                a = vx
                                b = vy
                                vx = b
                                vy = a

                        # when near paddle and distance from top of paddle to bottom of ball is less than dy
                        # let ball not run along the paddle
                        elif (self.ball.x + self.ball.width / 2 - self.window.width / 2) ** 2 + (
                                self.ball.y + self.ball.height / 2 - self.window.height / 2) ** 2 <= 193 ** 2:
                            if self.window.get_object_at(x, y) is self.paddle_eight_diagram[0][0] or \
                                    self.window.get_object_at(x, y) is self.paddle_eight_diagram[1][0]:
                                vy = - vy
                            elif self.window.get_object_at(x, y) is self.paddle_eight_diagram[2][
                                0] or self.window.get_object_at(x, y) is self.paddle_eight_diagram[3][0]:
                                vx = - vx

                    # when ball falls down out of window
                    elif (self.ball.x + self.ball.width / 2 - self.window.width / 2) ** 2 + (
                            self.ball.y + self.ball.height / 2 - self.window.height / 2) ** 2 < 60 ** 2:
                        lives -= 1
                        if lives > 0:
                            if lives == 2:
                                self.window.remove(self.heart_chinese1)
                            elif lives == 1:
                                self.window.remove(self.heart_chinese2)

                            pause(FRAME_RATE * 50)
                            self.lives_label.text = str(lives) + ' lives left!'
                            self.show_lives_left()
                            if lives == 2:
                                self.window.add(self.heart_chinese1)
                            elif lives == 1:
                                self.window.add(self.heart_chinese2)

                            pause(FRAME_RATE * 150)
                            self.window.remove(self.lives_label)
                            self.window.remove(self.rect_for_lives)
                            self.window.remove(self.rect_for_lives2)
                            if lives == 2:
                                self.window.remove(self.heart_chinese1)
                            elif lives == 1:
                                self.window.remove(self.heart_chinese2)

                            pause(FRAME_RATE * 50)
                            self.reset_ball()
                            self.ball.move(random.randint(-100, 100), 100)
                            pause(FRAME_RATE * 100)
            else:
                break

        # when win
        if self.num_bricks_chinese == 0:
            self.window.remove(self.ball)
            pause(FRAME_RATE * 50)
            pygame.mixer.music.stop()
            self.game_win()
            self.label_win.color = 'green'
            self.rect1_win.color = 'black'
            self.rect1_win.fill_color = 'black'
            self.rect2_win.color = 'green'
            self.rect2_win.fill_color = 'green'

        # when lose
        elif lives == 0:
            self.window.remove(self.ball)
            pause(FRAME_RATE * 50)
            pygame.mixer.music.stop()
            self.game_over()
            self.label_over.color = 'red'
            self.rect1_over.color = 'black'
            self.rect1_over.fill_color = 'black'
            self.rect2_over.color = 'red'
            self.rect2_over.fill_color = 'red'

    # detecting bump for eight-diagram game
    def detect_bump_eight_diagram(self):
        # detect whether ball bumps into the bricks or the paddle or not
        r = BALL_RADIUS
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None and \
                self.window.get_object_at(self.ball.x, self.ball.y) is not self.background_eight_diagram:
            return self.ball.x, self.ball.y
        elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * r) is not None and \
                self.window.get_object_at(self.ball.x, self.ball.y + 2 * r) is not self.background_eight_diagram:
            return self.ball.x, self.ball.y + 2 * r
        elif self.window.get_object_at(self.ball.x + 2 * r, self.ball.y) is not None and \
                self.window.get_object_at(self.ball.x + 2 * r, self.ball.y) is not self.background_eight_diagram:
            return self.ball.x + 2 * r, self.ball.y
        elif self.window.get_object_at(self.ball.x + 2 * r, self.ball.y + 2 * r) is not None and \
                self.window.get_object_at(self.ball.x + 2 * r,
                                          self.ball.y + 2 * r) is not self.background_eight_diagram:
            return self.ball.x + 2 * r, self.ball.y + 2 * r
        else:
            return False

    # if detected item is a brick, then remove it.
    def if_brick_remove_eight_diagram(self, x, y):
        if (x - self.window.width / 2) ** 2 + (y - self.window.height / 2) ** 2 > 130 ** 2:
            brick_to_remove = self.window.get_object_at(x, y)
            playsound('breakout_sound.mp3', block=False)
            self.window.remove(brick_to_remove)
            self.num_bricks_chinese -= 1
            global eight_diagram_score
            eight_diagram_score += 10  # total eight-diagram score is 320
            self.eight_diagram_score_board.text = 'Score: ' + str(eight_diagram_score)

    """"
    The following is for flower version breakout.
    """
    def start_japanese_mode(self):
        # pre-setting for flower game
        self.flower_dict = {}
        onmouseclicked(self.counting_click_times)
        pygame.init()
        pygame.mixer.init()
        pygame.time.delay(1000)  # wait 1 second to let mixer initialized
        pygame.mixer.music.load('bgm_Japanese_mode.mp3')
        pygame.mixer.music.play(-1)

        japanese_instruction = GImage('how_to_play_flower.png')
        self.window.add(japanese_instruction)
        pause(FRAME_RATE * 200)
        self.window.remove(japanese_instruction)

        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_game)
        lives = NUM_LIVES
        vy = self.get_ball_dy()
        vx = self.get_ball_dx()

        # flower background for flower game
        self.background_flower = GImage('flower_background.png')
        self.window.add(self.background_flower)

        # heart setting for flower game
        self.heart1 = GImage('flower_heart.png')
        self.heart2 = GImage('flower_heart.png')
        self.heart3 = GImage('flower_heart.png')
        self.window.add(self.heart1, 330, 673)
        self.window.add(self.heart2, 280, 673)
        self.window.add(self.heart3, 230, 673)

        # paddle setting for flower game
        self.creating_paddle()
        self.paddle.color = 'white'
        self.paddle.fill_color = 'lightcoral'

        # ball setting for flower game
        self.creating_ball_new()
        self.ball_new.color = 'white'
        self.ball_new.fill_color = 'lightcoral'
        self.ball_new.y = 600

        # Draw flowers
        self.num_flowers = 0
        for i in range(int(FLOWER_DENSE)):
            self.flower_adding(1, random.randint(250, 1000), random.randint(100, 300))
            self.flower_adding(1, random.randint(250, 1100), random.randint(100, 360))
            self.flower_adding(2, random.randint(200, 1100), random.randint(50, 360))
            self.flower_adding(2, random.randint(100, 1100), random.randint(50, 360))
            self.flower_adding(2, random.randint(100, 1100), random.randint(50, 360))
            self.num_flowers += 5

        # score board setting
        self.flower_score_board = GLabel('Score: ' + str(flower_score))
        self.flower_score_board.color = 'darksage'
        self.flower_score_board.font = 'Verdana-35-bold-italic'
        self.window.add(self.flower_score_board, 10, 710)

        while True:
            pause(FRAME_RATE)
            if lives > 0 and self.num_flowers > 0:

                # first-click to start game
                if self.to_start is True:
                    self.ball_new.move(vx, vy)

                    # flower falls down when hit by the ball
                    # It's suggested that comment this part if the game became too slow.
                    flower_exceed_window = {}
                    flower_exceed_count = 1
                    for flower, position in self.flower_dict.items():
                        # After original flower is removed , add a new flower to the window.
                        # The position of new flower is almost the same as the original one.
                        # And let the flower falls down while ball moves.
                        self.window.add(flower, position[0], position[1] + 5)
                        self.flower_dict[flower] = (self.flower_dict[flower][0], self.flower_dict[flower][1]+5)
                        if self.flower_dict[flower][1] > self.window_h:
                            flower_exceed_window[flower_exceed_count] = flower
                            flower_exceed_count += 1

                    # Other setting for the falling down of flowers.
                    # It's suggested that comment this part if the game became too slow.
                    for flower_exceed_count, flower_exceed in flower_exceed_window.items():
                        # Once the flower falls down outside of the window, it will be removed.
                        # This flower will also be deleted from lists.
                        # To let computer not loading too much.
                        self.window.remove(flower_exceed)
                        self.flower_dict.pop(flower_exceed)

                    # rebound when ball bumps into flowers or the paddle
                    if self.detect_bump_flower() is True:
                        # when near flowers
                        if self.ball_new.y < self.window.height * 2 / 3:
                            vy = - vy

                        # when near paddle and distance from top of paddle to bottom of ball is less than dy
                        # let ball not run along the paddle
                        elif self.ball_new.y + self.ball_new.height - self.paddle.y < self.get_ball_dy():
                            vy = - vy
                            playsound('bounce_sound.mp3', block=False)

                    # when ball touches the left and right side of wall
                    if self.ball_new.x <= 0 or (self.ball_new.x + self.ball_new.width) > self.window.width:
                        vx += random.randint(-1, 1)
                        vx = - vx

                    # when ball touches the upper side of wall
                    if self.ball_new.y <= 0:
                        vy = - vy

                    # when ball falls down out of window
                    elif self.ball_new.y >= self.window.height:
                        lives -= 1
                        if lives > 0:
                            # remove heart
                            if lives == 2:
                                self.window.remove(self.heart1)
                            elif lives == 1:
                                self.window.remove(self.heart2)

                            # show how many lives left
                            pause(FRAME_RATE * 50)
                            self.lives_label.text = str(lives) + ' lives left!'
                            self.show_lives_left()

                            # add heart back
                            if lives == 2:
                                self.window.add(self.heart1)
                            elif lives == 1:
                                self.window.add(self.heart2)
                            pause(FRAME_RATE * 150)

                            # remove heart again
                            self.window.remove(self.lives_label)
                            self.window.remove(self.rect_for_lives)
                            self.window.remove(self.rect_for_lives2)
                            if lives == 2:
                                self.window.remove(self.heart1)
                            elif lives == 1:
                                self.window.remove(self.heart2)

                            # reset ball
                            pause(FRAME_RATE * 50)
                            self.reset_ball_new()
                            pause(FRAME_RATE * 100)
            else:
                break

        # when win
        if self.num_flowers == 0:
            pause(FRAME_RATE * 50)
            self.window.remove(self.ball_new)
            self.num_flowers = 0
            pygame.mixer.music.stop()
            self.game_win()

        # when lose
        elif lives == 0:
            pause(FRAME_RATE * 50)
            self.window.remove(self.heart3)
            self.window.remove(self.ball_new)
            self.num_flowers = 0
            pygame.mixer.music.stop()
            self.game_over()

    # detecting bump for flower game
    def detect_bump_flower(self):
        # detect whether ball bumps into the flowers or the paddle or not
        r = BALL_RADIUS_NEW
        detected_1 = self.window.get_object_at(self.ball_new.x, self.ball_new.y)
        detected_2 = self.window.get_object_at(self.ball_new.x, self.ball_new.y + 2 * r)
        detected_3 = self.window.get_object_at(self.ball_new.x + 2 * r, self.ball_new.y)
        detected_4 = self.window.get_object_at(self.ball_new.x + 2 * r, self.ball_new.y + 2 * r)

        if detected_1 is not None:
            if detected_1 is not self.background_flower:
                if detected_1 is not self.heart1:
                    if detected_1 is not self.heart2:
                        if detected_1 is not self.heart3:
                            if detected_1 is not self.flower_score_board:
                                self.if_flower_remove(self.ball_new.x, self.ball_new.y)
                                return True
        if detected_2 is not None:
            if detected_2 is not self.background_flower:
                if detected_2 is not self.heart1:
                    if detected_2 is not self.heart2:
                        if detected_2 is not self.heart3:
                            if detected_2 is not self.flower_score_board:
                                self.if_flower_remove(self.ball_new.x, self.ball_new.y + 2 * r)
                                return True
        if detected_3 is not None:
            if detected_3 is not self.background_flower:
                if detected_3 is not self.heart1:
                    if detected_3 is not self.heart2:
                        if detected_3 is not self.heart3:
                            if detected_3 is not self.flower_score_board:
                                self.if_flower_remove(self.ball_new.x + 2 * r, self.ball_new.y)
                                return True
        if detected_4 is not None:
            if detected_4 is not self.background_flower:
                if detected_4 is not self.heart1:
                    if detected_4 is not self.heart2:
                        if detected_4 is not self.heart3:
                            if detected_4 is not self.flower_score_board:
                                self.if_flower_remove(self.ball_new.x + 2 * r, self.ball_new.y + 2 * r)
                                return True

    # if detected item is a flower, then remove it.
    def if_flower_remove(self, flower_x, flower_y):
        global flower_score
        if flower_y <= self.window_h * 2 / 3:
            flower_to_remove = self.window.get_object_at(flower_x, flower_y)

            # Make the first vertex of the hit flower as the initial fall-down position.
            # At this step, the method of 'flower.x' and 'flower.y' is not applicable.
            # Because the position of every flower is (0,0) in this case.
            # So the only solution here is making a vertex as the initial fall-down position.
            # It's suggested that comment this part if the game became too slow.
            fall_initial_x = flower_to_remove.vertices[0].x
            fall_initial_y = flower_to_remove.vertices[0].y

            # if ball bumps into the big flower (width of big flower is 45.3)
            if flower_to_remove.width > 45:
                flower_score += 5   # total flower score is 320

                # Other setting for the falling down of flowers.
                # It's suggested that comment this part if the game became too slow.
                flower_to_fall = self.flower_to_fall_making(1)
                # add a new flower that is outside of window as the reference point
                self.window.add(flower_to_fall)
                # replace the new flower to the initial fall-down position
                self.window.add(flower_to_fall, fall_initial_x, fall_initial_y)
                # Add the falling flower to the flower dictionary
                self.flower_dict[flower_to_fall] = (fall_initial_x, fall_initial_y)

            # if ball bumps into the small flower (width of small flower is 34.0)
            else:
                flower_score += 1   # total flower score is 320

                # # Other setting for the falling down of flowers.
                # # It's suggested that comment this part if the game became too slow.
                flower_to_fall = self.flower_to_fall_making(2)
                # add a new flower that is outside of window as the reference point
                self.window.add(flower_to_fall)
                # replace the new flower to the initial fall-down position
                self.window.add(flower_to_fall, fall_initial_x, fall_initial_y)
                # Add the falling flower to the flower dictionary
                self.flower_dict[flower_to_fall] = (fall_initial_x, fall_initial_y)

            self.flower_score_board.text = 'Score: ' + str(flower_score)
            playsound('breakout_sound.mp3', block=False)
            self.window.remove(flower_to_remove)
            self.num_flowers -= 1

    # Randomly set the position of flower. This step will adding a flower to the window.
    def flower_adding(self, flower_type, x, y):
        # Since I want the flower hit by the ball, I will specify the position of flower
        # at the step of adding vertices, rather than specify the position by adding to
        # the window. By this way, the function of "get_object_at" will able to detect
        # the object of flower.
        if flower_type == 1:
            big_flower = GPolygon()
            big_flower.add_vertex((46 / 1.5 + x, 34 / 1.5 + y))
            big_flower.add_vertex((39 / 1.5 + x, 26 / 1.5 + y))
            big_flower.add_vertex((32 / 1.5 + x, 23 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 23 / 1.5 + y))
            big_flower.add_vertex((21 / 1.5 + x, 24 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 30 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((26 / 1.5 + x, 43 / 1.5 + y))
            big_flower.add_vertex((34 / 1.5 + x, 46 / 1.5 + y))
            big_flower.add_vertex((29 / 1.5 + x, 48 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 52 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 59 / 1.5 + y))
            big_flower.add_vertex((21 / 1.5 + x, 67 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 70 / 1.5 + y))
            big_flower.add_vertex((31 / 1.5 + x, 71 / 1.5 + y))
            big_flower.add_vertex((39 / 1.5 + x, 65 / 1.5 + y))
            big_flower.add_vertex((46 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((50 / 1.5 + x, 66 / 1.5 + y))
            big_flower.add_vertex((53 / 1.5 + x, 73 / 1.5 + y))
            big_flower.add_vertex((64 / 1.5 + x, 79 / 1.5 + y))
            big_flower.add_vertex((67 / 1.5 + x, 78 / 1.5 + y))
            big_flower.add_vertex((70 / 1.5 + x, 77 / 1.5 + y))
            big_flower.add_vertex((72 / 1.5 + x, 72 / 1.5 + y))
            big_flower.add_vertex((70 / 1.5 + x, 63 / 1.5 + y))
            big_flower.add_vertex((63 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((69 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((77 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((82 / 1.5 + x, 54 / 1.5 + y))
            big_flower.add_vertex((87 / 1.5 + x, 45 / 1.5 + y))
            big_flower.add_vertex((84 / 1.5 + x, 41 / 1.5 + y))
            big_flower.add_vertex((80 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((77 / 1.5 + x, 36 / 1.5 + y))
            big_flower.add_vertex((71 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((62 / 1.5 + x, 38 / 1.5 + y))
            big_flower.add_vertex((65 / 1.5 + x, 30 / 1.5 + y))
            big_flower.add_vertex((67 / 1.5 + x, 25 / 1.5 + y))
            big_flower.add_vertex((66 / 1.5 + x, 19 / 1.5 + y))
            big_flower.add_vertex((60 / 1.5 + x, 11 / 1.5 + y))
            big_flower.add_vertex((54 / 1.5 + x, 12 / 1.5 + y))
            big_flower.add_vertex((50 / 1.5 + x, 13 / 1.5 + y))
            big_flower.add_vertex((47 / 1.5 + x, 18 / 1.5 + y))
            big_flower.color = 'white'
            big_flower.filled = True
            big_flower.fill_color = 'deeppink'
            self.window.add(big_flower)

        else:
            small_flower = GPolygon()
            small_flower.add_vertex((46 / 2 + x, 34 / 2 + y))
            small_flower.add_vertex((39 / 2 + x, 26 / 2 + y))
            small_flower.add_vertex((32 / 2 + x, 23 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 23 / 2 + y))
            small_flower.add_vertex((21 / 2 + x, 24 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 30 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((26 / 2 + x, 43 / 2 + y))
            small_flower.add_vertex((34 / 2 + x, 46 / 2 + y))
            small_flower.add_vertex((29 / 2 + x, 48 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 52 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 59 / 2 + y))
            small_flower.add_vertex((21 / 2 + x, 67 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 70 / 2 + y))
            small_flower.add_vertex((31 / 2 + x, 71 / 2 + y))
            small_flower.add_vertex((39 / 2 + x, 65 / 2 + y))
            small_flower.add_vertex((46 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((50 / 2 + x, 66 / 2 + y))
            small_flower.add_vertex((53 / 2 + x, 73 / 2 + y))
            small_flower.add_vertex((64 / 2 + x, 79 / 2 + y))
            small_flower.add_vertex((67 / 2 + x, 78 / 2 + y))
            small_flower.add_vertex((70 / 2 + x, 77 / 2 + y))
            small_flower.add_vertex((72 / 2 + x, 72 / 2 + y))
            small_flower.add_vertex((70 / 2 + x, 63 / 2 + y))
            small_flower.add_vertex((63 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((69 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((77 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((82 / 2 + x, 54 / 2 + y))
            small_flower.add_vertex((87 / 2 + x, 45 / 2 + y))
            small_flower.add_vertex((84 / 2 + x, 41 / 2 + y))
            small_flower.add_vertex((80 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((77 / 2 + x, 36 / 2 + y))
            small_flower.add_vertex((71 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((62 / 2 + x, 38 / 2 + y))
            small_flower.add_vertex((65 / 2 + x, 30 / 2 + y))
            small_flower.add_vertex((67 / 2 + x, 25 / 2 + y))
            small_flower.add_vertex((66 / 2 + x, 19 / 2 + y))
            small_flower.add_vertex((60 / 2 + x, 11 / 2 + y))
            small_flower.add_vertex((54 / 2 + x, 12 / 2 + y))
            small_flower.add_vertex((50 / 2 + x, 13 / 2 + y))
            small_flower.add_vertex((47 / 2 + x, 18 / 2 + y))
            small_flower.color = 'white'
            small_flower.filled = True
            small_flower.fill_color = 'lightpink'
            self.window.add(small_flower)

    # Making new flowers that is going to fall down.
    # Just return flower object, no need to add to the window at this step.
    def flower_to_fall_making(self, flower_type):
        x = 0

        # Since I don't want the new flower hit by the ball again while falling down,
        # I must set all vertices of the flower outside of the window.
        # The reason I do this is because that the function of "get_object_at" can only
        # detect the area of vertices that is set at the beginning, even though after
        # the flower is added to another position in the window.
        y = self.window_h * 1.5

        if flower_type == 1:
            big_flower = GPolygon()
            big_flower.add_vertex((46 / 1.5 + x, 34 / 1.5 + y))
            big_flower.add_vertex((39 / 1.5 + x, 26 / 1.5 + y))
            big_flower.add_vertex((32 / 1.5 + x, 23 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 23 / 1.5 + y))
            big_flower.add_vertex((21 / 1.5 + x, 24 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 30 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((26 / 1.5 + x, 43 / 1.5 + y))
            big_flower.add_vertex((34 / 1.5 + x, 46 / 1.5 + y))
            big_flower.add_vertex((29 / 1.5 + x, 48 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 52 / 1.5 + y))
            big_flower.add_vertex((19 / 1.5 + x, 59 / 1.5 + y))
            big_flower.add_vertex((21 / 1.5 + x, 67 / 1.5 + y))
            big_flower.add_vertex((25 / 1.5 + x, 70 / 1.5 + y))
            big_flower.add_vertex((31 / 1.5 + x, 71 / 1.5 + y))
            big_flower.add_vertex((39 / 1.5 + x, 65 / 1.5 + y))
            big_flower.add_vertex((46 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((50 / 1.5 + x, 66 / 1.5 + y))
            big_flower.add_vertex((53 / 1.5 + x, 73 / 1.5 + y))
            big_flower.add_vertex((64 / 1.5 + x, 79 / 1.5 + y))
            big_flower.add_vertex((67 / 1.5 + x, 78 / 1.5 + y))
            big_flower.add_vertex((70 / 1.5 + x, 77 / 1.5 + y))
            big_flower.add_vertex((72 / 1.5 + x, 72 / 1.5 + y))
            big_flower.add_vertex((70 / 1.5 + x, 63 / 1.5 + y))
            big_flower.add_vertex((63 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((69 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((77 / 1.5 + x, 57 / 1.5 + y))
            big_flower.add_vertex((82 / 1.5 + x, 54 / 1.5 + y))
            big_flower.add_vertex((87 / 1.5 + x, 45 / 1.5 + y))
            big_flower.add_vertex((84 / 1.5 + x, 41 / 1.5 + y))
            big_flower.add_vertex((80 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((77 / 1.5 + x, 36 / 1.5 + y))
            big_flower.add_vertex((71 / 1.5 + x, 37 / 1.5 + y))
            big_flower.add_vertex((62 / 1.5 + x, 38 / 1.5 + y))
            big_flower.add_vertex((65 / 1.5 + x, 30 / 1.5 + y))
            big_flower.add_vertex((67 / 1.5 + x, 25 / 1.5 + y))
            big_flower.add_vertex((66 / 1.5 + x, 19 / 1.5 + y))
            big_flower.add_vertex((60 / 1.5 + x, 11 / 1.5 + y))
            big_flower.add_vertex((54 / 1.5 + x, 12 / 1.5 + y))
            big_flower.add_vertex((50 / 1.5 + x, 13 / 1.5 + y))
            big_flower.add_vertex((47 / 1.5 + x, 18 / 1.5 + y))
            big_flower.color = 'white'
            big_flower.filled = True
            big_flower.fill_color = 'deeppink'
            return big_flower

        else:
            small_flower = GPolygon()
            small_flower.add_vertex((46 / 2 + x, 34 / 2 + y))
            small_flower.add_vertex((39 / 2 + x, 26 / 2 + y))
            small_flower.add_vertex((32 / 2 + x, 23 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 23 / 2 + y))
            small_flower.add_vertex((21 / 2 + x, 24 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 30 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((26 / 2 + x, 43 / 2 + y))
            small_flower.add_vertex((34 / 2 + x, 46 / 2 + y))
            small_flower.add_vertex((29 / 2 + x, 48 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 52 / 2 + y))
            small_flower.add_vertex((19 / 2 + x, 59 / 2 + y))
            small_flower.add_vertex((21 / 2 + x, 67 / 2 + y))
            small_flower.add_vertex((25 / 2 + x, 70 / 2 + y))
            small_flower.add_vertex((31 / 2 + x, 71 / 2 + y))
            small_flower.add_vertex((39 / 2 + x, 65 / 2 + y))
            small_flower.add_vertex((46 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((50 / 2 + x, 66 / 2 + y))
            small_flower.add_vertex((53 / 2 + x, 73 / 2 + y))
            small_flower.add_vertex((64 / 2 + x, 79 / 2 + y))
            small_flower.add_vertex((67 / 2 + x, 78 / 2 + y))
            small_flower.add_vertex((70 / 2 + x, 77 / 2 + y))
            small_flower.add_vertex((72 / 2 + x, 72 / 2 + y))
            small_flower.add_vertex((70 / 2 + x, 63 / 2 + y))
            small_flower.add_vertex((63 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((69 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((77 / 2 + x, 57 / 2 + y))
            small_flower.add_vertex((82 / 2 + x, 54 / 2 + y))
            small_flower.add_vertex((87 / 2 + x, 45 / 2 + y))
            small_flower.add_vertex((84 / 2 + x, 41 / 2 + y))
            small_flower.add_vertex((80 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((77 / 2 + x, 36 / 2 + y))
            small_flower.add_vertex((71 / 2 + x, 37 / 2 + y))
            small_flower.add_vertex((62 / 2 + x, 38 / 2 + y))
            small_flower.add_vertex((65 / 2 + x, 30 / 2 + y))
            small_flower.add_vertex((67 / 2 + x, 25 / 2 + y))
            small_flower.add_vertex((66 / 2 + x, 19 / 2 + y))
            small_flower.add_vertex((60 / 2 + x, 11 / 2 + y))
            small_flower.add_vertex((54 / 2 + x, 12 / 2 + y))
            small_flower.add_vertex((50 / 2 + x, 13 / 2 + y))
            small_flower.add_vertex((47 / 2 + x, 18 / 2 + y))
            small_flower.color = 'white'
            small_flower.filled = True
            small_flower.fill_color = 'lightpink'
            return small_flower
