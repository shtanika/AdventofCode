# PART ONE
'''
def findGamma2 (str):
    num0 = 0
    num1 = 0
    for s in str:
        if(s =="0"):
            num0 +=1
        else:
            num1+=1
    if(num0 > num1):
        return 0
    return 1

def findEpsilon (str):
    num0 = 0
    num1 = 0
    for s in str:
        if(s =="0"):
            num0 +=1
        else:
            num1+=1
    if(num0 > num1):
        return 1
    return 0

def findGamma (str):
    lst0 = [i for i, letter in enumerate(str) if letter == "0"]
    lst1 = [i for i, letter in enumerate(str) if letter == "1"]
    return (0 if len(lst0)>len(lst1) else 1)
'''

def findGammaAndEpsilon(str):
    lst0 = [i for i, letter in enumerate(str) if letter == "0"]
    lst1 = [i for i, letter in enumerate(str) if letter == "1"]
    return (0 if len(lst0)>len(lst1) else 1), (1 if len(lst0)>len(lst1) else 0)


input = open("2021/inputs/3.txt")
gamma = ""
epsilon = ""
col = ""
lst = []


for line in input:
    stripped = line.strip()
    lst.append(stripped)

for i in range (len(stripped)):
    for j in lst:
        col += j[i]
    gamma+= str(findGammaAndEpsilon(col)[0])
    epsilon += str(findGammaAndEpsilon(col)[1])        
    col = ""

input.close()
gamma = int(gamma,2)  
epsilon = int(epsilon,2) 
 
print(f"\ngamma: {gamma} and epsilon: {epsilon}\nMultiplied: {int(gamma)*int(epsilon)}\n")


#PART TWO

def findRating(lst, gamma, pos):
    lst = [x for x in lst if gamma in x[pos]]
    return lst


input = open("2021/inputs/3.txt")
lst = []
temp = []

for line in input:
    stripped = line.strip()
    lst.append(stripped)

temp = lst
for i in range (len(stripped)):
    for j in temp:
        col += j[i]
    gamma = str(findGammaAndEpsilon(col)[0])
    epsilon = str(findGammaAndEpsilon(col)[1])
    col = ""

    if(len(temp)>1):
        temp = findRating(temp, gamma, i)
    oxy = int(temp[0],2)

   
temp = lst
for i in range (len(stripped)):
    for j in temp:
        col += j[i]
    epsilon = str(findGammaAndEpsilon(col)[1])
    col = ""

    if(len(temp)>1):
        temp = findRating(temp, epsilon, i)

    co2 = int(temp[0],2)    


input.close()
   
print(f"\noxy: {oxy} and co2: {co2}\nMultiplied: {int(oxy)*int(co2)}")