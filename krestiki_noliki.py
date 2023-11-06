class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        row = int(input("Введите номер строки: "))
        col = int(input("Введите номер столбца: "))
        return row, col
class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

        self.players = [Player("Игрок 1", 'X'), Player("Игрок 2", 'O')]
        self.current_player = self.players[0]

    def print_board(self):
        print("---------")
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(cell, end="|")
            print("\n---------")

    def is_winner(self, symbol):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.print_board()
            row, col = self.current_player.make_move()

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player.symbol

                if self.is_winner(self.current_player.symbol):
                    self.print_board()
                    print(f"Победил игрок {self.current_player.name}!")
                    break
                elif self.is_draw():
                    self.print_board()
                    print("Ничья!")
                    break

                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
            else:
                print("Эта ячейка уже занята!")
game = Game()
game.play()