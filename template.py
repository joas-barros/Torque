from abc import ABC, abstractmethod

class SuperficieDeControle(ABC):
    @abstractmethod
    def calcularForca(self):
        return self.forca
    
    @abstractmethod
    def calcularDistancia(self):
        return self.distencia
    
    def calcularTorque(self):
        return self.calcularForca() * self.calcularDistancia()