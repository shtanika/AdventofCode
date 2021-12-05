import numpy as np

# Class variables: x1, y1, x2, y2
# Class functions: getMaxX, getMaxY, isHorizontal, isVertical, getLength
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

    def isHorizontal(self):
        if(self.y1==self.y2):
            return True
        return False

    def isVertical(self):
        if(self.x1==self.x2):
            return True
        return False

    # ONLY WORKS IF LINE IS HORIZONTAL OR VERTICAL
    def getLength(self):
        if(self.x1==self.x2):
            return abs(self.y2-self.y1)
        return abs(self.x2-self.x1)


with open("day5/example.txt") as f:
    lines = f.readlines()

# Make all lines into Line object only if horizontal or vertical lines
rawLines = list(line.rstrip('\n') for line in lines)
allLines = [Line(line) for line in rawLines if (Line(line).isHorizontal() or Line(line).isVertical())]

# Get maximum values of x and y to create diagram
maxX = max(l.getMaxX() for l in allLines)
maxY = max(l.getMaxY() for l in allLines)

# Create and populate diagram
diagram = [[0 for x in range(maxX)] for y in range(maxY)]
# print(np.array(diagram))


