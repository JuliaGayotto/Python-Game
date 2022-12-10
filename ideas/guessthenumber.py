import random

def randomnum():
    return random.randint(1, 100)

def game1():
    answer = randomnum()
    totalguesses = 0 
    num = int(input('Input a integer between 1 and 100: '))
    while num != answer:
        totalguesses +=1
        if num > answer:
            print('Too high! Make another guess.')
            num = int(input('Input a another number: '))
        else:
            print('Too low! Make another guess.')
            num = int(input('Input a another number: '))

    if totalguesses == 0:
        print('WOWWW!! Congratulations, you guessed right at the first try!!')
    else:
        print(f'Congratulations! You guessed right in {totalguesses + 1} tries!')

def ask1():
    question = input('Do you wanna play again? Y/N ')
    if question == 'Y' or question == 'y':
        return game1()
