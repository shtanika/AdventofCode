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

# gets one path
def dfs(start,visited,adjList):
    path=[]
    stack=[]

    stack.append('start')
    visited['start'] = True
    cave=stack[0]
    print(start)

    while(cave!="end"):
        cave = stack.pop()
        path.append(cave)
        print(f"{cave} ")

        connections = adjList[cave]

        for i in connections:
            if(not visited[i]):
                stack.append(i)
                if(i.islower()):
                    visited[i] = True
    print(path)

def getPaths(node, end, visited, adjList, path, paths):
    if (node.islower()):
        visited.add(node)
    path.append(node)

    if node == end:
        paths.append(path.copy())
    else:
        for nxt in adjList[node]:
            if nxt not in visited:
                getPaths(nxt,end,visited,adjList,path,paths)
    path.pop()
    if node.islower():
        visited.remove(node)
    return paths

# PART ONE
input = open("2021/inputs/12.txt")
connections=[tuple(l.strip().split("-")) for l in input]
adjList = getAdjacencyList(connections)

visited = set()
paths=[]
path=[]
paths = getPaths('start','end',visited,adjList,path,paths)

print(f"Number of paths that visit small caves at most once: {len(paths)}")