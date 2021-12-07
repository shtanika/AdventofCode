from collections import Counter

# PART ONE
input = open("day6/input.txt")
timers = list(map(int,input.readline().split(",")))

days = 80

for i in range(days):
    numZeros = timers.count(0)
    timers = [i-1 if i!=0 else 6 for i in timers]
    timers += numZeros * [8]

input.close()
#print(f"After {days} days: {len(timers)} lanternfish")

# PART TWO
# Make dictionary of each timer 

# decrement if not zero
# timers = [i-1 if i!=0 else 6 for i in timers]
def decrement(timers):
    for k in timers.keys():
        if (k!=0 and timers[k]!=0):
            timers[k-1] = timers[k]
            if (k!=9 and timers[k+1]==0):
                timers[k] -= timers[k]
            elif(k==9):
                timers[k] -= timers[k]    
    return timers

input = open("day6/input.txt")
timerList = list(map(int,input.readline().split(",")))
timers = {k:timerList.count(k) for k in range(10)}
#print(timers)

days = 256

for i in range(days):
    # increase 6 by amt of zeros 
    numZeros = timers[0]
    timers[7] += numZeros

    # increase 8 by amt of zeros
    timers[9] += numZeros
    #print(f"BEFORE DECREMENT    day {i+1}: {timers}")

    # reset zero to 0
    timers[0] = 0

    # decrement all nonzero values
    timers = decrement(timers)
    #print(f"AFTER DECREMENT     day {i+1}: {timers}\n")

del timers[9]
input.close()

print(f"final: {timers}\n")
print(f"After {days} days: {sum(timers.values())} lanternfish")