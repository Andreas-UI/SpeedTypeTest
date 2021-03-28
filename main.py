#  Import Library
import pygame as pg
import sys
import random
import time
from numberQuestion import numberQuestion
from score import Score
from stopwatch import Stopwatch
from input import Input
from previousList import PreviousList
from win import Win

pg.init()
clock = pg.time.Clock()

#  Set Screen
screenWidth = 800
screenHeight = 500
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Speed Type")

# Texts and Fonts
base_font = pg.font.Font(None, 32)
input_text = ""

# Colors
background_color = (242, 247, 255)
input_box_color = (0, 0, 0)
text_color = (0, 0, 0)

# Input
input = Input(screen, text_color, base_font, input_text, input_box_color)

# # backEndTimer
stopwatch = Stopwatch(screen, text_color, base_font)

# Score
score = Score(screen, text_color, base_font)

# Question
question = numberQuestion(screen, text_color, base_font)
total_question = random.randint(5, 10)

# Previous Question and Timer
previous = []
pList = PreviousList(screen, base_font, previous)

# WIn
win = Win(score.score_value, len(pList.previous), screen, text_color, base_font, total_question)

def main():
    # Game Loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:

                    # Redraw input_text except the last
                    input.input_text = input.input_text[:-1]

                elif event.key == pg.K_RETURN:
                    if input.input_text == question.question_value:
                        win.correct += 1

                        # Set endTimer with the current click in this section
                        stopwatch.endTimer = pg.time.get_ticks()

                        # Calculate the time difference between startTImer and endTimer
                        stopwatch.deltaTime = stopwatch.endTimer - stopwatch.startTimer

                        # Increase Scire by 1
                        score.score_value += round(((len(input.input_text)) * 1/(stopwatch.deltaTime)) * 1000)
                        print(score.score_value)

                        # Set startTimer with the current click in this section
                        stopwatch.startTimer = pg.time.get_ticks()

                        # Append previous from pList with information (input_text, question, deltaTime, True/False) as a history
                        pList.previous.append([str(input.input_text), str(question.question_value), str(stopwatch.deltaTime/1000), True])

                        # Set current input_text to nothing
                        input.input_text = ""

                        # Append the current history position by adding integer
                        pList.moveDown()


                        # Set current question by calling the generateQuestion function
                        question.question_value = question.generateQuestion()

                        # print(stopwatch.deltaTime/1000)
                    else:
                        
                        # Set endTimer with the current click in this section
                        stopwatch.endTimer = pg.time.get_ticks()

                        # Calculate the time difference between startTImer and endTimer
                        stopwatch.deltaTime = stopwatch.endTimer - stopwatch.startTimer

                        # Set startTimer with the current click in this section
                        stopwatch.startTimer = pg.time.get_ticks()

                        # Append previous from pList with information (input_text, question, deltaTime, True/False) as a history
                        pList.previous.append([str(input.input_text), str(question.question_value), str(stopwatch.deltaTime/1000), False])

                        # Set current input_text to nothing
                        input.input_text = ""

                        # Append the current history position by adding integer
                        pList.moveDown()


                        # Set current question by calling the generateQuestion function
                        question.question_value = question.generateQuestion()

                        # print(stopwatch.deltaTime/1000)

                else:

                    # When type, input_text will continue draw the unicode pressed by the keyboard
                    input.input_text += event.unicode

        # Background Color
        screen.fill(background_color)

        # Render input_text to surface
        input.updateInput()

        # Set endTimer with the continous ticking time
        stopwatch.endTimer = pg.time.get_ticks()

        # Render stopwatch to surface
        stopwatch.updateTimer()

        # Render score to surface
        score.updateScore()

        # Render question to surface
        question.updateQuestion()

        # Render previous list
        pList.updatepreviousList()

        # Render Win
        win.total = len(pList.previous)
        win.score = score.score_value

        if win.updateWin():

            # Cannot think of other words, so gameOver = paused
            paused = True

            while paused:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_c:
                            paused = False
                            score.score_value = 0
                            pList.pos_y = 60
                            pList.previous = []
                            main()
                        elif event.key == pg.K_q:
                            pg.quit()
                            quit()

                win.drawWin()
                pg.time.Clock().tick(60)
            

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()