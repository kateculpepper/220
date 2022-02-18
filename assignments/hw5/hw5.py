"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("Enter a persons first and last name:")
    first_name = name.split()[0]
    last_name = name.split()[1]
    print(last_name, ", " + first_name)


def company_name():
    user = input("Enter a domain :  ")
    split = user.split(".")
    output = split[1]
    print(output)


def initials():
    student_num = eval(input("How many students are in the class?: "))
    for student in range(student_num):
        name = input("what is the name of the student: ")
        split_f = name.split(" ")[0]
        split_l = name.split(" ")[1]
        output = split_f[0] + split_l[0]
        print(output)


def names():
    student_l = input("Enter a list of names :")
    split_names = student_l.split(", ")
    for i in range(len(split_names)):
        split_f = split_names[i].split(" ")[0]
        split_l = split_names[i].split(" ")[1]
        output = split_f[0] + split_l[0]
        print(output, end=" ")


def thirds():
    numSentence = input("Enter the number of sentences: ")
    sentenceList = []
    for i in range(int(numSentence)):
        sentence = input("enter sentence " + str(i + 1) + ": ")
        sentenceList.append(sentence)
    for k in range(len(sentenceList)):
        for j in range(0, len(sentenceList[k]), 3):
            print(sentenceList[k][j], end="")
        print()


def word_average():
    sentence = input("enter a sentence:")
    split_names = sentence.split(" ")









def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    word_average()
    # pig_latin()
