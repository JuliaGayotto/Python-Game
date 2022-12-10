import random

def randomnum():
    return random.randint(1, 3)

def rockpaperscissors():
    answer = randomnum()
    choice = int(input("Choose \n1-Rock \n2-Paper \n3-Scissors \n"))
    if choice == 1 and answer == 3:
        print('Congratulations, You win!! Your opponent choose scissors.')
        return True
    elif choice == 1 and answer == 2:
        print("I'm sorry, you lost.Your opponent choose paper.")
        return False
    elif choice == 2 and answer == 1:
        print('Congratulations, You win!! Your opponent choose rock.')
        return True
    elif choice == 2 and answer == 3:
        print("I'm sorry, you lost.Your opponent choose scissors.")
        return False
    elif choice == 3 and answer == 2:
        print('Congratulations, You win!! Your opponent choose paper.')
        return True
    elif choice == 3 and answer == 1:
        print("I'm sorry, you lost.Your opponent choose rock.")
        return False
    else:
        print("Tie! Your opponent choose the same. Let's go again!")
        rockpaperscissors()
