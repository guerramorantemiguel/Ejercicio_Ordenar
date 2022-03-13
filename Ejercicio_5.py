import random

class ordenacion_tareas:
    def __init__(self,tareas):
        self.tareas = defaultdict(tareas) 
        self.T = tareas
    def ordenacion_tareas(tareas):
      for j in range(len(tareas)):
        for r in range(j, len(tareas)):



  def ordenacion(self,tareas):
        for i in range(len(self.tareas)-1):
            for a in range(len(self.tareas)-1):
                if self.tareas[a] > self.tareas[a+1]:
                    self.tareas[a], self.tareas[a+1] = self.tareas[a+1], self.tareas[a]
        return self.