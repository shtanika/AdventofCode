# PART ONE
input = open("day6/example.txt")
timers = list(map(int,input.readline().split(",")))
print(timers)

days = 80

for i in range(days):
    numZeros = timers.count(0)
    timers = [i-1 if i!=0 else 6 for i in timers]
    timers += numZeros * [8]


print(f"{days}: {len(timers)}")

# PART TWO
# Need to figure out a more efficient method for this
