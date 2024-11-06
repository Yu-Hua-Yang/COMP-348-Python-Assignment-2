import os
import time
from grid import Grid

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def display_menu():
    print("\n1. Let me select two elemenws")
    print("2. Uncover one element for me")
    print("3. I give up – reveal the grid")
    print("4. New game")
    print("5. Quit")

def get_coordinates(size, grid):
    """Prompt the user for cell coordinates in the format 'A0', 'B1', etc., and validate them."""
    while True:
        try:
            cell = input("\nEnter cell (e.g., A0): ").strip().upper()
            col = ord(cell[0]) - 65  # Convert column letter to an integer (A=0, B=1, etc.)
            row = int(cell[1:])      # Use the row number exactly as entered

            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                clear_screen()
                print_logo()
                grid.display_grid()
                if not (0 <= row < size) and not (0 <= col < size):
                    print("\nInput error: column and row entry is out of range for the grid. Please try again.")
                elif not (0 <= col < size):
                    print("\nInput error: column entry is out of range for the grid. Please try again.")
                elif not (0 <= row < size):
                    print("\nInput error: row entry is out of range for the grid. Please try again.")

        except (ValueError, IndexError):
            clear_screen()
            print_logo()
            grid.display_grid()
            print("\nInvalid input. Please enter in format 'A0', 'B1', etc.")


def print_logo():
  print("--------------------------------")
  print("|         Brain Buster         |")
  print("--------------------------------\n")
  
def choose_grid_size():
  while True:
        try:
            size = int(input("Enter grid size (2, 4, or 6): "))
            if size in (2, 4, 6):
                break
            else:
                clear_screen()
                print_logo()
                print("Invalid input. Please enter 2, 4, or 6.")
        except ValueError:
            clear_screen()
            print_logo()
            print("Invalid input. Please enter a number.")
            
  return size
def main():
    won = False
    clear_screen()
    print_logo()
    
    size = choose_grid_size()
    grid = Grid(size)

    minimum_guess = size * (size/2)
    opt1 = 0
    opt2 = 0
    
    while True:
        clear_screen()
        print_logo()
        grid.display_grid()
        if won:
            if opt1 == 0:
              print("\nYou cheated -- Loser! You're score is 0!")
            else:
              print("\nOh Happy Day. You've won!! Your score is: "  + str(int((minimum_guess/(opt1 + opt2)) * 100)))
        display_menu()
        choice = input("\nSelect: ")

        if choice == '1':
            clear_screen()
            print_logo()
            grid.display_grid()
            print("\nSelect the first cell:")
            first_coords = get_coordinates(size, grid)
            
            if first_coords:
                row1, col1 = first_coords
                val1 = grid.reveal_cell(row1, col1)
                
                clear_screen()
                print_logo()
                grid.display_grid()
                
                print("\nSelect the second cell:")
                
                while True:
                  second_coords = get_coordinates(size, grid)

                  # Check if the second coordinate is the same as the first one
                  if second_coords == first_coords:
                      clear_screen()
                      print_logo()
                      grid.display_grid()
                      print("\nInvalid selection: You cannot select the same cell twice. Please choose a different cell.")
                  else:
                      break  # Exit the loop if the second cell is different
                    
                if second_coords:
                    row2, col2 = second_coords
                    val2 = grid.reveal_cell(row2, col2)
                    
                    clear_screen()
                    print_logo()
                    grid.display_grid()
                    
                    if val1 == val2:
                        print("\nIt's a match!")
                        time.sleep(2)
                    else:
                        print("\nNot a match.")
                        time.sleep(2)  # Show the cells for 2 seconds
                        grid.hide_cells([(row1, col1), (row2, col2)])
                        
            opt1 += 1
            won = grid.is_grid_revealed()
                        
        elif choice == '2':
            # Reveal a single cell
            clear_screen()
            print_logo()
            grid.display_grid()
            print("\nSelect a cell to reveal:")
            coords = get_coordinates(size, grid)
            if coords:
                row, col = coords
                val = grid.reveal_cell(row, col)
                clear_screen()
                grid.display_grid()
                print(f"\nCell ({chr(col + 65)}{row}): {val}")
            opt2 += 2
            won = grid.is_grid_revealed()

        elif choice == '3':
            # Reveal the entire grid
            print("\nRevealing the entire grid:")
            for row in range(size):
                for col in range(size):
                    grid.reveal_cell(row, col)
            clear_screen()
            grid.display_grid()

        elif choice == '4':
            # Start a new game
            clear_screen()
            print_logo()
            size = choose_grid_size()
            grid = Grid(size)
            won = False
            minimum_guess = size * (size/2)
            opt1 = 0
            opt2 = 0

        elif choice == '5':
            clear_screen()
            print_logo()
            grid.display_grid()
            display_menu()
            print("\nThank you for playing! Goodbye.\n")
            break

        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()
