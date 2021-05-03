#import module
import random

def game():

    #player guesses
    guess = input('Guess the number')
    guess = int(guess)


    #points
    pts = int(100)
    while pts >= int(-50):

        #Correct
        if int(num) == int(guess):
            print('BINGO! You got ' + str(pts) + 'points!')
            break


        elif int(num) > int(guess):
            #too low
            #minus pts
            pts = pts - int(10)
            print('The number you guessed is too low!' + '\n You now have ' + str(pts) + 'points!')
            if pts <= int(-50):
                print('Unfornuately, you lost too much points at ' + str(pts) + 'points. The number I was thinking of was ' + str(num) )
            elif pts > int(-50):
                guess = input('Guess again!')


        elif int(num) < int(guess):
            #too high
            #minus pts
            pts = pts - int(10)
            print('The number you guessed is too high!' + '\n You now have ' + str(pts) + 'points!')
            if pts <= int(-50):
                print('Unfortunately, you lost too much points at ' + str(pts) + 'points. The number I was thinking of was ' + str(num) )
            elif pts > int(-50):
                guess = input('Guess again!')

def end():
    #replay option
    reply = input('Do you want to try again? y/n')
    if reply == 'y':
        game()
    elif reply == 'n':
        exit()


def restart():
    game()

def exit():
    exit()

#Generate number
num = random.randint(1,100)
num = int(num)



game()
