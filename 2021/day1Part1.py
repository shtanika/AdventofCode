# PART ONE: CHECK IF PREVIOUS LINE IS LARGER THAN LAST LINE
input = open("2021/inputs/1.txt")
values = []
i = 0
larger = 0

for line in input:
    stripped = line.strip()

    values.append(int(stripped))
    #print(stripped)

    if(values[i]>values[i-1] and i!= 0):
        larger+=1

    i+=1

input.close()
print(larger)

