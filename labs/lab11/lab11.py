"""
Name: <Kate Culpepper>
<lab 11>.py

Problem: <This assignment runs a program the integrates to knew class types, door and button, and
 displays the door game in a graphics window>

Certification of Authenticity:

I certify that this assignment is my own work
"""

from lab10.button import Button
from lab10.door import Door
from graphics import *
from random import randint


def three_door_game():
    width_px = 700
    height_px = 700
    win = GraphWin("Door Game", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    door_1 = Door(Rectangle(Point(1, 2), Point(3, 7)), "Door 1")
    door_1.color_door("Brown")
    door_1.draw(win)

    door_2 = Door(Rectangle(Point(4, 2), Point(6, 7)), "Door 2")
    door_2.color_door("Brown")
    door_2.draw(win)

    door_3 = Door(Rectangle(Point(7, 2), Point(9, 7)), "Door 3")
    door_3.color_door("Brown")
    door_3.draw(win)

    button_rec = Rectangle(Point(7, 8), Point(9, 9))
    button = Button(button_rec, "Quit")
    button.draw(win)

    win_score = Rectangle(Point(1, 8), Point(2, 9))
    lose_score = Rectangle(Point(2, 8), Point(3, 9))
    win_score.draw(win)
    lose_score.draw(win)

    win_num = 0
    win_num_txt = Text(Point(1.5, 8.5), str(win_num))
    win_num_txt.draw(win)

    lose_num = 0
    lose_num_txt = Text(Point(2.5, 8.5), str(lose_num))
    lose_num_txt.draw(win)

    win_txt = Text(Point(1.5, 9.2), "wins")
    lose_txt = Text(Point(2.5, 9.2), "loses")
    win_txt.draw(win)
    lose_txt.draw(win)

    door_msg = Text(Point(5, 7.5), "I have a secret door")
    door_msg.draw(win)
    instructions = Text(Point(5, 1), "Click to guess which is the secret door!")
    instructions.draw(win)

    door_list = [door_1, door_2, door_3]
    random_door = randint(0, len(door_list)-1)
    door_list[random_door].set_secret(True)

    open = True
    while open:  #begin game
        mouse = win.getMouse()
        if button.is_clicked(mouse): # if quit is clicked close window
            open = False
            win.close()
        elif door_1.is_clicked(mouse) == True:  # if door 1 is clicked check if its correct
            if door_1.is_secret():
                win_num = win_num + 1
                win_num_txt.undraw()
                win_num_txt = Text(Point(1.5, 8.5), str(win_num))
                win_num_txt.draw(win)
                door_1.open("Green", "Door 1")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                win_msg = Text(Point(5, 7.5), "you win!")
                win_msg.draw(win)
                mouse = win.getMouse()

                if button.is_clicked(mouse) == False:  # reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    win_msg.undraw()
                    door_msg.draw(win)
                    instructions.draw(win)
                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close game
                    open = False
                    win.close()

            else:  # incorrect door
                lose_num = lose_num + 1
                lose_num_txt.undraw()
                lose_num_txt = Text(Point(2.5, 8.5), str(lose_num))
                lose_num_txt.draw(win)
                door_1.close("pink", "Door 1")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                lose_msg = Text(Point(5, 7.5), "sorry, incorrect")
                lose_msg.draw(win)

                mouse = win.getMouse()

                if button.is_clicked(mouse) == False: # reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    lose_msg.undraw()
                    door_msg.draw(win)
                    instructions.draw(win)
                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close game
                    open = False
                    win.close()
        elif door_2.is_clicked(mouse) == True: # check if door 2 is correct
            if door_2.is_secret():
                win_num = win_num + 1
                win_num_txt.undraw()
                win_num_txt = Text(Point(1.5, 8.5), str(win_num))
                win_num_txt.draw(win)
                door_2.open("Green", "Door 2")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                win_msg = Text(Point(5, 7.5), "you win!")
                win_msg.draw(win)
                mouse = win.getMouse()

                if button.is_clicked(mouse) == False: #reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    instructions.draw(win)
                    win_msg.undraw()
                    door_msg.draw(win)
                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close game
                    open = False
                    win.close()
            else: # incorrect door
                lose_num = lose_num + 1
                lose_num_txt.undraw()
                lose_num_txt = Text(Point(2.5, 8.5), str(lose_num))
                lose_num_txt.draw(win)
                door_2.close("pink", "Door 2")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                lose_msg = Text(Point(5, 7.5), "sorry, incorrect")
                lose_msg.draw(win)
                mouse = win.getMouse()

                if button.is_clicked(mouse) == False: # reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    instructions.draw(win)
                    lose_msg.undraw()
                    door_msg.draw(win)
                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close game
                    open = False
                    win.close()
        elif door_3.is_clicked(mouse) == True: # check if door three is correct
            if door_3.is_secret():
                win_num = win_num + 1
                win_num_txt.undraw()
                win_num_txt = Text(Point(1.5, 8.5), str(win_num))
                win_num_txt.draw(win)
                door_3.open("Green", "Door 3")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                win_msg = Text(Point(5, 7.5), "you win!")
                win_msg.draw(win)
                mouse = win.getMouse()

                if button.is_clicked(mouse) == False: # reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    instructions.draw(win)
                    win_msg.undraw()
                    door_msg.draw(win)
                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close game
                    open = False
                    win.close()
            else: # incorrect door
                lose_num = lose_num + 1
                lose_num_txt.undraw()
                lose_num_txt = Text(Point(2.5, 8.5), str(lose_num))
                lose_num_txt.draw(win)
                door_3.close("pink", "Door 3")
                instructions.undraw()
                play_again = Text(Point(5, 1), "Click anywhere to play again")
                play_again.draw(win)
                door_msg.undraw()
                lose_msg = Text(Point(5, 7.5), "sorry, incorrect")
                lose_msg.draw(win)
                mouse = win.getMouse()

                if button.is_clicked(mouse) == False: # reset game
                    door_list[random_door].set_secret(False)
                    play_again.undraw()
                    door_msg.draw(win)
                    lose_msg.undraw()
                    instructions.draw(win)

                    door_1.close("Brown", "Door 1")
                    door_2.close("Brown", "Door 2")
                    door_3.close("Brown", "Door 3")
                    door_list = [door_1, door_2, door_3]
                    random_door = randint(0, len(door_list) - 1)
                    door_list[random_door].set_secret(True)
                else: # close window
                    open = False
                    win.close()






three_door_game()
