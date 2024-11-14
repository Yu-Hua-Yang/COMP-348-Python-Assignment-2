import os
import time
from grid import Grid

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def display_menu():
    print("\n1. Select two elements")
    print("2. Reveal one element")
    print("3. Reveal entire grid")
    print("4. New game")
    print("5. Quit")

def get_coordinates(size, grid):
    while True:
        try:
            cell = input("\nEnter cell (e.g., A0): ").strip().upper()
            col, row = ord(cell[0]) - 65, int(cell[1:])

            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                show_invalid_coordinate_message(size, row, col, grid)
        except (ValueError, IndexError):
            clear_screen()
            print_logo()
            grid.display_grid()
            print("\nInvalid input format. Please enter in format 'A0', 'B1', etc.")

def show_invalid_coordinate_message(size, row, col, grid):
    clear_screen()
    print_logo()
    grid.display_grid()
    if not (0 <= row < size) and not (0 <= col < size):
        print("\nInput error: column and row entry is out of range for the grid. Please try again.")
    elif not (0 <= col < size):
        print("\nInput error: column entry is out of range for the grid. Please try again.")
    elif not (0 <= row < size):
        print("\nInput error: row entry is out of range for the grid. Please try again.")

def print_logo():
    print("--------------------------------")
    print("|         Brain Buster         |")
    print("--------------------------------\n")

def choose_grid_size():
    while True:
        try:
            size = int(input("Enter grid size (2, 4, or 6): "))
            if size in (2, 4, 6):
                return size
            else:
                clear_screen()
                print_logo()
                print("Invalid size. Enter 2, 4, or 6.")
        except ValueError:
            clear_screen()
            print_logo()
            print("Invalid input. Please enter a number.")

def main():
    won = False
    clear_screen()
    print_logo()
    
    size = choose_grid_size()
    grid = Grid(size)
    minimum_guess = size * (size / 2)
    opt1 = opt2 = 0

    while True:
        clear_screen()
        print_logo()
        grid.display_grid()
        show_score_if_won(won, opt1, opt2, minimum_guess)
        
        display_menu()
        choice = input("\nSelect: ")

        if choice == '1':
            handle_match_selection(grid, size, opt1)
            opt1 += 1
            won = grid.is_grid_revealed()

        elif choice == '2':
            handle_single_reveal(grid, size)
            opt2 += 2
            won = grid.is_grid_revealed()

        elif choice == '3':
            reveal_entire_grid(grid, size)

        elif choice == '4':
            size, grid, won, opt1, opt2, minimum_guess = start_new_game()

        elif choice == '5':
            end_game(grid)
            break

        else:
            print("\nInvalid choice. Try again.")

def show_score_if_won(won, opt1, opt2, minimum_guess):
    if won:
        score = 0 if opt1 == 0 else int((minimum_guess / (opt1 + opt2)) * 100)
        print(f"\n{'You cheated -- Loser!' if score == 0 else 'Oh Happy Day, You won!!'} Score: {score}")

def handle_match_selection(grid, size, opt1):
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
            if second_coords != first_coords:
                break
            show_same_cell_error(grid)

        if second_coords:
            row2, col2 = second_coords
            val2 = grid.reveal_cell(row2, col2)

            clear_screen()
            print_logo()
            grid.display_grid()

            if val1 == val2:
                print("\nIt's a match!")
            else:
                print("\nNot a match.")
                time.sleep(2)
                grid.hide_cells([(row1, col1), (row2, col2)])

def show_same_cell_error(grid):
    clear_screen()
    print_logo()
    grid.display_grid()
    print("\nError: You cannot select the same cell twice. Choose a different cell.")

def handle_single_reveal(grid, size):
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

def reveal_entire_grid(grid, size):
    print("\nRevealing the entire grid:")
    for row in range(size):
        for col in range(size):
            grid.reveal_cell(row, col)
    clear_screen()
    grid.display_grid()

def start_new_game():
    clear_screen()
    print_logo()
    size = choose_grid_size()
    grid = Grid(size)
    return size, grid, False, 0, 0, size * (size / 2)

def end_game(grid):
    clear_screen()
    print_logo()
    grid.display_grid()
    display_menu()
    print("\nThank you for playing! Goodbye.\n")

if __name__ == "__main__":
    main()
