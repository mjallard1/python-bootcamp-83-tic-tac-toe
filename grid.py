from os import system
import numpy as np

class Grid:

  NUMBER_OF_CELLS = 9

  EMPTY = "     "

  SYMBOLS = {
    0 : "  O  ", 
    1 : "  X  "
  }

  EMPTY_GRID = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
      ]


  def __init__(self) -> None:
      self.reset()


  def reset(self) -> None:
    self.grid = self.EMPTY_GRID
    self.empty_cells = self.NUMBER_OF_CELLS
    self.symbol_index = 0
    self.winner: str
    self.print_grid()


  def print_grid(self) -> None:
    system('clear')
    rows = []
    print('\n')
    for row in self.grid:
      rows.append("|".join(row))
    print("\n_ _ _ _ _ _ _ _ _\n\n".join(rows))
    print('\n')
  

  def fill_cell(self, row: int, column: int) -> None:
    if self.grid[row][column] != self.EMPTY:
      raise Exception("Cell already filled. try again.")

    self.grid[row][column] = self.SYMBOLS[self.symbol_index]
    self.empty_cells -= 1
    

  
  def switch_player(self) -> None:
    self.symbol_index = (self.symbol_index + 1) % 2


  def has_empty_cells(self) -> bool:
    return self.empty_cells > 0

  
  def has_winner(self) -> bool:
    #check horizontals
    for row in self.grid:
      if self.is_win(row):
        return True

    #check verticals
    transposition = np.transpose(self.grid)
    for row in transposition:
      if self.is_win(row):
        return True

    #check diagonals
    first_diagonal = np.diag(self.grid)
    if self.is_win(first_diagonal):
      return True

    second_diagonal = np.diag(np.fliplr(self.grid))
    if self.is_win(second_diagonal):
      return True

    return False
  

  def get_winner(self) -> str:
    return self.winner

  
  def is_win(self, row) -> bool:
    for cell in row:
      if cell != self.SYMBOLS[self.symbol_index]:
        return False
    self.winner = self.SYMBOLS[self.symbol_index]
    return True