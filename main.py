import math
from grid import Grid


grid = Grid()


def choose_game_type():
  play_human = input("Do you want to play against a human or not? (y/n): ")
  if play_human == 'y':
    return
  if play_human == 'n':
    return
  else:
    print("Invalid option. Try again.")
    choose_game_type()


def game_over():
  print('GAME OVER')
  if grid.has_winner():
    print(f"Player \"{grid.get_winner().strip()}\" has won!\n")
  else:
    print("It's a tie!\n")


def play_again():
  again = input("Want to play another game? (y/n): ")
  if (again == 'y'):
    grid.reset()
    play_game()
  if (again != 'n'):
    print("Invalid option. try again.")
    play_again()


def play_game():
  choose_game_type()
  while grid.has_empty_cells():
    cell = int(input("Input cell id please (top left is 1, bottom right is 9): ")) - 1
    if  cell < 0 or cell > 8:
      print("Invalid option. try again.")
      continue
    try:
      grid.fill_cell(math.floor(cell/3), cell%3)
      grid.print_grid()
      if grid.has_winner():
        break
      grid.switch_player()
    except Exception as message:
      print(message)
  game_over()
  play_again()


if __name__ == "__main__":
  play_game()