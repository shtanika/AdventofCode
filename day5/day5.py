import numpy as np

# Class variables: x1, y1, x2, y2
# Class functions: getMaxX, getMaxY, isHorizontal, isVertical
class Line():
    def __init__(self, l):
        self.x1 = int(l.split(",")[0].strip())
        self.y1 = int(l.split(",")[1].split("->")[0].strip())
        self.x2 = int(l.split(",")[1].split("->")[1].strip())
        self.y2 = int(l.split(",")[2].strip())

    def __repr__(self) -> str:
        return f"({self.x1},{self.y1}) -> ({self.x2},{self.y2})"

    def getMaxX(self):
        if(self.x1>self.x2):
            return self.x1
        return self.x2
    
    def getMaxY(self):
        if(self.y1>self.y2):
            return self.y1
        return self.y2

    # returns [x2, x1] if x1>x2 and [x1, x2] if x2>x1
    def getOrderedX(self):
        xs =[]
        if(self.x1>self.x2):
            xs.append(self.x2)
            xs.append(self.x1)
        else:
            xs.append(self.x1)
            xs.append(self.x2)
        return xs

    def getOrderedY(self):
        ys =[]
        if(self.y1>self.y2):
            ys.append(self.y2)
            ys.append(self.y1)
        else:
            ys.append(self.y1)
            ys.append(self.y2)
        return ys

    def isHorizontal(self):
        if(self.y1==self.y2):
            return True
        return False

    def isVertical(self):
        if(self.x1==self.x2):
            return True
        return False

    def is45(self):
        if(abs((self.y2-self.y1)/(self.x2-self.x1)) == 1):
            return True
        return False
        
# PART ONE
with open("day5/input.txt") as f:
    lines = f.readlines()

# Make all lines into Line object only if horizontal or vertical lines
rawLines = list(line.rstrip('\n') for line in lines)
allLines = [Line(line) for line in rawLines if (Line(line).isHorizontal() or Line(line).isVertical())]

# Get maximum values of x and y to create diagram
maxX = max(l.getMaxX() for l in allLines)
maxY = max(l.getMaxY() for l in allLines)

# Create and populate diagram
diagram = [[0 for x in range(maxX+1)] for y in range(maxY+1)]
diagram = np.array(diagram)

for i in range(len(allLines)):
    x1 = allLines[i].x1
    y1 = allLines[i].y1
    x2 = allLines[i].x2
    y2 = allLines[i].y2

    if(allLines[i].isHorizontal()):
        xs1 = allLines[i].getOrderedX()[0]
        xs2 = allLines[i].getOrderedX()[1]
        diagram[y1,xs1:(xs2+1)] += 1

    if(allLines[i].isVertical()):
        ys1 = allLines[i].getOrderedY()[0]
        ys2 = allLines[i].getOrderedY()[1]
        diagram[ys1:(ys2+1),x1] += 1

# diagram = np.array(diagram)
numPoints = np.count_nonzero(diagram>=2)
f.close()

print(f"PART ONE\nNumber of points >= 2: {numPoints}")



#PART TWO
with open("day5/input.txt") as f:
    lines = f.readlines()

# Make all lines into Line object only if horizontal, vertical line, or 45 degree  lines
rawLines = list(line.rstrip('\n') for line in lines)
allLines = [Line(line) for line in rawLines if (Line(line).isHorizontal() or Line(line).isVertical() or Line(line).is45())]

# Get maximum values of x and y to create diagram
maxX = max(l.getMaxX() for l in allLines)
maxY = max(l.getMaxY() for l in allLines)

# Create and populate diagram
diagram = [[0 for x in range(maxX+1)] for y in range(maxY+1)]
diagram = np.array(diagram)


for i in range(len(allLines)):
    length = allLines[i].getLength()
    x1 = allLines[i].x1
    y1 = allLines[i].y1
    x2 = allLines[i].x2
    y2 = allLines[i].y2

    if(allLines[i].isHorizontal()):
        xs1 = allLines[i].getOrderedX()[0]
        xs2 = allLines[i].getOrderedX()[1]
        diagram[y1,xs1:(xs2+1)] += 1

    elif(allLines[i].isVertical()):
        ys1 = allLines[i].getOrderedY()[0]
        ys2 = allLines[i].getOrderedY()[1]
        diagram[ys1:(ys2+1),x1] += 1
    
    elif(allLines[i].is45()):
        xs1 = allLines[i].getOrderedX()[0]
        xs2 = allLines[i].getOrderedX()[1]
        ys1 = allLines[i].getOrderedY()[0]
        ys2 = allLines[i].getOrderedY()[1]

        if(x1<x2 and y1>y2):
            for i in range(abs(x1-x2)+1):
                diagram[y1-i,x1+i] += 1
    
        elif(x1<x2 and y1<y2):
            for i in range(abs(x1-x2)+1):
                diagram[y1+i,x1+i] += 1

        elif(x1>x2 and y1>y2):
            for i in range(abs(x1-x2)+1):
                diagram[y1-i,x1-i] += 1

        elif(x1>x2 and y1<y2):
            for i in range(abs(x1-x2)+1):
                diagram[y1+i,x1-i] += 1
        

numPoints = np.count_nonzero(diagram>=2)
f.close()

# print(f"{diagram}\n")
print(f"\nPART TWO\nNumber of points >= 2: {numPoints}")