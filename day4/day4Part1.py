from os import error
import numpy as np
from  itertools import chain

from numpy.core.numeric import indices

# Counts number of lines without anything to get num of boards
with open('day4/input.txt') as f:
    f.readline()
    f.readline()
    numBoards = sum(line.isspace() for line in f)
f.close()


input = open("day4/input.txt")

# Gets list of numbers
numbers = list(map(int,input.readline().split(",")))

# Gets one board from input
def read_board(input):
    input.readline()
    board = []

    for _ in range(5):
        board.append(list(map(int,filter(lambda str: str != '', input.readline().strip().split(" ")))))
    return board

# Makes board of bools from board
def makeBool(board):
    npboard = np.array(board)
    boolBoard = (npboard == -1)
    return boolBoard

# Finds index of value
def index_2d(board, n):
    for i, x in enumerate(board):
        if n in x:
            return (i, x.index(n))

# Checks if any rows or columns have only True vals
def winner(boolBoard):
    # rows
    for i in range(len(boolBoard[0])):
        if(all(boolBoard[i])):
            return True
    #transpose to check columns   
    transpose = [list(i) for i in zip(*boolBoard)]
    for i in range(len(transpose[0])):
        if(all(transpose[i])):
            return True     
    return False

def anyWinners(boolBoards):
    for boolBoard in boolBoards:
        if(winner(boolBoard)):
            return True
    return False

def countWinners(boolBoards):
    n = 0
    for boolBoard in boolBoards:
        if(winner(boolBoard)):
            n+=1
    return n


def changeVals(boards, boolBoards, num):
    i=0
    for board in boards:
        if(num in chain(*board)):
            idx = index_2d(board, num)
            boolBoards[i][idx[0]][idx[1]] = True

        if(winner(boolBoards[i])):
            #print(f"\nWinner is {board} \n {boolBoards[i]} at index {i} with num {num}")
            #winningBoard = board
            #winningBoolBoard = boolBoards[i]
            #lastNum = num
            boards[0] = board
            boolBoards[0] = boolBoards[i]
            return boards, boolBoards, num 
            #break
        i+=1
    return boards, boolBoards, num

def changeVals2(boards, boolBoards, winningBoards, num):
    i=0
    for board in boards:
        if(num in chain(*board)):
            idx = index_2d(board, num)
            boolBoards[i][idx[0]][idx[1]] = True

        if(winner(boolBoards[i])):
            winningBoards.append(board)
        i+=1
    return boards, boolBoards, winningBoards, num


def sumUnmarked(board, boolBoard):
    res=0
    indices = [list(i) for i in zip(*np.where(boolBoard == False))]
    board = np.array(board)
    indices = np.array(indices)

    for i in range(len(indices)):
        res += board[tuple(indices[i])].sum(axis=0)
    #sum = board[tuple(indices.T) + (slice(None),)].sum(0)

    return res


# Create board of boards and corresponding bool board
i=0
boards = []
boolBoards = []
while True:
    board = read_board(input)
    boolBoard = makeBool(board)

    boards.append(board)
    boolBoards.append(boolBoard)
    if(i==numBoards):
        break

    i+=1

#boolBoards[0][1] = [not elem for elem in boolBoards[0][1]]
#bs = checkBoards(boards, boolBoards, 3)
#print(bs)
winningBoards = []

#MAIN METHOD FOR TESTING ALL NUMS

for num in numbers:
    if(not anyWinners(boolBoards)):
        boards, boolBoards, n = changeVals(boards, boolBoards, num)
    else:
        break

res = sumUnmarked(boards[0], boolBoards[0])
print(f"sum of unmarked: {res} \nmultiplied by last num: {res*n}")

#PART TWO: FIND LAST ONE
'''
k = 0
for num in numbers:
    # boards, boolBoards = checkBoards(boards, boolBoards, num)
    #if(countWinners(boolBoards)<numBoards):
    #    boards, boolBoards, n, idx = changeVals2(boards, boolBoards, num, idx)
    if(len(winningBoards)<numBoards):
        boards, boolBoards, winningBoards, n = changeVals2(boards, boolBoards, winningBoards, num)

    winningBoards = list(set(winningBoards))

    k+=1
    print(f"index {k} and num {num}")

#board = boards[0]      
#boolBoard = boolBoards[0]
#board, boolBoard, n = lastVals(board, boolBoard, num)
print(f"\n{boards}\nnum: {n}")

#print(f"\n{boards}\n{boolBoards}\n")
res = sumUnmarked(boards[0], boolBoards[0])
print(f"sum of unmarked: {res} \nmultiplied by last num: {res*n}")
'''