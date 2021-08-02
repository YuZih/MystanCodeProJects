"""
File: my_drawing.py
Name: Yuzu
----------------------
TODO:
"""

from campy.graphics.gobjects import GRect, GPolygon, GLabel
from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from playsound import playsound
import random

# constant
WIDTH = 1280
HEIGHT = 720

# global variable
window = GWindow(WIDTH, HEIGHT, title='my_drawing')


def main():
    """
    My idea is from a animation called 'Odd Taxi.'
    At first, I was trying to make a picture.
    But at the end, I have made a animation instead. (lol)
    """
    i = 0
    dense = 50                                  # mean density of stars
    background_0()                              # mean background for the opening scene
    playsound('Odd_Taxi_OP.mp3', block=False)   # insert background music
    taxi = GImage('taxi.png')
    # Opening Part
    while i < 29:
        background_0()                          # insert background for opening
        gen_star(dense)                         # insert stars
        window.add(taxi, -200, 560)             # insert picture of taxi
        taxi.move(i*50, 0)                      # make taxi move
        if 4*i+40 < 100:
            show_text(4*i+40)                   # show text and continually zoom in
        else:
            show_text(100)                      # text is kept in font 100
        window.clear()                          # reset window
        i += 1
    # Dancing Part
    while True:
        movement_bottom()                       # show the 1st picture of dancing part
        pause(600)
        window.clear()
        movement_top()                          # show the 2nd picture of dancing part
        pause(600)
        window.clear()


def show_text(size):
    english1 = GLabel("TAXI")
    english1.font = 'Verdana-'+str(int(size*1.1))+'-bold-italic'
    english1.color = 'antiquewhite'
    japan = GLabel("オ ッ ド タ ク シ ー")
    japan.font = 'Verdana-' + str(int(size/3.4)) + '-bold-italic'
    japan.color = 'antiquewhite'
    english2 = GLabel("ODD")
    english2.font = 'Verdana-' + str(int(size*1.5)) + '-bold-italic'
    english2.color = 'antiquewhite'
    move = random.randrange(-5, 5)           # title 'Odd' will move up and down randomly
    for i in range(5):                       # do effect of zoom in by smoothly adjusting size and position of stars
        window.add(english2, WIDTH / 2 - english2.width, (HEIGHT + english1.height) / 2 + move + english2.height / 4)
        window.add(english1, WIDTH / 2, (HEIGHT + english1.height) / 2)
        window.add(japan, (WIDTH - japan.width + english1.width) / 2, HEIGHT/2 + english1.height - japan.height/2)
        pause(160)
        window.remove(english1)
        window.remove(japan)
        window.remove(english2)


def gen_star(dense):
    # generate stars randomly
    for i in range(int(WIDTH*HEIGHT/dense/dense)):
        star_type(random.randrange(1, 4), random.randrange(1, WIDTH), random.randrange(1, HEIGHT), random.randint(1, 3))


def star_type(size, x, y, color):
    # set up types of stars
    rect = GRect(size, size, x=x, y=y)
    rect.filled = 'True'
    if color == 1:
        color = "YELLOW"
    elif color == 2:
        color = "CADETBLUE"
    elif color == 3:
        color = "MAGENTA"
    rect.color = color
    rect.fill_color = color
    window.add(rect)


def background_0():
    # background for the opening scene
    rect = GRect(WIDTH, HEIGHT)
    rect.filled = 'True'
    rect.fill_color = 'darkslateblue'
    window.add(rect)


def movement_bottom():
    # background for the dance scene
    background = setup_background()
    window.add(background)
    # when hands are at the bottom position
    b_fox_right_ear1 = b_setup_f_r_ear1()
    b_fox_right_ear2 = b_setup_f_r_ear2()
    b_fox_right_ear3 = b_setup_f_r_ear3()
    b_fox_left_ear1 = b_setup_f_l_ear1()
    b_fox_left_ear2 = b_setup_f_l_ear2()
    b_fox_left_ear3 = b_setup_f_l_ear3()
    b_fox_face = b_setup_f_face()
    b_fox_coat = b_setup_f_coat()
    b_fox_neck = b_setup_f_neck()
    b_fox_right_eye = b_setup_f_r_eye()
    b_fox_left_eye = b_setup_f_l_eye()
    b_fox_nose = b_setup_f_nose()
    b_fox_cloth = b_setup_f_cloth()
    b_fox_right_hand = b_setup_f_r_hand()
    b_fox_left_hand = b_setup_f_l_hand()
    b_wolf_white_part = b_setup_w_white()
    b_wolf_red_part = b_setup_w_red()
    b_wolf_head = b_setup_w_head()
    b_wolf_right_hand = b_setup_w_r_hand()
    b_wolf_left_hand = b_setup_w_l_hand()
    b_wolf_nose = b_setup_w_nose()
    window.add(b_fox_right_ear1)
    window.add(b_fox_right_ear2)
    window.add(b_fox_right_ear3)
    window.add(b_fox_left_ear1)
    window.add(b_fox_left_ear2)
    window.add(b_fox_left_ear3)
    window.add(b_fox_face)
    window.add(b_fox_coat)
    window.add(b_fox_neck)
    window.add(b_fox_right_eye)
    window.add(b_fox_left_eye)
    window.add(b_fox_nose)
    window.add(b_fox_cloth)
    window.add(b_fox_right_hand)
    window.add(b_fox_left_hand)
    window.add(b_wolf_white_part)
    window.add(b_wolf_red_part)
    window.add(b_wolf_head)
    window.add(b_wolf_right_hand)
    window.add(b_wolf_left_hand)
    window.add(b_wolf_nose)


def movement_top():
    # background for the dance scene
    background = setup_background()
    window.add(background)
    # when hands are at the top position
    t_fox_right_ear1 = t_setup_f_r_ear1()
    t_fox_right_ear2 = t_setup_f_r_ear2()
    t_fox_right_ear3 = t_setup_f_r_ear3()
    t_fox_left_ear1 = t_setup_f_l_ear1()
    t_fox_left_ear2 = t_setup_f_l_ear2()
    t_fox_left_ear3 = t_setup_f_l_ear3()
    t_fox_face = t_setup_f_face()
    t_fox_coat = t_setup_f_coat()
    t_fox_neck = t_setup_f_neck()
    t_fox_right_eye = t_setup_f_r_eye()
    t_fox_left_eye = t_setup_f_l_eye()
    t_fox_nose = t_setup_f_nose()
    t_fox_cloth = t_setup_f_cloth()
    t_fox_right_hand = t_setup_f_r_hand()
    t_fox_left_hand = t_setup_f_l_hand()
    t_wolf_white_part = t_setup_w_white()
    t_wolf_red_part1 = t_setup_w_red1()
    t_wolf_red_part2 = t_setup_w_red2()
    t_wolf_head = t_setup_w_head()
    t_wolf_right_hand = t_setup_w_r_hand()
    t_wolf_left_hand = t_setup_w_l_hand()
    t_wolf_nose = t_setup_w_nose()
    window.add(t_fox_right_ear1)
    window.add(t_fox_right_ear2)
    window.add(t_fox_right_ear3)
    window.add(t_fox_left_ear1)
    window.add(t_fox_left_ear2)
    window.add(t_fox_left_ear3)
    window.add(t_fox_face)
    window.add(t_fox_coat)
    window.add(t_fox_neck)
    window.add(t_fox_right_eye)
    window.add(t_fox_left_eye)
    window.add(t_fox_nose)
    window.add(t_fox_cloth)
    window.add(t_fox_right_hand)
    window.add(t_fox_left_hand)
    window.add(t_wolf_white_part)
    window.add(t_wolf_red_part1)
    window.add(t_wolf_red_part2)
    window.add(t_wolf_head)
    window.add(t_wolf_right_hand)
    window.add(t_wolf_left_hand)
    window.add(t_wolf_nose)


def setup_background():
    rect_bg = GRect(1280, 720)
    rect_bg.color = 'rosybrown'
    rect_bg.filled = True
    rect_bg.fill_color = 'rosybrown'
    return rect_bg


def b_setup_f_r_ear1():
    triangle = GPolygon()
    triangle.add_vertex((379, 154))  # far-left
    triangle.add_vertex((386, 126))
    triangle.add_vertex((398, 84))
    triangle.add_vertex((402, 77))  # near top at left side
    triangle.add_vertex((404, 76))  # top
    triangle.add_vertex((410, 80))  # near top at right side
    triangle.add_vertex((412, 84))
    triangle.add_vertex((426, 108))
    triangle.add_vertex((442, 138))  # far-right
    triangle.filled = True
    return triangle


def b_setup_f_r_ear2():
    triangle = GPolygon()
    triangle.add_vertex((391, 151))  # far-left
    triangle.add_vertex((398, 129))
    triangle.add_vertex((402, 113))
    triangle.add_vertex((406, 100))  # near top at left side
    triangle.add_vertex((408, 95))  # top
    triangle.add_vertex((410, 98))  # near top at right side
    triangle.add_vertex((415, 108))
    triangle.add_vertex((420, 123))
    triangle.add_vertex((429, 142))  # far-right
    triangle.color = 'darkgrey'
    triangle.filled = True
    triangle.fill_color = 'darkgrey'
    return triangle


def b_setup_f_r_ear3():
    triangle = GPolygon()
    triangle.add_vertex((411, 147))  # far-left
    triangle.add_vertex((411.25, 135))
    triangle.add_vertex((411.5, 129))
    triangle.add_vertex((411.75, 124))  # near top at left side
    triangle.add_vertex((412, 122))  # top
    triangle.add_vertex((414, 123))  # near top at right side
    triangle.add_vertex((416, 125))
    triangle.add_vertex((422, 133))
    triangle.add_vertex((429, 142))  # far-right
    triangle.filled = True
    return triangle


def b_setup_f_l_ear1():
    triangle = GPolygon()
    triangle.add_vertex((444, 140))  # far-left
    triangle.add_vertex((456, 118))
    triangle.add_vertex((468, 102))
    triangle.add_vertex((485, 78))  # near top at left side
    triangle.add_vertex((491, 77))  # top
    triangle.add_vertex((493, 81))  # near top at right side
    triangle.add_vertex((496, 95))
    triangle.add_vertex((495, 120))
    triangle.add_vertex((494, 155))  # far-right
    triangle.filled = True
    return triangle


def b_setup_f_l_ear2():
    triangle = GPolygon()
    triangle.add_vertex((454, 142))  # far-left
    triangle.add_vertex((466, 125))
    triangle.add_vertex((473, 116))
    triangle.add_vertex((481, 102))  # near top at left side
    triangle.add_vertex((485, 101))  # top
    triangle.add_vertex((487, 104))  # near top at right side
    triangle.add_vertex((488, 121))
    triangle.add_vertex((489, 136))
    triangle.add_vertex((489, 152))  # far-right
    triangle.color = 'darkgrey'
    triangle.filled = True
    triangle.fill_color = 'darkgrey'
    return triangle


def b_setup_f_l_ear3():
    triangle = GPolygon()
    triangle.add_vertex((454, 142))  # far-left
    triangle.add_vertex((464, 133))
    triangle.add_vertex((467, 130))
    triangle.add_vertex((470, 125))  # near top at left side
    triangle.add_vertex((474, 125))  # top
    triangle.add_vertex((475, 129))  # near top at right side
    triangle.add_vertex((476, 134))
    triangle.add_vertex((477, 141))
    triangle.add_vertex((472, 148))  # far-right
    triangle.filled = True
    return triangle


def b_setup_f_face():
    f_face = GPolygon()
    f_face.add_vertex((379, 155))
    f_face.add_vertex((444, 138))
    f_face.add_vertex((499, 156))
    f_face.add_vertex((507, 222))
    f_face.add_vertex((364, 220))
    f_face.color = 'khaki'
    f_face.filled = True
    f_face.fill_color = 'khaki'
    return f_face


def b_setup_f_coat():
    f_coat = GPolygon()
    f_coat.add_vertex((251, 351))
    f_coat.add_vertex((259, 346))
    f_coat.add_vertex((290, 338))
    f_coat.add_vertex((312, 332))
    f_coat.add_vertex((328, 328))
    f_coat.add_vertex((346, 324))
    f_coat.add_vertex((357, 318))
    f_coat.add_vertex((360, 315))
    f_coat.add_vertex((427, 308))
    f_coat.add_vertex((486, 316))
    f_coat.add_vertex((497, 316))
    f_coat.add_vertex((503, 319))
    f_coat.add_vertex((510, 323))
    f_coat.add_vertex((527, 332))
    f_coat.add_vertex((552, 339))
    f_coat.add_vertex((566, 345))
    f_coat.add_vertex((576, 350))
    f_coat.add_vertex((581, 354))
    f_coat.add_vertex((583, 359))
    f_coat.add_vertex((609, 422))
    f_coat.add_vertex((639, 498))
    f_coat.add_vertex((646, 530))
    f_coat.add_vertex((648, 587))
    f_coat.add_vertex((646, 603))
    f_coat.add_vertex((641, 611))
    f_coat.add_vertex((639, 614))
    f_coat.add_vertex((625, 632))
    f_coat.add_vertex((609, 635))
    f_coat.add_vertex((603, 634))
    f_coat.add_vertex((592, 627))
    f_coat.add_vertex((591, 637))
    f_coat.add_vertex((589, 661))
    f_coat.add_vertex((588, 699))
    f_coat.add_vertex((587, 720))
    f_coat.add_vertex((450, 720))
    f_coat.add_vertex((400, 720))
    f_coat.add_vertex((380, 720))
    f_coat.add_vertex((377, 720))
    f_coat.add_vertex((249, 720))
    f_coat.add_vertex((251, 685))
    f_coat.add_vertex((252, 676))
    f_coat.add_vertex((247, 673))
    f_coat.add_vertex((239, 667))
    f_coat.add_vertex((232, 664))
    f_coat.add_vertex((223, 658))
    f_coat.add_vertex((209, 636))
    f_coat.add_vertex((210, 639))
    f_coat.add_vertex((209, 628))
    f_coat.add_vertex((212, 593))
    f_coat.add_vertex((221, 526))
    f_coat.add_vertex((228, 483))
    f_coat.add_vertex((234, 442))
    f_coat.add_vertex((244, 394))
    f_coat.add_vertex((245, 371))
    f_coat.add_vertex((248, 357))
    f_coat.color = 'darkgrey'
    f_coat.filled = True
    f_coat.fill_color = 'darkgrey'
    return f_coat


def b_setup_f_neck():
    f_neck = GPolygon()
    f_neck.add_vertex((364, 220))
    f_neck.add_vertex((379, 205))
    f_neck.add_vertex((404, 210))
    f_neck.add_vertex((438, 190))
    f_neck.add_vertex((469, 193))
    f_neck.add_vertex((492, 214))
    f_neck.add_vertex((505, 206))
    f_neck.add_vertex((510, 238))
    f_neck.add_vertex((493, 261))
    f_neck.add_vertex((499, 316))
    f_neck.add_vertex((500, 338))
    f_neck.add_vertex((487, 385))
    f_neck.add_vertex((442, 416))
    f_neck.add_vertex((387, 399))
    f_neck.add_vertex((364, 379))
    f_neck.add_vertex((357, 324))
    f_neck.add_vertex((360, 308))
    f_neck.add_vertex((365, 289))
    f_neck.add_vertex((369, 270))
    f_neck.color = 'lightgoldenrodyellow'
    f_neck.filled = True
    f_neck.fill_color = 'lightgoldenrodyellow'
    return f_neck


def b_setup_f_r_eye():
    f_r_eye = GPolygon()
    f_r_eye.add_vertex((394, 184))
    f_r_eye.add_vertex((396, 183))
    f_r_eye.add_vertex((409, 182))
    f_r_eye.add_vertex((427, 188))
    f_r_eye.add_vertex((428, 189))
    f_r_eye.add_vertex((414, 199))
    f_r_eye.add_vertex((405, 196))
    f_r_eye.add_vertex((399, 191))
    f_r_eye.add_vertex((395, 187))
    f_r_eye.color = 'ghostwhite'
    f_r_eye.filled = True
    f_r_eye.fill_color = 'ghostwhite'
    return f_r_eye


def b_setup_f_l_eye():
    f_l_eye = GPolygon()
    f_l_eye.add_vertex((477, 196))
    f_l_eye.add_vertex((479, 193))
    f_l_eye.add_vertex((488, 191))
    f_l_eye.add_vertex((497, 190))
    f_l_eye.add_vertex((496, 196))
    f_l_eye.add_vertex((492, 203))
    f_l_eye.add_vertex((485, 202))
    f_l_eye.add_vertex((481, 200))
    f_l_eye.color = 'ghostwhite'
    f_l_eye.filled = True
    f_l_eye.fill_color = 'ghostwhite'
    return f_l_eye


def b_setup_f_nose():
    f_nose = GPolygon()
    f_nose.add_vertex((439, 213))
    f_nose.add_vertex((442, 211))
    f_nose.add_vertex((454, 210))
    f_nose.add_vertex((458, 209))
    f_nose.add_vertex((467, 210))
    f_nose.add_vertex((466, 211))
    f_nose.add_vertex((465, 219))
    f_nose.add_vertex((463, 221))
    f_nose.add_vertex((456, 226))
    f_nose.add_vertex((449, 223))
    f_nose.add_vertex((443, 220))
    f_nose.add_vertex((440, 216))
    f_nose.filled = True
    return f_nose


def b_setup_f_cloth():
    f_cloth = GPolygon()
    f_cloth.add_vertex((356, 326))
    f_cloth.add_vertex((360, 327))
    f_cloth.add_vertex((376, 345))
    f_cloth.add_vertex((442, 401))
    f_cloth.add_vertex((472, 366))
    f_cloth.add_vertex((499, 325))
    f_cloth.add_vertex((499, 316))
    f_cloth.add_vertex((502, 319))
    f_cloth.add_vertex((503, 328))
    f_cloth.add_vertex((504, 345))
    f_cloth.add_vertex((504, 451))
    f_cloth.add_vertex((503, 566))
    f_cloth.add_vertex((499, 629))
    f_cloth.add_vertex((488, 701))
    f_cloth.add_vertex((486, 718))
    f_cloth.add_vertex((476, 720))
    f_cloth.add_vertex((427, 720))
    f_cloth.add_vertex((397, 720))
    f_cloth.add_vertex((380, 718))
    f_cloth.add_vertex((378, 706))
    f_cloth.add_vertex((376, 663))
    f_cloth.add_vertex((367, 550))
    f_cloth.add_vertex((362, 474))
    f_cloth.add_vertex((360, 426))
    f_cloth.add_vertex((358, 353))
    f_cloth.add_vertex((357, 334))
    f_cloth.color = 'peru'
    f_cloth.filled = True
    f_cloth.fill_color = 'peru'
    return f_cloth


def b_setup_f_r_hand():
    f_r_hand = GPolygon()
    f_r_hand.add_vertex((337, 579))
    f_r_hand.add_vertex((355, 565))
    f_r_hand.add_vertex((360, 564))
    f_r_hand.add_vertex((373, 561))
    f_r_hand.add_vertex((389, 560))
    f_r_hand.add_vertex((403, 566))
    f_r_hand.add_vertex((428, 590))
    f_r_hand.add_vertex((431, 599))
    f_r_hand.add_vertex((429, 610))
    f_r_hand.add_vertex((425, 620))
    f_r_hand.add_vertex((417, 632))
    f_r_hand.add_vertex((406, 643))
    f_r_hand.add_vertex((395, 656))
    f_r_hand.add_vertex((392, 657))
    f_r_hand.add_vertex((380, 660))
    f_r_hand.add_vertex((377, 662))
    f_r_hand.add_vertex((374, 665))
    f_r_hand.add_vertex((361, 667))
    f_r_hand.add_vertex((352, 662))
    f_r_hand.add_vertex((344, 654))
    f_r_hand.add_vertex((331, 638))
    f_r_hand.add_vertex((330, 630))
    f_r_hand.add_vertex((328, 611))
    f_r_hand.add_vertex((332, 586))
    f_r_hand.add_vertex((334, 583))
    f_r_hand.add_vertex((340, 580))
    f_r_hand.color = 'khaki'
    f_r_hand.filled = True
    f_r_hand.fill_color = 'khaki'
    return f_r_hand


def b_setup_f_l_hand():
    f_l_hand = GPolygon()
    f_l_hand.add_vertex((509, 543))
    f_l_hand.add_vertex((512, 526))
    f_l_hand.add_vertex((516, 517))
    f_l_hand.add_vertex((519, 511))
    f_l_hand.add_vertex((526, 508))
    f_l_hand.add_vertex((532, 505))
    f_l_hand.add_vertex((537, 503))
    f_l_hand.add_vertex((549, 497))
    f_l_hand.add_vertex((555, 495))
    f_l_hand.add_vertex((565, 494))
    f_l_hand.add_vertex((568, 494))
    f_l_hand.add_vertex((573, 496))
    f_l_hand.add_vertex((580, 501))
    f_l_hand.add_vertex((584, 503))
    f_l_hand.add_vertex((581, 502))
    f_l_hand.add_vertex((593, 514))
    f_l_hand.add_vertex((596, 517))
    f_l_hand.add_vertex((595, 517))
    f_l_hand.add_vertex((604, 526))
    f_l_hand.add_vertex((613, 539))
    f_l_hand.add_vertex((612, 544))
    f_l_hand.add_vertex((612, 555))
    f_l_hand.add_vertex((608, 563))
    f_l_hand.add_vertex((603, 571))
    f_l_hand.add_vertex((593, 585))
    f_l_hand.add_vertex((589, 587))
    f_l_hand.add_vertex((581, 587))
    f_l_hand.add_vertex((571, 585))
    f_l_hand.add_vertex((568, 589))
    f_l_hand.add_vertex((562, 589))
    f_l_hand.add_vertex((559, 590))
    f_l_hand.add_vertex((556, 589))
    f_l_hand.add_vertex((554, 589))
    f_l_hand.add_vertex((549, 583))
    f_l_hand.add_vertex((541, 585))
    f_l_hand.add_vertex((535, 582))
    f_l_hand.add_vertex((528, 579))
    f_l_hand.add_vertex((524, 568))
    f_l_hand.add_vertex((525, 559))
    f_l_hand.add_vertex((519, 555))
    f_l_hand.add_vertex((515, 550))
    f_l_hand.color = 'khaki'
    f_l_hand.filled = True
    f_l_hand.fill_color = 'khaki'
    return f_l_hand


def t_setup_f_r_ear1():
    triangle = GPolygon()
    triangle.add_vertex((408, 130))  # far-left
    triangle.add_vertex((414, 110))
    triangle.add_vertex((426, 71))
    triangle.add_vertex((436, 52))  # near top at left side
    triangle.add_vertex((439, 51))  # top
    triangle.add_vertex((443, 53))  # near top at right side
    triangle.add_vertex((452, 72))
    triangle.add_vertex((462, 95))
    triangle.add_vertex((473, 121))  # far-right
    triangle.filled = True
    return triangle


def t_setup_f_r_ear2():
    triangle = GPolygon()
    triangle.add_vertex((419, 129))  # far-left
    triangle.add_vertex((426, 109))
    triangle.add_vertex((432, 93))
    triangle.add_vertex((438, 75))  # near top at left side
    triangle.add_vertex((440, 72))  # top
    triangle.add_vertex((443, 75))  # near top at right side
    triangle.add_vertex((451, 91))
    triangle.add_vertex((456, 103))
    triangle.add_vertex((465, 122))  # far-right
    triangle.color = 'darkgrey'
    triangle.filled = True
    triangle.fill_color = 'darkgrey'
    return triangle


def t_setup_f_r_ear3():
    triangle = GPolygon()
    triangle.add_vertex((441, 126))  # far-left
    triangle.add_vertex((443, 118))
    triangle.add_vertex((444, 108))
    triangle.add_vertex((446, 103))  # near top at left side
    triangle.add_vertex((447, 100))  # top
    triangle.add_vertex((451, 102))  # near top at right side
    triangle.add_vertex((456, 108))
    triangle.add_vertex((461, 113))
    triangle.add_vertex((465, 122))  # far-right
    triangle.filled = True
    return triangle


def t_setup_f_l_ear1():
    triangle = GPolygon()
    triangle.add_vertex((473, 121))  # far-left
    triangle.add_vertex((485, 101))
    triangle.add_vertex((506, 73))
    triangle.add_vertex((521, 56))  # near top at left side
    triangle.add_vertex((526, 55))  # top
    triangle.add_vertex((528, 59))  # near top at right side
    triangle.add_vertex((528, 74))
    triangle.add_vertex((527, 104))
    triangle.add_vertex((526, 137))  # far-right
    triangle.filled = True
    return triangle


def t_setup_f_l_ear2():
    triangle = GPolygon()
    triangle.add_vertex((484, 125))  # far-left
    triangle.add_vertex((494, 111))
    triangle.add_vertex((508, 90))
    triangle.add_vertex((515, 80))  # near top at left side
    triangle.add_vertex((519, 73))  # top
    triangle.add_vertex((519, 81))  # near top at right side
    triangle.add_vertex((519, 94))
    triangle.add_vertex((519, 118))
    triangle.add_vertex((516, 134))  # far-right
    triangle.color = 'darkgrey'
    triangle.filled = True
    triangle.fill_color = 'darkgrey'
    return triangle


def t_setup_f_l_ear3():
    triangle = GPolygon()
    triangle.add_vertex((484, 125))  # far-left
    triangle.add_vertex((494, 111))
    triangle.add_vertex((497, 107))
    triangle.add_vertex((499, 105))  # near top at left side
    triangle.add_vertex((503, 104))  # top
    triangle.add_vertex((504, 109))  # near top at right side
    triangle.add_vertex((504, 114))
    triangle.add_vertex((504, 119))
    triangle.add_vertex((500, 131))  # far-right
    triangle.filled = True
    return triangle


def t_setup_f_face():
    f_face = GPolygon()
    f_face.add_vertex((408, 130))
    f_face.add_vertex((473, 121))
    f_face.add_vertex((529, 139))
    f_face.add_vertex((536, 223))
    f_face.add_vertex((388, 190))
    f_face.color = 'khaki'
    f_face.filled = True
    f_face.fill_color = 'khaki'
    return f_face


def t_setup_f_coat():
    f_coat = GPolygon()
    f_coat.add_vertex((296, 244))
    f_coat.add_vertex((314, 240))
    f_coat.add_vertex((320, 242))
    f_coat.add_vertex((331, 248))
    f_coat.add_vertex((351, 266))
    f_coat.add_vertex((361, 274))
    f_coat.add_vertex((363, 277))
    f_coat.add_vertex((370, 292))
    f_coat.add_vertex((377, 295))
    f_coat.add_vertex((506, 326))
    f_coat.add_vertex((520, 325))
    f_coat.add_vertex((558, 343))
    f_coat.add_vertex((581, 352))
    f_coat.add_vertex((606, 365))
    f_coat.add_vertex((608, 368))
    f_coat.add_vertex((609, 371))
    f_coat.add_vertex((609, 373))
    f_coat.add_vertex((610, 383))
    f_coat.add_vertex((619, 402))
    f_coat.add_vertex((662, 536))
    f_coat.add_vertex((661, 547))
    f_coat.add_vertex((659, 561))
    f_coat.add_vertex((658, 569))
    f_coat.add_vertex((656, 579))
    f_coat.add_vertex((652, 591))
    f_coat.add_vertex((646, 599))
    f_coat.add_vertex((635, 608))
    f_coat.add_vertex((620, 620))
    f_coat.add_vertex((610, 624))
    f_coat.add_vertex((603, 625))
    f_coat.add_vertex((598, 623))
    f_coat.add_vertex((591, 620))
    f_coat.add_vertex((591, 643))
    f_coat.add_vertex((590, 655))
    f_coat.add_vertex((590, 693))
    f_coat.add_vertex((589, 712))
    f_coat.add_vertex((590, 720))
    f_coat.add_vertex((514, 720))
    f_coat.add_vertex((430, 720))
    f_coat.add_vertex((338, 720))
    f_coat.add_vertex((221, 720))
    f_coat.add_vertex((167, 720))
    f_coat.add_vertex((182, 655))
    f_coat.add_vertex((192, 588))
    f_coat.add_vertex((199, 558))
    f_coat.add_vertex((219, 452))
    f_coat.add_vertex((212, 489))
    f_coat.add_vertex((208, 443))
    f_coat.add_vertex((191, 424))
    f_coat.add_vertex((178, 404))
    f_coat.add_vertex((176, 399))
    f_coat.add_vertex((173, 362))
    f_coat.add_vertex((178, 305))
    f_coat.add_vertex((193, 241))
    f_coat.add_vertex((215, 165))
    f_coat.add_vertex((223, 129))
    f_coat.add_vertex((238, 93))
    f_coat.add_vertex((258, 68))
    f_coat.add_vertex((263, 62))
    f_coat.add_vertex((280, 51))
    f_coat.add_vertex((339, 92))
    f_coat.add_vertex((343, 96))
    f_coat.add_vertex((345, 99))
    f_coat.add_vertex((343, 109))
    f_coat.add_vertex((338, 129))
    f_coat.add_vertex((331, 141))
    f_coat.add_vertex((314, 177))
    f_coat.add_vertex((310, 188))
    f_coat.add_vertex((305, 200))
    f_coat.add_vertex((299, 221))
    f_coat.add_vertex((298, 232))
    f_coat.color = 'darkgrey'
    f_coat.filled = True
    f_coat.fill_color = 'darkgrey'
    return f_coat


def t_setup_f_neck():
    f_neck = GPolygon()
    f_neck.add_vertex((388, 190))
    f_neck.add_vertex((409, 176))
    f_neck.add_vertex((430, 185))
    f_neck.add_vertex((465, 165))
    f_neck.add_vertex((492, 167))
    f_neck.add_vertex((522, 197))
    f_neck.add_vertex((536, 223))
    f_neck.add_vertex((508, 253))
    f_neck.add_vertex((505, 337))
    f_neck.add_vertex((453, 406))
    f_neck.add_vertex((375, 307))
    f_neck.add_vertex((382, 278))
    f_neck.add_vertex((391, 245))
    f_neck.add_vertex((386, 218))
    f_neck.add_vertex((384, 210))
    f_neck.add_vertex((387, 198))
    f_neck.color = 'lightgoldenrodyellow'
    f_neck.filled = True
    f_neck.fill_color = 'lightgoldenrodyellow'
    return f_neck


def t_setup_f_r_eye():
    f_r_eye = GPolygon()
    f_r_eye.add_vertex((422, 157))
    f_r_eye.add_vertex((423, 155))
    f_r_eye.add_vertex((424, 155))
    f_r_eye.add_vertex((436, 157))
    f_r_eye.add_vertex((448, 161))
    f_r_eye.add_vertex((451, 162))
    f_r_eye.add_vertex((457, 163))
    f_r_eye.add_vertex((446, 169))
    f_r_eye.add_vertex((436, 172))
    f_r_eye.add_vertex((430, 164))
    f_r_eye.add_vertex((427, 160))
    f_r_eye.color = 'ghostwhite'
    f_r_eye.filled = True
    f_r_eye.fill_color = 'ghostwhite'
    return f_r_eye


def t_setup_f_l_eye():
    f_l_eye = GPolygon()
    f_l_eye.add_vertex((502, 168))
    f_l_eye.add_vertex((505, 165))
    f_l_eye.add_vertex((512, 164))
    f_l_eye.add_vertex((521, 163))
    f_l_eye.add_vertex((526, 163))
    f_l_eye.add_vertex((524, 169))
    f_l_eye.add_vertex((520, 173))
    f_l_eye.add_vertex((517, 176))
    f_l_eye.add_vertex((510, 173))
    f_l_eye.add_vertex((505, 170))
    f_l_eye.color = 'ghostwhite'
    f_l_eye.filled = True
    f_l_eye.fill_color = 'ghostwhite'
    return f_l_eye


def t_setup_f_nose():
    f_nose = GPolygon()
    f_nose.add_vertex((469, 181))
    f_nose.add_vertex((471, 178))
    f_nose.add_vertex((478, 178))
    f_nose.add_vertex((487, 178))
    f_nose.add_vertex((494, 180))
    f_nose.add_vertex((494, 183))
    f_nose.add_vertex((484, 190))
    f_nose.add_vertex((478, 190))
    f_nose.add_vertex((476, 189))
    f_nose.add_vertex((473, 185))
    f_nose.add_vertex((472, 184))
    f_nose.filled = True
    return f_nose


def t_setup_f_cloth():
    f_cloth = GPolygon()
    f_cloth.add_vertex((375, 307))
    f_cloth.add_vertex((453, 406))
    f_cloth.add_vertex((505, 337))
    f_cloth.add_vertex((506, 317))
    f_cloth.add_vertex((520, 325))
    f_cloth.add_vertex((523, 350))
    f_cloth.add_vertex((526, 425))
    f_cloth.add_vertex((525, 521))
    f_cloth.add_vertex((515, 626))
    f_cloth.add_vertex((516, 693))
    f_cloth.add_vertex((514, 714))
    f_cloth.add_vertex((512, 720))
    f_cloth.add_vertex((466, 720))
    f_cloth.add_vertex((421, 720))
    f_cloth.add_vertex((309, 720))
    f_cloth.add_vertex((319, 694))
    f_cloth.add_vertex((334, 645))
    f_cloth.add_vertex((337, 634))
    f_cloth.add_vertex((355, 573))
    f_cloth.add_vertex((368, 530))
    f_cloth.add_vertex((376, 506))
    f_cloth.add_vertex((378, 474))
    f_cloth.add_vertex((378, 402))
    f_cloth.add_vertex((377, 389))
    f_cloth.add_vertex((375, 334))
    f_cloth.add_vertex((374, 315))
    f_cloth.color = 'peru'
    f_cloth.filled = True
    f_cloth.fill_color = 'peru'
    return f_cloth


def t_setup_f_r_hand():
    f_r_hand = GPolygon()
    f_r_hand.add_vertex((266, 60))
    f_r_hand.add_vertex((264, 48))
    f_r_hand.add_vertex((265, 46))
    f_r_hand.add_vertex((272, 37))
    f_r_hand.add_vertex((285, 25))
    f_r_hand.add_vertex((304, 17))
    f_r_hand.add_vertex((320, 14))
    f_r_hand.add_vertex((343, 10))
    f_r_hand.add_vertex((357, 10))
    f_r_hand.add_vertex((359, 11))
    f_r_hand.add_vertex((365, 17))
    f_r_hand.add_vertex((370, 27))
    f_r_hand.add_vertex((373, 41))
    f_r_hand.add_vertex((372, 51))
    f_r_hand.add_vertex((372, 66))
    f_r_hand.add_vertex((376, 81))
    f_r_hand.add_vertex((367, 92))
    f_r_hand.add_vertex((359, 95))
    f_r_hand.add_vertex((354, 93))
    f_r_hand.add_vertex((348, 90))
    f_r_hand.add_vertex((342, 92))
    f_r_hand.add_vertex((334, 93))
    f_r_hand.add_vertex((324, 96))
    f_r_hand.add_vertex((318, 99))
    f_r_hand.add_vertex((311, 95))
    f_r_hand.add_vertex((304, 101))
    f_r_hand.add_vertex((296, 100))
    f_r_hand.add_vertex((290, 96))
    f_r_hand.add_vertex((283, 89))
    f_r_hand.add_vertex((274, 74))
    f_r_hand.add_vertex((271, 69))
    f_r_hand.color = 'khaki'
    f_r_hand.filled = True
    f_r_hand.fill_color = 'khaki'
    return f_r_hand


def t_setup_f_l_hand():
    f_l_hand = GPolygon()
    f_l_hand.add_vertex((609, 444))
    f_l_hand.add_vertex((615, 447))
    f_l_hand.add_vertex((619, 450))
    f_l_hand.add_vertex((632, 459))
    f_l_hand.add_vertex((641, 464))
    f_l_hand.add_vertex((656, 482))
    f_l_hand.add_vertex((658, 486))
    f_l_hand.add_vertex((658, 489))
    f_l_hand.add_vertex((656, 494))
    f_l_hand.add_vertex((661, 498))
    f_l_hand.add_vertex((658, 506))
    f_l_hand.add_vertex((649, 524))
    f_l_hand.add_vertex((637, 534))
    f_l_hand.add_vertex((636, 536))
    f_l_hand.add_vertex((631, 538))
    f_l_hand.add_vertex((628, 538))
    f_l_hand.add_vertex((621, 538))
    f_l_hand.add_vertex((617, 541))
    f_l_hand.add_vertex((600, 543))
    f_l_hand.add_vertex((594, 538))
    f_l_hand.add_vertex((590, 534))
    f_l_hand.add_vertex((582, 535))
    f_l_hand.add_vertex((575, 531))
    f_l_hand.add_vertex((573, 528))
    f_l_hand.add_vertex((570, 524))
    f_l_hand.add_vertex((569, 518))
    f_l_hand.add_vertex((570, 513))
    f_l_hand.add_vertex((571, 511))
    f_l_hand.add_vertex((557, 506))
    f_l_hand.add_vertex((556, 481))
    f_l_hand.add_vertex((558, 472))
    f_l_hand.add_vertex((567, 463))
    f_l_hand.add_vertex((584, 452))
    f_l_hand.add_vertex((600, 446))
    f_l_hand.color = 'khaki'
    f_l_hand.filled = True
    f_l_hand.fill_color = 'khaki'
    return f_l_hand


def b_setup_w_white():
    w_white = GPolygon()
    w_white.add_vertex((799, 151))
    w_white.add_vertex((809, 148))
    w_white.add_vertex((825, 147))
    w_white.add_vertex((839, 150))
    w_white.add_vertex((852, 158))
    w_white.add_vertex((863, 157))
    w_white.add_vertex((874, 157))
    w_white.add_vertex((880, 160))
    w_white.add_vertex((888, 165))
    w_white.add_vertex((896, 177))
    w_white.add_vertex((901, 185))
    w_white.add_vertex((943, 341))
    w_white.add_vertex((953, 340))
    w_white.add_vertex((966, 338))
    w_white.add_vertex((973, 339))
    w_white.add_vertex((983, 336))
    w_white.add_vertex((977, 349))
    w_white.add_vertex((972, 357))
    w_white.add_vertex((962, 363))
    w_white.add_vertex((968, 364))
    w_white.add_vertex((977, 367))
    w_white.add_vertex((972, 372))
    w_white.add_vertex((964, 377))
    w_white.add_vertex((939, 720))
    w_white.add_vertex((893, 720))
    w_white.add_vertex((820, 720))
    w_white.add_vertex((794, 720))
    w_white.add_vertex((810, 554))
    w_white.add_vertex((840, 425))
    w_white.add_vertex((793, 327))
    w_white.add_vertex((802, 235))
    w_white.add_vertex((831, 202))
    w_white.add_vertex((836, 198))
    w_white.add_vertex((841, 193))
    w_white.add_vertex((839, 184))
    w_white.add_vertex((837, 178))
    w_white.add_vertex((832, 173))
    w_white.add_vertex((828, 166))
    w_white.add_vertex((820, 159))
    w_white.add_vertex((808, 153))
    w_white.add_vertex((803, 152))
    w_white.color = 'ghostwhite'
    w_white.filled = True
    w_white.fill_color = 'ghostwhite'
    return w_white


def b_setup_w_red():
    w_red = GPolygon()
    w_red.add_vertex((837, 408))
    w_red.add_vertex((831, 415))
    w_red.add_vertex((828, 420))
    w_red.add_vertex((819, 436))
    w_red.add_vertex((807, 439))
    w_red.add_vertex((799, 442))
    w_red.add_vertex((785, 457))
    w_red.add_vertex((760, 491))
    w_red.add_vertex((747, 517))
    w_red.add_vertex((724, 561))
    w_red.add_vertex((712, 588))
    w_red.add_vertex((708, 600))
    w_red.add_vertex((703, 637))
    w_red.add_vertex((711, 651))
    w_red.add_vertex((733, 667))
    w_red.add_vertex((742, 668))
    w_red.add_vertex((756, 668))
    w_red.add_vertex((756, 683))
    w_red.add_vertex((754, 697))
    w_red.add_vertex((753, 711))
    w_red.add_vertex((756, 720))
    w_red.add_vertex((790, 720))
    w_red.add_vertex((822, 720))
    w_red.add_vertex((825, 708))
    w_red.add_vertex((829, 670))
    w_red.add_vertex((839, 614))
    w_red.add_vertex((851, 551))
    w_red.add_vertex((859, 510))
    w_red.add_vertex((871, 455))
    w_red.add_vertex((874, 433))
    w_red.add_vertex((881, 414))
    w_red.add_vertex((928, 408))
    w_red.add_vertex((926, 445))
    w_red.add_vertex((921, 471))
    w_red.add_vertex((911, 520))
    w_red.add_vertex((908, 565))
    w_red.add_vertex((907, 598))
    w_red.add_vertex((905, 623))
    w_red.add_vertex((905, 676))
    w_red.add_vertex((905, 720))
    w_red.add_vertex((970, 720))
    w_red.add_vertex((1044, 720))
    w_red.add_vertex((1050, 718))
    w_red.add_vertex((1057, 717))
    w_red.add_vertex((1056, 694))
    w_red.add_vertex((1056, 680))
    w_red.add_vertex((1055, 643))
    w_red.add_vertex((1054, 630))
    w_red.add_vertex((1061, 626))
    w_red.add_vertex((1066, 620))
    w_red.add_vertex((1071, 614))
    w_red.add_vertex((1073, 608))
    w_red.add_vertex((1072, 599))
    w_red.add_vertex((1071, 574))
    w_red.add_vertex((1060, 506))
    w_red.add_vertex((1049, 465))
    w_red.add_vertex((1041, 444))
    w_red.add_vertex((1037, 436))
    w_red.add_vertex((1027, 426))
    w_red.add_vertex((1008, 415))
    w_red.add_vertex((1001, 412))
    w_red.add_vertex((991, 408))
    w_red.add_vertex((995, 405))
    w_red.add_vertex((1001, 403))
    w_red.add_vertex((996, 396))
    w_red.add_vertex((987, 390))
    w_red.add_vertex((975, 383))
    w_red.add_vertex((857, 375))
    w_red.add_vertex((931, 370))
    w_red.add_vertex((891, 370))
    w_red.color = 'darkred'
    w_red.filled = True
    w_red.fill_color = 'darkred'
    return w_red


def b_setup_w_head():
    w_head = GPolygon()
    w_head.add_vertex((832, 203))
    w_head.add_vertex((820, 191))
    w_head.add_vertex((810, 182))
    w_head.add_vertex((795, 171))
    w_head.add_vertex((783, 170))
    w_head.add_vertex((778, 170))
    w_head.add_vertex((772, 180))
    w_head.add_vertex((769, 206))
    w_head.add_vertex((769, 211))
    w_head.add_vertex((773, 241))
    w_head.add_vertex((778, 256))
    w_head.add_vertex((783, 269))
    w_head.add_vertex((780, 276))
    w_head.add_vertex((778, 292))
    w_head.add_vertex((779, 308))
    w_head.add_vertex((780, 325))
    w_head.add_vertex((778, 356))
    w_head.add_vertex((778, 372))
    w_head.add_vertex((778, 377))
    w_head.add_vertex((781, 382))
    w_head.add_vertex((783, 383))
    w_head.add_vertex((788, 394))
    w_head.add_vertex((789, 395))
    w_head.add_vertex((799, 402))
    w_head.add_vertex((802, 404))
    w_head.add_vertex((814, 409))
    w_head.add_vertex((823, 411))
    w_head.add_vertex((831, 413))
    w_head.add_vertex((838, 414))
    w_head.add_vertex((843, 414))
    w_head.add_vertex((849, 414))
    w_head.add_vertex((856, 413))
    w_head.add_vertex((863, 413))
    w_head.add_vertex((866, 416))
    w_head.add_vertex((873, 429))
    w_head.add_vertex((882, 448))
    w_head.add_vertex((890, 450))
    w_head.add_vertex((894, 451))
    w_head.add_vertex((903, 452))
    w_head.add_vertex((912, 451))
    w_head.add_vertex((926, 444))
    w_head.add_vertex((928, 436))
    w_head.add_vertex((930, 429))
    w_head.add_vertex((931, 425))
    w_head.add_vertex((932, 420))
    w_head.add_vertex((938, 410))
    w_head.add_vertex((934, 399))
    w_head.add_vertex((929, 390))
    w_head.add_vertex((925, 384))
    w_head.add_vertex((929, 374))
    w_head.add_vertex((932, 368))
    w_head.add_vertex((936, 361))
    w_head.add_vertex((940, 355))
    w_head.add_vertex((943, 345))
    w_head.add_vertex((944, 340))
    w_head.add_vertex((948, 331))
    w_head.add_vertex((950, 305))
    w_head.add_vertex((949, 294))
    w_head.add_vertex((946, 283))
    w_head.add_vertex((943, 274))
    w_head.add_vertex((946, 265))
    w_head.add_vertex((951, 251))
    w_head.add_vertex((958, 220))
    w_head.add_vertex((962, 203))
    w_head.add_vertex((961, 194))
    w_head.add_vertex((959, 173))
    w_head.add_vertex((956, 166))
    w_head.add_vertex((953, 161))
    w_head.add_vertex((949, 161))
    w_head.add_vertex((935, 163))
    w_head.add_vertex((926, 166))
    w_head.add_vertex((915, 175))
    w_head.add_vertex((904, 181))
    w_head.add_vertex((891, 195))
    w_head.add_vertex((887, 200))
    w_head.add_vertex((882, 210))
    w_head.add_vertex((877, 212))
    w_head.add_vertex((870, 214))
    w_head.add_vertex((859, 222))
    w_head.add_vertex((846, 238))
    w_head.add_vertex((837, 254))
    w_head.add_vertex((829, 266))
    w_head.add_vertex((824, 281))
    w_head.add_vertex((822, 273))
    w_head.add_vertex((820, 260))
    w_head.add_vertex((821, 243))
    w_head.add_vertex((825, 221))
    w_head.add_vertex((828, 209))
    w_head.color = 'lightgrey'
    w_head.filled = True
    w_head.fill_color = 'lightgrey'
    return w_head


def b_setup_w_nose():
    w_nose = GPolygon()
    w_nose.add_vertex((813, 340))
    w_nose.add_vertex((823, 335))
    w_nose.add_vertex((836, 335))
    w_nose.add_vertex((831, 347))
    w_nose.add_vertex((824, 349))
    w_nose.add_vertex((816, 346))
    w_nose.add_vertex((814, 343))
    w_nose.filled = True
    return w_nose


def b_setup_w_r_hand():
    w_r_hand = GPolygon()
    w_r_hand.add_vertex((823, 594))
    w_r_hand.add_vertex((810, 588))
    w_r_hand.add_vertex((796, 586))
    w_r_hand.add_vertex((774, 589))
    w_r_hand.add_vertex((762, 595))
    w_r_hand.add_vertex((746, 608))
    w_r_hand.add_vertex((743, 624))
    w_r_hand.add_vertex((743, 642))
    w_r_hand.add_vertex((753, 660))
    w_r_hand.add_vertex((768, 668))
    w_r_hand.add_vertex((770, 670))
    w_r_hand.add_vertex((788, 674))
    w_r_hand.add_vertex((800, 674))
    w_r_hand.add_vertex((806, 672))
    w_r_hand.add_vertex((810, 666))
    w_r_hand.add_vertex((810, 663))
    w_r_hand.add_vertex((807, 659))
    w_r_hand.add_vertex((816, 651))
    w_r_hand.add_vertex((822, 649))
    w_r_hand.add_vertex((829, 636))
    w_r_hand.add_vertex((829, 628))
    w_r_hand.add_vertex((827, 617))
    w_r_hand.add_vertex((824, 613))
    w_r_hand.color = 'lightgrey'
    w_r_hand.filled = True
    w_r_hand.fill_color = 'lightgrey'
    return w_r_hand


def b_setup_w_l_hand():
    w_l_hand = GPolygon()
    w_l_hand.add_vertex((889, 552))
    w_l_hand.add_vertex((896, 564))
    w_l_hand.add_vertex((892, 576))
    w_l_hand.add_vertex((891, 580))
    w_l_hand.add_vertex((894, 587))
    w_l_hand.add_vertex((898, 593))
    w_l_hand.add_vertex((904, 599))
    w_l_hand.add_vertex((922, 598))
    w_l_hand.add_vertex((925, 606))
    w_l_hand.add_vertex((932, 608))
    w_l_hand.add_vertex((947, 607))
    w_l_hand.add_vertex((959, 603))
    w_l_hand.add_vertex((968, 597))
    w_l_hand.add_vertex((975, 589))
    w_l_hand.add_vertex((976, 571))
    w_l_hand.add_vertex((976, 565))
    w_l_hand.add_vertex((974, 555))
    w_l_hand.add_vertex((963, 529))
    w_l_hand.add_vertex((961, 526))
    w_l_hand.add_vertex((959, 523))
    w_l_hand.add_vertex((945, 515))
    w_l_hand.add_vertex((944, 516))
    w_l_hand.add_vertex((933, 514))
    w_l_hand.add_vertex((923, 517))
    w_l_hand.add_vertex((911, 523))
    w_l_hand.add_vertex((895, 540))
    w_l_hand.color = 'lightgrey'
    w_l_hand.filled = True
    w_l_hand.fill_color = 'lightgrey'
    return w_l_hand


def t_setup_w_white():
    w_white = GPolygon()
    w_white.add_vertex((729, 148))
    w_white.add_vertex((738, 142))
    w_white.add_vertex((752, 139))
    w_white.add_vertex((757, 138))
    w_white.add_vertex((771, 141))
    w_white.add_vertex((779, 136))
    w_white.add_vertex((793, 135))
    w_white.add_vertex((807, 137))
    w_white.add_vertex((823, 144))
    w_white.add_vertex((831, 151))
    w_white.add_vertex((882, 276))
    w_white.add_vertex((895, 288))
    w_white.add_vertex((901, 294))
    w_white.add_vertex((914, 292))
    w_white.add_vertex((929, 285))
    w_white.add_vertex((970, 270))
    w_white.add_vertex((1007, 659))
    w_white.add_vertex((1005, 696))
    w_white.add_vertex((1005, 720))
    w_white.add_vertex((940, 720))
    w_white.add_vertex((900, 720))
    w_white.add_vertex((850, 720))
    w_white.add_vertex((830, 720))
    w_white.add_vertex((813, 720))
    w_white.add_vertex((804, 699))
    w_white.add_vertex((798, 576))
    w_white.add_vertex((799, 561))
    w_white.add_vertex((798, 506))
    w_white.add_vertex((799, 479))
    w_white.add_vertex((805, 453))
    w_white.add_vertex((819, 418))
    w_white.add_vertex((822, 411))
    w_white.add_vertex((831, 402))
    w_white.add_vertex((757, 331))
    w_white.add_vertex((753, 281))
    w_white.add_vertex((741, 212))
    w_white.add_vertex((768, 193))
    w_white.add_vertex((768, 186))
    w_white.add_vertex((775, 177))
    w_white.add_vertex((770, 166))
    w_white.add_vertex((767, 163))
    w_white.add_vertex((760, 157))
    w_white.add_vertex((748, 149))
    w_white.add_vertex((741, 149))
    w_white.color = 'ghostwhite'
    w_white.filled = True
    w_white.fill_color = 'ghostwhite'
    return w_white


def t_setup_w_red1():
    w_red = GPolygon()
    w_red.add_vertex((792, 387))
    w_red.add_vertex((784, 393))
    w_red.add_vertex((779, 405))
    w_red.add_vertex((776, 418))
    w_red.add_vertex((785, 421))
    w_red.add_vertex((799, 421))
    w_red.add_vertex((800, 421))
    w_red.add_vertex((808, 429))
    w_red.add_vertex((794, 434))
    w_red.add_vertex((779, 446))
    w_red.add_vertex((771, 458))
    w_red.add_vertex((770, 463))
    w_red.add_vertex((764, 477))
    w_red.add_vertex((763, 492))
    w_red.add_vertex((761, 518))
    w_red.add_vertex((760, 539))
    w_red.add_vertex((754, 569))
    w_red.add_vertex((733, 606))
    w_red.add_vertex((727, 614))
    w_red.add_vertex((726, 627))
    w_red.add_vertex((729, 637))
    w_red.add_vertex((735, 650))
    w_red.add_vertex((741, 654))
    w_red.add_vertex((744, 655))
    w_red.add_vertex((747, 657))
    w_red.add_vertex((749, 659))
    w_red.add_vertex((751, 661))
    w_red.add_vertex((766, 660))
    w_red.add_vertex((768, 679))
    w_red.add_vertex((769, 698))
    w_red.add_vertex((786, 696))
    w_red.add_vertex((804, 688))
    w_red.add_vertex((804, 664))
    w_red.add_vertex((801, 630))
    w_red.add_vertex((799, 578))
    w_red.add_vertex((797, 545))
    w_red.add_vertex((798, 504))
    w_red.add_vertex((801, 471))
    w_red.add_vertex((809, 445))
    w_red.add_vertex((817, 425))
    w_red.add_vertex((825, 408))
    w_red.add_vertex((832, 400))
    w_red.add_vertex((828, 392))
    w_red.add_vertex((822, 386))
    w_red.add_vertex((806, 387))
    w_red.add_vertex((796, 387))
    w_red.color = 'darkred'
    w_red.filled = True
    w_red.fill_color = 'darkred'
    return w_red


def t_setup_w_red2():
    w_red = GPolygon()
    w_red.add_vertex((924, 685))
    w_red.add_vertex((961, 677))
    w_red.add_vertex((996, 666))
    w_red.add_vertex((1006, 665))
    w_red.add_vertex((1053, 654))
    w_red.add_vertex((1078, 651))
    w_red.add_vertex((1074, 618))
    w_red.add_vertex((1067, 576))
    w_red.add_vertex((1054, 531))
    w_red.add_vertex((1032, 449))
    w_red.add_vertex((1019, 389))
    w_red.add_vertex((1012, 349))
    w_red.add_vertex((1013, 305))
    w_red.add_vertex((1014, 289))
    w_red.add_vertex((1013, 258))
    w_red.add_vertex((1014, 235))
    w_red.add_vertex((1004, 179))
    w_red.add_vertex((997, 147))
    w_red.add_vertex((982, 99))
    w_red.add_vertex((974, 84))
    w_red.add_vertex((964, 77))
    w_red.add_vertex((954, 71))
    w_red.add_vertex((909, 57))
    w_red.add_vertex((886, 109))
    w_red.add_vertex((885, 119))
    w_red.add_vertex((889, 129))
    w_red.add_vertex((903, 162))
    w_red.add_vertex((920, 204))
    w_red.add_vertex((928, 227))
    w_red.add_vertex((929, 239))
    w_red.add_vertex((929, 269))
    w_red.add_vertex((929, 321))
    w_red.add_vertex((907, 315))
    w_red.add_vertex((900, 316))
    w_red.add_vertex((887, 316))
    w_red.add_vertex((881, 316))
    w_red.add_vertex((874, 319))
    w_red.add_vertex((868, 331))
    w_red.add_vertex((867, 387))
    w_red.add_vertex((874, 451))
    w_red.add_vertex((893, 536))
    w_red.add_vertex((904, 585))
    w_red.add_vertex((911, 629))
    w_red.add_vertex((917, 664))
    w_red.add_vertex((920, 678))
    w_red.color = 'darkred'
    w_red.filled = True
    w_red.fill_color = 'darkred'
    return w_red


def t_setup_w_head():
    w_head = GPolygon()
    w_head.add_vertex((768, 193))
    w_head.add_vertex((747, 181))
    w_head.add_vertex((723, 171))
    w_head.add_vertex((712, 170))
    w_head.add_vertex((705, 175))
    w_head.add_vertex((704, 187))
    w_head.add_vertex((705, 203))
    w_head.add_vertex((709, 220))
    w_head.add_vertex((728, 256))
    w_head.add_vertex((729, 279))
    w_head.add_vertex((737, 313))
    w_head.add_vertex((735, 334))
    w_head.add_vertex((739, 359))
    w_head.add_vertex((746, 367))
    w_head.add_vertex((762, 377))
    w_head.add_vertex((791, 386))
    w_head.add_vertex((803, 386))
    w_head.add_vertex((821, 385))
    w_head.add_vertex((830, 396))
    w_head.add_vertex((833, 407))
    w_head.add_vertex((842, 414))
    w_head.add_vertex((859, 410))
    w_head.add_vertex((868, 403))
    w_head.add_vertex((867, 385))
    w_head.add_vertex((867, 364))
    w_head.add_vertex((868, 330))
    w_head.add_vertex((870, 324))
    w_head.add_vertex((874, 318))
    w_head.add_vertex((877, 317))
    w_head.add_vertex((889, 316))
    w_head.add_vertex((899, 316))
    w_head.add_vertex((901, 316))
    w_head.add_vertex((902, 302))
    w_head.add_vertex((902, 281))
    w_head.add_vertex((901, 278))
    w_head.add_vertex((896, 246))
    w_head.add_vertex((886, 226))
    w_head.add_vertex((888, 214))
    w_head.add_vertex((890, 191))
    w_head.add_vertex((889, 170))
    w_head.add_vertex((880, 140))
    w_head.add_vertex((873, 131))
    w_head.add_vertex((865, 124))
    w_head.add_vertex((853, 130))
    w_head.add_vertex((833, 148))
    w_head.add_vertex((820, 165))
    w_head.add_vertex((816, 183))
    w_head.add_vertex((806, 187))
    w_head.add_vertex((790, 206))
    w_head.add_vertex((779, 225))
    w_head.add_vertex((776, 242))
    w_head.add_vertex((770, 231))
    w_head.add_vertex((768, 219))
    w_head.add_vertex((767, 202))
    w_head.add_vertex((768, 198))
    w_head.color = 'lightgrey'
    w_head.filled = True
    w_head.fill_color = 'lightgrey'
    return w_head


def t_setup_w_r_hand():
    w_r_hand = GPolygon()
    w_r_hand.add_vertex((776, 548))
    w_r_hand.add_vertex((760, 539))
    w_r_hand.add_vertex((756, 538))
    w_r_hand.add_vertex((738, 538))
    w_r_hand.add_vertex((725, 542))
    w_r_hand.add_vertex((722, 546))
    w_r_hand.add_vertex((721, 552))
    w_r_hand.add_vertex((720, 553))
    w_r_hand.add_vertex((722, 556))
    w_r_hand.add_vertex((718, 563))
    w_r_hand.add_vertex((717, 573))
    w_r_hand.add_vertex((719, 581))
    w_r_hand.add_vertex((718, 584))
    w_r_hand.add_vertex((718, 594))
    w_r_hand.add_vertex((721, 598))
    w_r_hand.add_vertex((720, 602))
    w_r_hand.add_vertex((718, 610))
    w_r_hand.add_vertex((720, 620))
    w_r_hand.add_vertex((721, 623))
    w_r_hand.add_vertex((726, 624))
    w_r_hand.add_vertex((737, 626))
    w_r_hand.add_vertex((744, 624))
    w_r_hand.add_vertex((766, 618))
    w_r_hand.add_vertex((773, 610))
    w_r_hand.add_vertex((773, 601))
    w_r_hand.add_vertex((772, 595))
    w_r_hand.add_vertex((776, 591))
    w_r_hand.add_vertex((778, 577))
    w_r_hand.add_vertex((778, 556))
    w_r_hand.color = 'lightgrey'
    w_r_hand.filled = True
    w_r_hand.fill_color = 'lightgrey'
    return w_r_hand


def t_setup_w_l_hand():
    w_l_hand = GPolygon()
    w_l_hand.add_vertex((860, 44))
    w_l_hand.add_vertex((860, 66))
    w_l_hand.add_vertex((865, 78))
    w_l_hand.add_vertex((869, 80))
    w_l_hand.add_vertex((866, 85))
    w_l_hand.add_vertex((870, 97))
    w_l_hand.add_vertex((874, 102))
    w_l_hand.add_vertex((884, 104))
    w_l_hand.add_vertex((888, 105))
    w_l_hand.add_vertex((903, 107))
    w_l_hand.add_vertex((917, 105))
    w_l_hand.add_vertex((936, 100))
    w_l_hand.add_vertex((940, 98))
    w_l_hand.add_vertex((951, 85))
    w_l_hand.add_vertex((955, 64))
    w_l_hand.add_vertex((954, 60))
    w_l_hand.add_vertex((949, 41))
    w_l_hand.add_vertex((942, 35))
    w_l_hand.add_vertex((937, 33))
    w_l_hand.add_vertex((931, 34))
    w_l_hand.add_vertex((926, 29))
    w_l_hand.add_vertex((921, 27))
    w_l_hand.add_vertex((911, 26))
    w_l_hand.add_vertex((902, 33))
    w_l_hand.add_vertex((896, 32))
    w_l_hand.add_vertex((891, 31))
    w_l_hand.add_vertex((887, 34))
    w_l_hand.add_vertex((878, 33))
    w_l_hand.add_vertex((869, 35))
    w_l_hand.add_vertex((862, 39))
    w_l_hand.color = 'lightgrey'
    w_l_hand.filled = True
    w_l_hand.fill_color = 'lightgrey'
    return w_l_hand


def t_setup_w_nose():
    w_nose = GPolygon()
    w_nose.add_vertex((770, 312))
    w_nose.add_vertex((774, 309))
    w_nose.add_vertex((786, 306))
    w_nose.add_vertex((780, 307))
    w_nose.add_vertex((794, 306))
    w_nose.add_vertex((794, 309))
    w_nose.add_vertex((792, 315))
    w_nose.add_vertex((786, 321))
    w_nose.add_vertex((778, 320))
    w_nose.add_vertex((772, 316))
    w_nose.filled = True
    return w_nose


if __name__ == '__main__':
    main()
