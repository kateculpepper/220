"""
Name: <Kate Culpepper>
<Lab5.py

Problem: <This program implements the  vigenere cipher, where a different shift amount is
given to each character. It takes input from the user in a seperate window then outputs
the resulting message in the same window>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
from graphics import *


def vigenere():
    win_width = 400
    win_height = 400
    win = GraphWin("vigenere", win_width, win_height)
    win.setBackground("white")

    entry_1 = Entry(Point(250, 75), 30)
    entry_1.draw(win)
    text_1 = Text(Point(60, 75), "Message to code")
    text_1.draw(win)
    key_entry = Entry(Point(250, 115), 30)
    key_entry.draw(win)
    text_2 = Text(Point(60, 115), "Enter key word ")
    text_2.draw(win)

    encode_box = Rectangle(Point(200, 150), Point(300, 200))
    encode_box.draw(win)
    encode_txt = Text(Point(250, 175), "Encode")
    encode_txt.draw(win)

    win.getMouse()
    user_code = entry_1.getText().upper().replace(" ", "")
    user_key = key_entry.getText().upper().replace(" ", "")
    encode_txt.undraw()
    encode_box.undraw()
    output = " "
    for i in range(len(user_code)):
        msg_value = ord(user_code[i]) - 65
        key_value = ord(user_key[i % len(user_key)]) - 65
        result_msg = ((msg_value + key_value) % 26) + 65
        output = output + chr(result_msg)

    result_msg2 = Text(Point(200, 175), "Resulting Message")
    result_msg2.draw(win)
    result_txt = Text(Point(200, 200), output)
    result_txt.draw(win)
    close_txt = Text(Point(200, 375), "Click anywhere to close window")
    close_txt.draw(win)

    win.getMouse()
    win.close()


vigenere()
