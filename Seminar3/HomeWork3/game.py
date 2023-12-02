from board import Board
from player import Player
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def start_game(self):
        self.initialize_players()
        self.current_player = self.player1

        while True:
            self.board.display()
            self.take_turn(self.current_player)

            if self.board.is_winner(self.current_player.symbol):
                print(f"Поздравляем, {self.current_player.name}! Вы выиграли!")
                break
            elif self.board.is_full():
                print("Ничья!")
                break

            self.switch_turn()

        self.ask_play_again()

    def initialize_players(self):
        name1 = input("Введите имя первого игрока: ")
        symbol1 = self.get_valid_symbol_input()
        self.player1 = Player(name1, symbol1)

        if symbol1 == 'X' or symbol1 == 'Х':
            symbol2 = 'O'
        else:
            symbol2 = 'X'
        name2 = input("Введите имя второго игрока или нажмите Enter, чтобы играть с компьютером: ")
        self.player2 = Player(name2 if name2 else "Компьютер", symbol2)

    def get_valid_symbol_input(self):
        while True:
            symbol = input("Выберите 'X' или 'O': ").upper()
            if symbol in ['X', 'O', 'Х', 'О']:
                return symbol
            else:
                print("Пожалуйста, выберите 'X' или 'O'.")

    def take_turn(self, player):
        print(f"\nХод игрока {player.name} ({player.symbol})")
        if player == self.player1 or (player == self.player2 and self.player2.name != "Компьютер"):
            row, col = self.get_valid_position_input()
        else:
            row, col = self.get_computer_move()
        self.board.update_board(row, col, player.symbol)

    def get_valid_position_input(self):
        while True:
            try:
                row = int(input("Выберите строку (от 1 до 3): "))
                col = int(input("Выберите столбец (от 1 до 3): "))
                if self.board.is_position_valid(row, col):
                    return row, col
                else:
                    print("Эта позиция уже занята или некорректна. Попробуйте еще раз.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 3.")

    def get_computer_move(self):
        available_positions = [(row, col) for row in range(1, 4) for col in range(1, 4)
                               if self.board.cells[row-1][col-1] == ' ']
        return random.choice(available_positions)

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def ask_play_again(self):
        while True:
            play_again = input("Хотите сыграть снова? (Да/Нет): ").lower()
            if play_again == 'да':
                self.board = Board()
                self.start_game()
            elif play_again == 'нет':
                print("Спасибо за игру! До свидания.")
                exit()
            else:
                print("Пожалуйста, введите 'Да' или 'Нет'.")

