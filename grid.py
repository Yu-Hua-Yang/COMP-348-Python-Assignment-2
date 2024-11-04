import random

class Grid:
    def __init__(self, size):
        """Initialize the grid with the given size and set up hidden pairs."""
        self.size = size
        self.grid = [['X' for _ in range(size)] for _ in range(size)]
        self.hidden_values = self._generate_hidden_pairs()
        self.revealed = [[False for _ in range(size)] for _ in range(size)]

    def _generate_hidden_pairs(self):
        """Generate shuffled pairs of values for the grid."""
        num_pairs = (self.size * self.size) // 2
        pairs = [i for i in range(num_pairs) for _ in range(2)]
        random.shuffle(pairs)
        return pairs

    def reveal_cell(self, row, col):
        """Reveal a cell at the specified location."""
        if not (0 <= row < self.size and 0 <= col < self.size):
            print("Invalid cell coordinates.")
            return None
        self.revealed[row][col] = True
        index = row * self.size + col
        return self.hidden_values[index]

    def hide_cell(self, row, col):
        """Hide a cell again after revealing."""
        if not (0 <= row < self.size and 0 <= col < self.size):
            return
        self.revealed[row][col] = False

    def display_grid(self):
        """Display the current state of the grid with labeled rows and columns."""
        # Print the top header with column letters
        print("    ", end="")
        for col in range(self.size):
            print(f" [{chr(65 + col)}]", end="")
        print()

        # Print each row with a row label and grid content
        for row in range(self.size):
            print(f"[{row}]", end=" ")
            for col in range(self.size):
                if self.revealed[row][col]:
                    index = row * self.size + col
                    print(f" {self.hidden_values[index]:2}", end=" ")
                else:
                    print("  X", end=" ")
            print()
