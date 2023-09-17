import random
import datetime


def main():
  print("Welcome to the SIMPLE Strategy Game!")
  hu_time = datetime.datetime.now()
  print(hu_time)
  target = random.randint(10,
                          50)  #set a random target number between 10 and 50
  current_number = 0
  player_turn = True  #true for player,false for computer

  while current_number < target:
    print(f"\nCurrent number: {current_number}")
    if player_turn:
      player_move = get_player_move()  #calls the get_player_move function
      current_number += player_move
      print(f"You choose to add {player_move} to the current number.")
    else:
      computer_move = get_computer_move(target, current_number)
      current_number += computer_move
      print(f"Computer choose to add {computer_move} to tge current number.")
    player_turn = not player_turn  #switch turns


def get_player_move():
  while True:
    try:
      move = int(input("Enter 10 or 20 to add to the current number:"))
      if move == 10 or move == 20:
        return move
      else:
        print("Invalid input")
    except ValueError:
      print("Invalid input,pls enter 10 or 20")


def get_computer_move(target, current_number):
  val = target - current_number
  max_possible_move = min(2, val)  #smallest nr between 2 and val
  return random.randint(
      1, max_possible_move)  #returns with a number between 1 and max_pos..


if __name__ == "__main__":
  main()
