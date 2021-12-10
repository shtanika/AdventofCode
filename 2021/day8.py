from re import search

def flatten(lst):
    flat = []
    for sublist in lst:
        for elem in sublist:
            flat.append(elem)
    return flat

# digit = seq of letters
# s = mapping[i]
def hasString(digit, s):
    for i in range(len(s)):
        if(digit.find(s[i])==-1):
            return False
    return True

def checkUnique(digits):
    num = 0
    for i in digits:
        # if segement is equal to 1, 4, 7, or, 8
        if(len(i)==2 or len(i)==4 or len(i)==3 or len(i)==7):
            num += 1
    return num

def createMapping(inp):
    mapping=[""]*3
    for digit in inp:
        # if segment is equal to 1, 4, 7
        if len(digit)==2:
            mapping[0]=digit

        elif len(digit)==4:
            mapping[1]=digit

        elif len(digit)==3:
            mapping[2]=digit
    return mapping


def checkNums(output, mapping):
    nums=""
    for digit in output:
        # digits in 4 minus the digits in 1
        map5 = mapping[1].replace(mapping[0][0],"")
        map5 = map5.replace(mapping[0][1],"")

        # unique vals: 1, 4, 7, or, 8
        if len(digit)==2:
            nums += str(1)

        elif len(digit)==4:
            nums += str(4)

        elif len(digit)==3:
            nums += str(7)
        
        elif len(digit)==7:
            nums += str(8)

        # can be 2, 3, or 5
        # 3 has 1 (or 7) inside of it 
        # 5 has (4-1) inside of it 
        # else 2 
        elif len(digit)==5:
            if(hasString(digit,mapping[0])):
                nums += str(3)
            elif(hasString(digit,map5)):
                nums += str(5)
            else:
                nums += str(2)

        # can be 0, 6, or 9
        # 9 has 4 inside of it
        # 0 not 9 but 1 is inside of it
        # else 6
        elif len(digit)==6:
            if(hasString(digit,mapping[1])):
                nums += str(9)
            elif(hasString(digit,mapping[0])):
                nums += str(0)
            else:
                nums += str(6)
    return nums    


# PART ONE
input = open("2021/inputs/8.txt")

digits = list(line.rstrip('\n').split("| ",1)[1] for line in input)
digits = list(line.split(" ") for line in digits)
allDigits = flatten(digits)

print(f"PART ONE\nTotal instances of 1, 4, 7, or 8 in output: {checkUnique(allDigits)}\n")
input.close()

# PART TWO
input = open("2021/inputs/8.txt")
inputs = list(line.rstrip('\n').split("| ",1)[0] for line in input)
inputs = list(line.strip().split(" ") for line in inputs)

# loop to get every output number
outputs = []
for i in range (len(digits)):
    mapping = createMapping(inputs[i])
    n = checkNums(digits[i], mapping)
    outputs.append(int(n))

#print(outputs)

total = sum(outputs)

print(f"PART TWO\nSum of all output values: {total}\n")
input.close()
