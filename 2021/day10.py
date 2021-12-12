import numpy as np

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
        idxs = [i if i!=-1 else 99 for i in idxs]
        points += vals[np.argmin(idxs)]
    return points


# PART ONE
removePairs(lines)

points = 0
for line in lines:
    #print(f"{len(line)} {line}")
    points = findIncorrect(line,points)
print(f"PART ONE\nTotal syntax error score: {points}\n")

# PART TWO