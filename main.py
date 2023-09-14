import random

def main():
  print("Welcome to the SIMPLE Strategy Game!")
  target=random.randint(10,50) #set a random target number between 10 and 50
  current_number=0
  player_turn=True #true for player,false for computer

  while current_number<target:
    print(f"\nCurrent number: {current_number}")
    if player_turn:
      player_move=get_player_move()


    
    main()

def get_player_move()_