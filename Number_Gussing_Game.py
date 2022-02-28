import random
logo = """
 _                _              _   _                 _                   _____                        _ 
| |              | |            | \ | |               | |                 |  __ \                      | |
| |    _   _  ___| | ___   _    |  \| |_   _ _ __ ___ | |__   ___ _ __    | |  \/ __ _ _ __ ___   ___  | |
| |   | | | |/ __| |/ / | | |   | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|   | | __ / _` | '_ ` _ \ / _ \ | |
| |___| |_| | (__|   <| |_| |   | |\  | |_| | | | | | | |_) |  __/ |      | |_\ \ (_| | | | | | |  __/ |_|
\_____/\__,_|\___|_|\_\\__, |   \_| \_/\__,_|_| |_| |_|_.__/ \___|_|       \____/\__,_|_| |_| |_|\___| (_)
                        __/ |                                                                             
                       |___/                                                                              
                      
"""""

print(logo)

print('Welcom to Guessing Your Lucky Number Game \n')

lucky_number = random.randrange(0, 100)

print('I am thinking of a number between 0 and 100 \n')

print('Can you guess that number \n')

level = 0
dificulty = input("Choose a dificulty level. type 'easy' or 'hard': ")


if dificulty == 'easy':
    print('you have 10 attempts')
    level = 10
elif dificulty == 'hard':
    print('You have 5 atemps')
    level = 5
else:
    print("Please enter 'easy' or 'hard '")

user_guess = 0
while level != 0 and user_guess != lucky_number:
    user_guess = int(input('Make a guess: '))
    if user_guess == lucky_number:
        print(f'You go it.  the luck number is  {lucky_number}')
        print('Congratulation! You win the game')
    elif user_guess < lucky_number:
        print('too low. try again: \n')
        level -= 1
        print(f'You have {level} attempts remaining to guess the number\n')
    elif user_guess > lucky_number:
        print('too high. try again: \n')
        level -= 1
        print(f'You have {level} attempts remaining to guess the number\n')
    else:
        print('please enter a number between 1 and 100')
        level -= 1
if level == 0:
    print(' You have used all your attempts\n')
    print('Game over. you loose!\n')
