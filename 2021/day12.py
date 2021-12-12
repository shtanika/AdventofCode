# make adjacency list and use dfs 
from collections import defaultdict

def getAdjacencyList(connections):
    adjList = defaultdict(set)
    for connection in connections:
        try:
            adjList[connection[0]].add(connection[1])
        except KeyError:
            adjList[connection[0]] = {connection[1]}
        try:
            adjList[connection[1]].add(connection[0])
        except KeyError:
            adjList[connection[1]] = {connection[0]}
    return adjList


input = open("2021/inputs/ex12.txt")
connections=[tuple(l.strip().split("-")) for l in input]

adjList = getAdjacencyList(connections)

for cave in adjList:
    print([cave][-1])
    print(f"{adjList[cave]}\n")

p = ['start'][-1]
print(p)