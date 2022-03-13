# Ejercicio_Ordenar

Este es el link del [repositorio]: https://github.com/guerramorantemiguel/Ejercicio_Ordenar.git

Ejercicio 4:
```
class ordenacion_dicotomica:
    def __init__(self):
        while True:
          self.tabla = lista(tabla)
          for i in range(len(self.tabla)):
            for j in range(i, len(self.tabla)):
              if self.tabla[j] < self.tabla[i]:
                 self.tabla[j], self.tabla[i] = self.tabla[i], self.tabla[j]
                print(self.tabla)
              
                return self, tabla
```
Ejercicio 5:
```
import random

class ordenacion_tareas:
    def __init__(self,tareas):
        self.tareas = defaultdict(tareas) 
        self.T = tareas
    def ordenacion_tareas(tareas):
      for j in range(len(tareas)):
        for r in range(j, len(tareas)):
          if self.T[r] > self.T[r+1]:
            self.T[r], self.T[r+1] = self.T[r+1], self.T[r]
            return self.T
```
Ejercicio 6:
```
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
```
