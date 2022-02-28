from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
players_choices = {}
end = "no"
print(logo)

def find_highest_bidder (bidding_record):
    highest_bid =0
    winner =''

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner =bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")

print("welcome to the silent auction ")

end = False

while not end:
    name = input('please  insert the name of the player: ')
    bit = int(input('please inser the player bit $: ' ))
    
    players_choices[name]= bit
    response = input("Is ther another player  enter yes or no  ")
    if (response  == 'no'):
        end = True

print(find_highest_bidder(players_choices))