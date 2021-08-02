"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Here is the basic version of breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			    # Number of attempts


def main():
    # initial window
    graphics = BreakoutGraphics()

    # other settings
    lives = NUM_LIVES
    vy = graphics.get_ball_dy()
    vx = graphics.get_ball_dx()

    # animation
    while True:
        pause(FRAME_RATE)
        if lives > 0 and graphics.num_bricks > 0:

            # first-click to start game
            if graphics.to_start is True:
                graphics.ball.move(vx, vy)

                # rebound when ball bumps into bricks or the paddle
                if graphics.detect_bump() is True:
                    # when near bricks
                    if graphics.ball.y < graphics.bricks_bottom:
                        vy = - vy       # change the vertical direction of ball

                    # when near paddle and the distance from top of paddle to bottom of ball is less than dy
                    # let ball not run along the paddle
                    elif graphics.ball.y + graphics.ball.height - graphics.paddle.y < graphics.get_ball_dy():
                        vy = - vy       # change the vertical direction of ball

                # when ball touches the left and right side of wall
                if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) > graphics.window.width:
                    vx = - vx       # change the horizontal direction of ball

                # when ball touches the upper side of wall
                if graphics.ball.y <= 0:
                    vy = - vy       # change the vertical direction of ball

                # when ball falls down out of window
                elif graphics.ball.y >= graphics.window.height:
                    lives -= 1
                    if lives > 0:
                        pause(FRAME_RATE * 100)
                        graphics.lives_label.text = str(lives) + ' lives left!'
                        graphics.show_lives_left()
                        pause(FRAME_RATE * 100)
                        graphics.window.remove(graphics.lives_label)
                        pause(FRAME_RATE * 100)
                        graphics.reset_ball()
                        pause(FRAME_RATE * 100)
        else:
            break

    # when win
    if graphics.num_bricks == 0:
        pause(FRAME_RATE * 50)
        graphics.game_win()

    # when lose
    elif lives == 0:
        pause(FRAME_RATE * 50)
        graphics.game_over()


if __name__ == '__main__':
    main()
