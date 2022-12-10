from rockpaperscissors import rockpaperscissors
import sys
from time import sleep

def typing(phrase):
    for letter in phrase:
        sleep(0.06)
        sys.stdout.write(letter)
        sys.stdout.flush()

def meet():
    typing("Hi friend! What's your name? ")
    name = input()
    typing(f"Nice to meet you {name}! I'm Martin, the guy responsable for guide you in this wonderfull game night. Before you choose a game, i would like to tell you the story behind this event. Since my boss, Austin Brooks, was a kid, he always loved to play games with his family. \nOne day, he decided to create a game challenge to have fun with his family and friends. The game night was so interesting that he decided repeat the event one night a year. Over the years, the game night gain a lot of prestigious and fame, and the demand of players grow up a lot. Because of that, Mr. Brooks can't give attention to all the players, so only the best ones are allow to chat with him.  \nDo you thing you have a chance? ")
    meet = input()
    typing("Okay, let's find out! \n")
    typing(f"Let's start with rock, paper, scissors to warm you up. Choosing your oppenent... You gonna play aggainst {name}. \nGame starting in 3 2 1\n")
    game1 = rockpaperscissors()
    if game1 == True:
        print("WOWWW! WHAT A GAME! You already win at your first game. Let's see if you really that good or if was just beginner's luck! The next game is The Password Game. \nDo you know how to play? Y/N")
    if game1 == False:
        print("Well, it wasn't a good start, but i believe you will recover soon. Let's keep playing! The next game is The Password Game. \nDo you know how to play? Y/N")

    know = input()

    game2rule = typing("explaned  the rule")

    if know == "N" or "n":
            print(game2rule)

meet()
