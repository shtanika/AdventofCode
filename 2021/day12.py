# make adjacency list ?
from collections import defaultdict

input = open("2021/inputs/ex12.txt")
connections=[tuple(l.strip().split("-")) for l in input]
print(connections)

