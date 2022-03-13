from collections import defaultdict

class segmento:
    def __init__(self):
        while True:
          self.tabla = defaultdict(list)
    
    def limite(self, u, v):
        self.graph[u].append(v)
 
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
 
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
 