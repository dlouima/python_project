import art
from game_data import data
import random
import os

final_score = 0
print(art.logo)

start_account_a = random.choice(data)
start_account_b = random.choice(data)


def data_format(account):
    """format the account data in order to print"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(user_guess, start_a_followers, start_b_followers):
    """Take user guess and follwer count and return it they guess right"""
    if start_a_followers > start_b_followers:
        return user_guess == 'a'
    else:
        return user_guess == "b"


game_continue = True
stat_account_b = random.choice(data)


while game_continue:
    # generate random number

    start_account_a = start_account_b
    account_b = random.choice(data)
    while start_account_a == start_account_b:
        start_account_b = random.choice(data)

    print(f"Compare A: {data_format(start_account_a)}")
    print(art.vs)
    print(f"Against B: {data_format(start_account_b)}\n")
    guess = input('Who has more followers "A" or " B: "').lower()

    account_a_followers = start_account_a['follower_count']
    account_b_followers = start_account_b['follower_count']
    is_correct = check_answer(guess, account_a_followers, account_b_followers)

    # clear the screen
    os.system("clear")
    print(art.logo)

    if is_correct:
        print(f'You are right! your current score is {final_score}')
        final_score += 1

    else:
        game_continue = False
        print(f"Sorry that's wrong. You current score is {final_score}")
