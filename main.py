class Board:
    def __init__(self, number_of_generations):
        self.board = [[0 for j in range(10)] for i in range(9)]
        self.transform = {"a": 1, "b": 2, "c": 3, "d": 4,
                          "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
        self.number_of_generations = number_of_generations
        for i in range(0, len(self.board)):
            self.board[i][0] = i+1
        self.board.insert(0, ["  A, B, C, D, E, F, G, H, I"])
        self.show_board("Board created")

    def show_board(self, title=""):
        print("\n")
        print(title)
        print("-"*len(title))
        for row in self.board:
            print(row)

    def input(self, user_input):
        data = user_input.replace(" ", "").split(",")
        for item in data:
            column = item[:1].lower()
            line = int(item[1:])
            if column in self.transform:
                column = self.transform.get(column)
                self.board[line][column] = 1
        self.show_board("Inserted cells. Ready to simulate!")

    def board_is_not_empty(self):
        for row in range(1, len(self.board)):
            for column in range(1, len(self.board)):
                if self.board[row][column] == 1:
                    return True
        # self.show_board("This is the life!")
        return False

    def calculate_neighbors(self, row, column):

        top = self.board[row-1][column] if row >= 2 else 0
        top_right_diagonal = self.board[row-1][column +
                                               1] if row >= 2 and column <= 8 else 0
        right = self.board[row][column+1] if column <= 8 else 0
        bottom_right_diagonal = self.board[row +
                                           1][column+1] if row <= 8 and column <= 8 else 0
        bottom = self.board[row+1][column] if row <= 8 else 0

        bottom_left_diagonal = self.board[row +
                                          1][column-1] if row <= 8 and column >= 2 else 0
        left = self.board[row][column-1] if column >= 2 else 0
        top_left_diagonal = self.board[row-1][column -
                                              1] if row >= 2 and column >= 2 else 0

        sum = top + top_right_diagonal + right + bottom_right_diagonal + \
            bottom + bottom_left_diagonal + left + top_left_diagonal
        return sum

    def change_state(self, indices):
        for row in indices:
            self.board[row[0][0]][row[0][1]] = row[1]

    def start(self):
        generation = 0
        indices_to_change = []
        # while(self.board_is_not_empty()):
        for i in range(0, self.number_of_generations):
            for row in range(1, len(self.board)):
                for column in range(1, len(self.board)):
                    current = self.board[row][column]
                    neighbors_amount = self.calculate_neighbors(row, column)
                    if (current == 1 and (neighbors_amount < 2 or neighbors_amount > 3)):  # die
                        indices_to_change.append([[row, column], 0])
                    elif current == 0 and neighbors_amount == 3:  # living
                        indices_to_change.append([[row, column], 1])
            self.change_state(indices_to_change)
            indices_to_change.clear()
            self.show_board(f"Generation {i}")

game = Board(10)
# data = input("enter the cells separated by comma: ")
data = "c1, d2, b3, c3, d3"
game.input(data)
game.start()
