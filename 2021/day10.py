import numpy as np
import statistics

input = open("2021/inputs/10.txt")
lines=[l.strip() for l in input]

def removePairs(lines):
    for i in range(len(lines)):
        before = len(lines[i])
        after = ""
        while before!=after:
            lines[i] = lines[i].replace("()","").replace("[]","").replace("{}","").replace("<>","")
            after = before
            before = len(lines[i])
    return lines

def findIncorrect(line,points):
    vals = [3,57,1197,25137]
    idxs=[]
    
    idxs.append(line.find(')'))
    idxs.append(line.find(']'))
    idxs.append(line.find('}'))
    idxs.append(line.find('>'))

    if(max(idxs)>0):
        idxs = [i if i!=-1 else max(idxs)+1 for i in idxs]
        points += vals[np.argmin(idxs)]
    return points

def removeCorrupted(lines):
    incomplete=[]
    for line in lines:
        if(line.find(')')==-1 and line.find(']')==-1 and line.find('}')==-1 and line.find('>')==-1):
            incomplete.append(line)
    return incomplete

def getScore(line):
    score=0
    line = line[::-1]
    for i in line:
        if(i=='('):
            score = score*5+1
        elif(i=='['):
            score = score*5+2
        elif(i=='{'):
            score = score*5+3
        elif(i=='<'):
            score = score*5+4
    return score

# PART ONE
lines = removePairs(lines)
points = 0
for line in lines:
    points = findIncorrect(line,points)
print(f"PART ONE\nTotal syntax error score: {points}\n")

# PART TWO
lines = removeCorrupted(lines)
scores = []
for line in lines:
    score = getScore(line)
    scores.append(score)
print(f"PART TWO\nMiddle score: {statistics.median(scores)}")