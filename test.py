from time import sleep
from pynput import keyboard
import _thread


class PLAYER:
    __x = 0
    #y coordinate is always at the bottom of the screen

    def getX(self):
        return self.__x
    
    def move(self, move, max_x):
        position_change = 0
        for i in move:
            if i == 'r':
                position_change+=1
            elif i == 'l':
                position_change-=1
            if(position_change+self.__x<0): position_change+=1
            if(position_change+self.__x>=max_x): position_change-=1
        self.__x += position_change


class BOARD:
    __board = []
    __xsize = 0
    __ysize = 0
    def __init__(self, xsize, ysize):
        self.__xsize = xsize
        self.__ysize = ysize
        self.clearBoard()
    

    def clearBoard(self):
        self.__board.clear()
        for i in range(0,self.__ysize):
            self.__board.append([])
            for j in range(0,self.__xsize):
                self.__board[i].append("ff")
    
    
    def setPlayer(self, player_position):
        self.__board[self.__ysize-1][player_position] = "[]"
    

    def showBoard(self):
        for i in range(0,self.__ysize):
            for j in range(0,self.__xsize):
                print(self.__board[i][j], end="")
            print("\n", end="")
    

    def getXsize(self):
        return self.__xsize

        
player = PLAYER()
board = BOARD(10,10)

moves = ['llrrlrlrr', 'lrrrlrlrlrr','r','l','l','lrlrrr','rr','l']

for i in range(0,100):
    board.clearBoard()
    board.setPlayer(player.getX())
    board.showBoard()
    player.move(moves[min(i, len(moves)-1)], board.getXsize())
    sleep(.5)
#moves = 'rlllr' # this is a move stack which is being created between frames
#place = ["f","f","f","f","f","f","f","f","[]","f","f","f","f","f","f","f"] # this is temporary solution to show where the player is


"""def move(move, pos):
    position = pos
    lpos = position
    if move == 'r':
        position+=1
    else:
        position-=1
    tmp = place[lpos]
    place[lpos] = place[position]
    place[position] = tmp
    return position

def printPos():
    for i in place:
        print(i, end="")

position = 8

for i in moves:
    position = move(i, position)
    printPos()
    sleep(.1)
    print("")"""