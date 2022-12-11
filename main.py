import random

class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self. M = M
        self.pole = self.init()
        self.counter = 0

    def generate_min(self, general_pole):
        massiv = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(0, self.M):
            line = random.randint(0,self.N - 1)
            column = random.randint(0,self.N - 1)
            general_pole[line][column].mine = True
            for j in massiv:
                if (line + j[0]>= 0 and line + j[0]<= self.N - 1) and ( column + j[1]>= 0 and column + j[1]<= self.N - 1 ):
                    general_pole[line + j[0]][column + j[1]].around_mines +=1
        return general_pole

    def open_fields(self, line, column):
        massiv = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        if self.pole[line][column].fl_open == False:
            self.pole[line][column].fl_open = True
            self.counter += 1
        for j in massiv:
            if (line + j[0] >= 0 and line + j[0] <= self.N - 1) and (column + j[1] >= 0 and column + j[1] <= self.N - 1) and self.pole[line + j[0]][column + j[1]].fl_open == False:
                self.pole[line + j[0]][column + j[1]].fl_open = True
                self.counter +=1
        return

    def init(self):
        general_pole = [[Cell(0, 0) for i in range(0, self.N)] for i in range(0, self.N)]
        position_of_mines = self.generate_min(general_pole)
        return position_of_mines

    def show(self,line=0,column=0,lose = False):
        if self.first_attempt:
            for line_ in range(0, self.N):
                print(' '.join(['#' for column_ in range(0,self.N)]))
            self.first_attempt = False
        else:
            for line_ in range(0, self.N):
                for column_ in range(0, self.N):
                    if line_ == line and column_ == column and lose==True:
                        print('@',end=' ',sep='')
                    elif self.pole[line_][column_].fl_open == True and self.pole[line_][column_].mine==True:
                        print('*',end=' ',sep='')
                    elif self.pole[line_][column_].fl_open == True and self.pole[line_][column_].mine==False:
                        print('0',end=' ',sep='')
                    else:
                        print('#',end=' ',sep='')
                print('\n')
        return
    def gameplay(self):
        lose = False
        self.first_attempt = True
        self.show()
        while lose == False:
            if self.counter == (self.N) ** 2:
                print('Победа!')
                lose = True
                return
            print('Введите координаты:')
            print('столбик=',end=' ')
            column = int(input())
            print('строчка=', end=' ')
            line = int(input())
            if line < 0 or line >= self.N or column < 0 or column >= self.N:
                print('Указанные координаты за пределами поля')
            elif self.pole[line][column].mine == True:
                lose = True
                self.show(line, column, lose)
                print('Игра проиграна')
            else:
                self.open_fields(line,column)
                self.show(line, column)

N = 4
M = 13
pole_game = GamePole(N, M)
pole_game.gameplay()
