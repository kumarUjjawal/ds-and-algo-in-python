# Breadth First Search

from collections import defaultdict

class Graph(object):
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
    
    # add a new edge to the graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        # mak all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        # create a queue for bfs
        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True




    # mark the sourc node as visited and enqueue it



