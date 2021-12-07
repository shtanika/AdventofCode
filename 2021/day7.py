import statistics
import numpy as np

# PART ONE
input = open("2021/inputs/7.txt")
positions = list(map(int,input.readline().split(",")))

# get median
pos = int(statistics.median(positions))

# get total of all numbers subracted by median
total = sum([abs(i-pos) for i in positions])
print(f"PART ONE\ntotal fuel: {total}\n")

# PART TWO
def getFuel(num):
    total = 0
    for i in range(num+1):
        total += i
    return total

def findPos(positions):
    fuels = {}

    for pos in range(min(positions),max(positions)+1):
        fuel = 0
        for i in positions:
            fuel += getFuel(abs(i-pos))
        fuels[pos] = fuel

    #print(fuels)
    pos = min(fuels, key=fuels.get)
    totalTwo = fuels[pos]
    return totalTwo, pos

pos = int(statistics.mean(positions))

totalTwo = sum([getFuel(abs(i-pos)) for i in positions])
print(f"PART TWO\ntotal fuel: {totalTwo}")