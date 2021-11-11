from collections import defaultdict
 
class Graph:
 
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print (s, end = " ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(1, 7)
g.addEdge(7, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(2, 5)
g.addEdge(5, 2)
g.addEdge(3, 5)
g.addEdge(5, 3)
g.addEdge(3, 4)
g.addEdge(4, 3)
g.addEdge(4, 6)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(6, 5)
g.addEdge(6, 10)
g.addEdge(10, 6)
g.addEdge(7, 11)
g.addEdge(11, 7)
g.addEdge(7, 19)
g.addEdge(19, 7)
g.addEdge(5, 8)
g.addEdge(8, 5)
g.addEdge(8, 9)
g.addEdge(9, 8)
g.addEdge(8, 11)
g.addEdge(11, 8)
g.addEdge(9, 12)
g.addEdge(12, 9)
g.addEdge(9, 13)
g.addEdge(13, 9)
g.addEdge(10, 18)
g.addEdge(18, 10)
g.addEdge(10, 23)
g.addEdge(23, 10)
g.addEdge(11, 12)
g.addEdge(12, 11)
g.addEdge(11, 14)
g.addEdge(14, 11)
g.addEdge(12, 15)
g.addEdge(15, 12)
g.addEdge(12, 16)
g.addEdge(16, 12)
g.addEdge(13, 17)
g.addEdge(17, 13)
g.addEdge(13, 18)
g.addEdge(18, 13)
g.addEdge(14, 15)
g.addEdge(15, 14)
g.addEdge(14, 19)
g.addEdge(19, 14)
g.addEdge(14, 20)
g.addEdge(20, 14)
g.addEdge(15, 16)
g.addEdge(16, 15)
g.addEdge(15, 21)
g.addEdge(21, 15)
g.addEdge(16, 21)
g.addEdge(21, 16)
g.addEdge(16, 17)
g.addEdge(17, 16)
g.addEdge(17, 18)
g.addEdge(18, 17)
g.addEdge(17, 22)
g.addEdge(22, 17)
g.addEdge(18, 23)
g.addEdge(23, 18)
g.addEdge(19, 20)
g.addEdge(20, 19)
g.addEdge(19, 25)
g.addEdge(25, 19)
g.addEdge(20, 21)
g.addEdge(21, 20)
g.addEdge(20, 26)
g.addEdge(26, 20)
g.addEdge(21, 22)
g.addEdge(22, 21)
g.addEdge(21, 24)
g.addEdge(24, 21)
g.addEdge(21, 27)
g.addEdge(27, 21)
g.addEdge(22, 23)
g.addEdge(23, 22)
g.addEdge(22, 24)
g.addEdge(24, 22)
g.addEdge(24, 28)
g.addEdge(28, 24)
g.addEdge(25, 26)
g.addEdge(26, 25)
g.addEdge(26, 27)
g.addEdge(27, 26)
g.addEdge(27, 28)
g.addEdge(28, 27)

g.BFS(1)
 