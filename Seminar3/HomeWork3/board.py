class Board:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]  # двумерный массив для представления доски 3x3

    def display(self):
        for row in self.cells:
            print(" | ".join(row))
            print("---------")

    def is_position_valid(self, row, col):
        return 1 <= row <= 3 and 1 <= col <= 3 and self.cells[row-1][col-1] == ' '

    def update_board(self, row, col, symbol):
        self.cells[row-1][col-1] = symbol

    def is_winner(self, symbol):
        # проверка на выигрышные комбинации
        winning_combinations = [
            [(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
            [(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
            [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]
        ]
        for combo in winning_combinations:
            if all(self.cells[row-1][col-1] == symbol for row, col in combo):
                return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.cells for cell in row)
