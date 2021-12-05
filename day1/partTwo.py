#PART TWO: CHECK EACH TRIO OF NUMBERS (INCLUSIVE) IF LARGER THAN LAST TRIO
input = open("C:/Users/shama/adventofcode/day1/input.txt")
values = []
trios = []
i = 0
j = 0
larger = 0


for line in input:
    stripped = line.strip()

    values.append(int(stripped))

    if(i>1):
        trios.append(values[i]+values[i-1]+values[i-2])

        if(trios[j]>trios[j-1] and len(trios)>1):
            larger+=1
        
        j+=1

    i+=1
    #print(trios)
    #print(larger)

input.close()
print(larger)