#import module
import random
from tkinter import *


# initialize window
root = Tk()
root.geometry('300x300')
root.title('DataFlair-Number Generator')
Label(root, text= 'KB Number Guessing Game \n Have Fun!' , font = 'Garde 40 bold').pack()
Label(root, text = 'Start guessing!', font = 'trebutchet 15 ').place(x=40, y=200)

######Entry


frame = Frame(root)
frame.pack()

my_entry = Entry(frame, width = 100)
my_entry.place(x=60, y=240)
my_entry.insert(0,'Guess a number from 1 - 100!')
my_entry.pack(padx = 5, pady = 5)

def retrieve():
    print(my_entry.get())


################Guessing##############
user = my_entry.get()


def game():

    #Generate number
    num = random.randint(1,100)
    num = int(num)

    #player guesses
    guess = my_entry.get()
    guess = int(guess)

    #points
    pts = int(100)
    while pts >= 1:

        #Correct
        if num == guess:
            Label(root, text = 'BINGO! You got ' + pts + 'points!').place(x=40, y=300)
            break


        elif num >= guess:
            #too low
            #minus pts
            pts = pts - int(10)
            Label(root, text = 'The number you guessed is too low!' + '\n You now have ' + str(pts) + 'points!').place(x=40, y=300)
            if pts <= int(-50):
                Label(root, text = 'Unfornuately, you lost too much points at ' + str(pts) + 'points. The number I was thinking of was ' + str(num) )


        elif num <= guess:
            #too high
            #minus pts
            pts = pts - int(10)
            Label(root, text = 'The number you guessed is too high!' + '\n You now have ' + str(pts) + 'points!').place(x=40, y=300)
            if pts <= int(-50):
                Label(root, text = 'Unfornuately, you lost too much points at ' + str(pts) + 'points. The number I was thinking of was ' + str(num) )

def end():
    #replay option
    Label(root, text = 'Do you want to try again?').place(x=40, y=300)
    Button1 = Button(frame, text = 'Yes! One more.', command = restart)
    Button1.place(x=40, y=320)
    Button1.pack(padx = 5, pady = 5)

    Button2 = Button(frame, text = 'Nah. I give up.', command = exit)
    Button2.place(x=40, y=340)
    Button2.pack(padx = 5, pady = 5)


def restart():
    game()

def exit():
    exit()

Button = Button(frame, text = "Submit", command = game)
Button.place(x=70, y=260)
Button.pack(padx = 5, pady = 5)

root.mainloop()
