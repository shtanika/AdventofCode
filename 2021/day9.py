import numpy as np

def checkAdjacent(heightMap):
    lowPoints = []
    for i in range(len(heightMap)):
        for j in range(len(heightMap[0])):
            # top of map
            if(i==0):
                # top left corner
                if(j==0):
                    if(heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j+1]):
                        lowPoints.append(heightMap[i][j])
                # top right corner
                elif(j==len(heightMap[0])-1):
                    if(heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j-1]):
                        lowPoints.append(heightMap[i][j])
                # rest of top 
                else:
                    if(heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j-1] and heightMap[i][j]<heightMap[i][j+1]):
                        lowPoints.append(heightMap[i][j])

            # bottom of map
            elif(i==len(heightMap)-1):
                # bottom left corner
                if(j==0):
                    if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i][j+1]):
                        lowPoints.append(heightMap[i][j])
                # bottom right corner
                elif(j==len(heightMap[0])-1):
                    if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i][j-1]):
                        lowPoints.append(heightMap[i][j])
                # rest of bottom
                else:
                    if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i][j-1] and heightMap[i][j]<heightMap[i][j+1]):
                        lowPoints.append(heightMap[i][j])

            # leftmost of map
            elif(j==0):
                if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j+1]):
                        lowPoints.append(heightMap[i][j])

            # rightmost of map
            elif(j==len(heightMap[0])-1):
                if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j-1]):
                        lowPoints.append(heightMap[i][j])

            # rest of board 
            else:
                # less than above, below, left, and right
                if(heightMap[i][j]<heightMap[i-1][j] and heightMap[i][j]<heightMap[i+1][j] and heightMap[i][j]<heightMap[i][j-1] and heightMap[i][j]<heightMap[i][j+1]):
                    lowPoints.append(heightMap[i][j])
    return lowPoints


# PART ONE 
# Counts number of lines 
with open('2021/inputs/ex9.txt') as f:
    numLines = sum(1 for line in f)
f.close()

input = open("2021/inputs/ex9.txt")

heightMap = []
for _ in range(numLines):
    heightMap.append(list(map(int,filter(lambda str: str != '', input.readline().strip()))))

# print(np.array(heightMap))

lows = checkAdjacent(heightMap)
lows = [i+1 for i in lows]
print(f"Sum of all low points: {sum(lows)}")
input.close()

# PART TWO 
# maybe make dictionary with indices as keys and low point as value?