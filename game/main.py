import random



def choose_options():
  options = ('Rock', 'Paper', 'Scissors')
  user_option = input("Rock, Paper or Scissors? => ").capitalize().strip()
  computer_option = random.choice(options)
  
  if not user_option in options:
    print('That is not a valid option')
    # continue
    return None, None
  
  # prints
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Tie! 😅')
  elif user_option == "Rock":
    if computer_option == 'Scissors':
      print("Rock wins to Scissors")
      print('User wins! 😁')
      user_wins += 1
    else:
      print("Paper wins to Rock")
      print("Computer wins 😭")
      computer_wins += 1
  elif user_option == 'Paper':
    if computer_option == 'Rock':
      print("Paper wins to Rock")
      print('User wins! 😁')
      user_wins += 1
    else:
      print("Scissors win to Paper")
      print("Computer wins 😭")
      computer_wins += 1
  elif user_option == 'Scissors':
    if computer_option == 'Rock':
      print("Rock wins to Scissors")
      print("Computer wins 😭")
      computer_wins += 1
    else:
      print("Scissors win to Paper")
      print('User wins! 😁')
      user_wins += 1
      
  return user_wins, computer_wins

def run_game():
  rounds = 1   
  computer_wins = 0
  user_wins = 0

  while True:  
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)
  
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
    
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print("The Winner is:      COMPUTER!!")
      break
      
    if user_wins == 2:
      print("The Winner is:        USER!!")
      break
      
    rounds += 1
    
run_game()