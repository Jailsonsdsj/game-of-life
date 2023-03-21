#blocks = input("enter the cells separated by a comma: ")

#cells = blocks.split(",")
class Board:
    def __init__(self):
        self.board = [[0 for j in range(10)] for i in range(9)]
        self.transform = {"a":1, "b":2, "c":3, "d":4, "e":5,"f":6, "g":7, "h":8, "i":9}

        for i in range(0, len(self.board)):
            self.board[i][0] = i+1
        self.board.insert(0,["  A, B, C, D, E, F, G, H, I"])

        # self.show_board("Board created")

    def show_board(self, title):
        print("\n")
        print(title)
        print("-"*len(title))
        for row in self.board:
            print(row) 

    def input(self, user_input):
        data = user_input.replace(" ","").split(",")
        for item in data:
            column = item[:1].lower()
            line = int(item[1:])
          
            if column in self.transform:
                column = self.transform.get(column)
                self.board[line][column] = 1
        self.show_board("Inserted cells. Ready to simulate!")

    def board_is_empty(self):
        for row in range(1, len(self.board)):
            for column in range(1,row):
               if self.board[row][column] == 1:
                    return False
                    
        print("This is the life")
        return True

    def check_neighbour():

        pass

    def start(self):
        if(not self.board_is_empty()):
           #first rule

           for row in range(1, len(self.board)):
            for column in range(1,row):
               current = self.board[row][column]
               if current == 1:
                    left = current - 1 
                    right = current + 1 

                    print(current)
           


game = Board()

game.input("B2, B3, B5, c1")
game.start()



