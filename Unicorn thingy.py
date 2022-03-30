'''
Oliver Trengrove Lucky unicorn game
this game allows users to bet money and win based on what token is returned

'''

import random
# the initial bet for each round is one dollar, the value of this variable can be changed based on needs
bet = 1
total_bet = 0
session_limit = 10
total_won = 0
current_win = 0
token_list=["donkey","horse","zebra","unicorn"]
print("Welcome to Oliver's lucky unicorn game \n"
      "Each round costs $" + str(bet) + ", you can only spend up to $10")
keep_going = "y"

# all the code for the game sits in the while loop. at the start of each round the user is asked if they want to play
while keep_going == "y":
  # check if the user is trying to bet more than the session limit, if so quit
  if total_bet >= session_limit:
    print("sorry you have reached the betting limit")
    break
  keep_going = input("Would you like to play a round? Press y, to quit press any other key")
  # checking that the user wants to play the game
  if keep_going != "y":
    break
  total_bet += 1
  chosen_token = random.choice(token_list)
  print("You got a {}".format(chosen_token))
  # calculate the money won based of the selected token
  if chosen_token =='zebra'or chosen_token =='horse':
    current_win = 0.5
    total_won += current_win
  elif chosen_token == 'unicorn':
    current_win = 5
    total_won += current_win
  else:
    current_win = 0

  print('you have won a total of $'+str(total_won))
  print('you have bet a total of $'+str(total_bet))
  if total_won <0:
    print("Sorry, you don't have enough money to continue. Gave over.")
    keep_going = "end"









