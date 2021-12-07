# PART ONE: CHECK DEPTH INCREASE + HORIZONTAL INCREASE
input = open("2021/inputs/2.txt")
direction = []
horizontal = 0
vertical = 0
aim = 0


for line in input:
    stripped = line.strip()
    direction = stripped.split()

    if (direction[0] == "forward"):
        horizontal += int(direction[1])
    
    elif (direction[0] == "up"):
        vertical -= int(direction[1])
    
    else:
        vertical += int(direction[1])

input.close()    
print(f"PART ONE\nThe horizontal position is {horizontal}. The depth is {vertical}.")
print(f"Multiplied they are {horizontal*vertical}.")

# PART ONE: CHECK DEPTH INCREASE + HORIZONTAL INCREASE WITH AIM VALUE    
input = open("2021/inputs/2.txt")
horizontal = 0
vertical = 0

for line in input:
    stripped = line.strip()
    direction = stripped.split()

    if (direction[0] == "forward"):
        horizontal += int(direction[1])
        vertical += int(direction[1]) * aim
    
    elif (direction[0] == "up"):
        aim -= int(direction[1])
    
    else:
        aim += int(direction[1])
    
input.close()    

print(f"\nPART TWO\nThe horizontal position is {horizontal}. The depth is {vertical}.")
print(f"Multiplied they are {horizontal*vertical}.")