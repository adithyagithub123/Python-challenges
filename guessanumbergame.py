import random
import time

number = random.randint(1,100)

def intro() :
    print("May I ask your name")
    global name
    name = input()
    print(name + ",we are going to play a game , I am thinking of a number between 1 to 100")
    if (number%2 == 0) :
        x = "even"
    else :
        x = "odd"
    print("\n This is an {} number".format(x))
    time.sleep(.5)
    print("GO AHEAD GUESS!!!")

def pick() :
    guesses = 0
    while guesses < 6 :
        time.sleep(.5)
        enter = input("Guess !! : ")
        try :
            guess = int(enter)
            if guess <= 100 and guess>=1 :
                guesses = guesses + 1
                if guesses < 6 :
                    if guess < number :
                        print("The number that you have guessed is too low") 
                    if guess > number :
                        print("The number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess == number :
                        break
            if guess>100 or guess<1 :
                print("The number isnt in the range ")
                time.sleep(.5)
                print("please enter a number between 1 to 100")
        except :
            print("I dont think "+enter+" is a number , Try AGAIN !!")
    if guess == number :
        guesses = str(guesses)
        print("Good job , {} you have guessed my number in {} guesses".format(name,guesses))
    if guess != number :
        print("I was thinking of "+str(number))

playagain = "yes"
while playagain == "yes" or playagain == "Yes" or playagain =="Y" or playagain == "y" or playagain == "YEs" or playagain == "YES" or playagain == "yES" or playagain == "yeS" or playagain == "yEs" :
    intro()
    pick()
    print("Do you want to play again")
    playagain = input()