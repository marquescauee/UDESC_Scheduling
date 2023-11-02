from abc import ABC, abstractmethod

class ConstraintHard(ABC):
    def __init__(self, cumprido):
        self.cumprido = cumprido
    
    def getCumprido(self):
        return self.cumprido
    
    def setCumprido(self, cumprido):
        self.cumprido = cumprido

class DiasNaoMinistradasHard(ConstraintHard):
    def __init__(self, cumprido, diasNaoMinistradasHard):
        super().__init__(cumprido)
        self.diasNaoMinistradasHard = diasNaoMinistradasHard
    
    def getDiasNaoMinistradas(self):
        return self.diasNaoMinistradasHard
    
    def setDiasNaoMinistradas(self, diasNaoMinistradasHard):
        self.diasNaoMinistradasHard = diasNaoMinistradasHard

class DeveSerNoiteCheiaHard(ConstraintHard):
    def __init__(self, cumprido, deveSerNoiteCheiaHard):
        super().__init__(cumprido)
        self.deveSerNoiteCheiaHard = deveSerNoiteCheiaHard
    
    def getDeveSerNoiteCheia(self):
        return self.deveSerNoiteCheiaHard
    
    def setDeveSerNoiteCheia(self, deveSerNoiteCheiaHard):
        self.deveSerNoiteCheiaHard = deveSerNoiteCheiaHard


##Softs

from abc import ABC, abstractmethod

class ConstraintSoft(ABC):
    def __init__(self, cumprido, peso):
        self.cumprido = cumprido
        self.peso = peso
    
    def getCumprido(self):
        return self.cumprido
    
    def setCumprido(self, cumprido):
        self.cumprido = cumprido
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso

class DiasNaoMinistradasSoft(ConstraintSoft):
    def __init__(self, cumprido, diasNaoMinistradas, peso):
        super().__init__(cumprido, peso)
        self.diasNaoMinistradas = diasNaoMinistradas
    
    def getDiasNaoMinistradas(self):
        return self.diasNaoMinistradas
    
    def setDiasNaoMinistradas(self, diasNaoMinistradas):
        self.diasNaoMinistradas = diasNaoMinistradas

class DeveSerNoiteCheiaSoft(ConstraintSoft):
    def __init__(self, cumprido, deveSerNoiteCheia, peso):
        super().__init__(cumprido, peso)
        self.deveSerNoiteCheia = deveSerNoiteCheia
    
    def getDeveSerNoiteCheia(self):
        return self.deveSerNoiteCheia
    
    def setDeveSerNoiteCheia(self, deveSerNoiteCheia):
        self.deveSerNoiteCheia = deveSerNoiteCheia
