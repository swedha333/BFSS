'''Depth First Search uses STACK AND RECURSION
'''
#import defaultdict
from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        #TYPE UR CODE HERE
            dfs(graph,neighbour,visited,path)
            visited[neighbour]=True
    return path
graph=defaultdict(list)
n,e=map(int,input().split())
for i in range(e):
    #TYPE UR CODE HERE
#print(graph)
start='A'
visited=defaultdict(bool)
path=[]
traversedpath=#TYPE UR CODE HERE
print(traversedpath)
