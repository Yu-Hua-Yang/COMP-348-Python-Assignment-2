import os
from grid import Grid

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def display_menu():
    print("1. Let me select two elemenws")
    print("2. Uncover one element for me")
    print("3. I give up – reveal the grid")
    print("4. New game")
    print("5. Quit")

def get_coordinates(size):
    """Prompt the user for cell coordinates in the format 'A0', 'B1', etc., and validate them."""
    try:
        cell = input("Enter cell (e.g., A0): ").strip().upper()
        col = ord(cell[0]) - 65  # Convert column letter to an integer (A=0, B=1, etc.)
        row = int(cell[1:])      # Use the row number exactly as entered

        if 0 <= row < size and 0 <= col < size:
            return row, col
        else:
            print("Coordinates out of bounds. Try again.")
            return None
    except (ValueError, IndexError):
        print("Invalid input. Please enter in format 'A0', 'B1', etc.")
        return None

def print_logo():
  print("--------------------------------")
  print("|         Brain Buster         |")
  print("--------------------------------")
def main():
    clear_screen()
    print_logo()
    size = int(input("Enter grid size (2, 4, or 6): "))
    grid = Grid(size)

    while True:
        clear_screen()
        print_logo()
        grid.display_grid()
        display_menu()
        choice = input("\nSelect: ")

        if choice == '1':
            # Guess a pair of cells
            print("\nSelect the first cell:")
            first_coords = get_coordinates(size)
            if not first_coords:
                continue

            print("Select the second cell:")
            second_coords = get_coordinates(size)
            if not second_coords:
                continue

            row1, col1 = first_coords
            row2, col2 = second_coords

            val1 = grid.reveal_cell(row1, col1)
            val2 = grid.reveal_cell(row2, col2)

            clear_screen()
            grid.display_grid()
            print(f"\nFirst cell ({chr(col1 + 65)}{row1}): {val1}")
            print(f"Second cell ({chr(col2 + 65)}{row2}): {val2}")

            if val1 == val2:
                print("It's a match!")
            else:
                print("Not a match. Try again.")
                grid.hide_cell(row1, col1)
                grid.hide_cell(row2, col2)

        elif choice == '2':
            # Reveal a single cell
            print("\nSelect a cell to reveal:")
            coords = get_coordinates(size)
            if coords:
                row, col = coords
                val = grid.reveal_cell(row, col)
                clear_screen()
                grid.display_grid()
                print(f"\nCell ({chr(col + 65)}{row}): {val}")

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
            size = int(input("Enter grid size (2, 4, or 6): "))
            grid = Grid(size)

        elif choice == '5':
            print("Thank you for playing! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
