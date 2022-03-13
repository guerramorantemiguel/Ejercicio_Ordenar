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