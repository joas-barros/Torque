from template import SuperficieDeControle

class Profundor(SuperficieDeControle):
    def __init__(self, ch, pTotal, ce):
        self.ch = ch
        self.pTotal = pTotal
        self.ce = ce
        self.carregamentoEH = self.calcularCarregamentoEH()
        self.carregamentoProfundor = self.calcularCarregamentoProfundor()
    
    def calcularCarregamentoEH(self):
        self.carregamentoEH = 2 * self.pTotal / (self.ch * 9.81)
        return self.carregamentoEH 

    def calcularCarregamentoProfundor(self):
        self.carregamentoProfundor = self.calcularCarregamentoEH() * self.ce / self.ch
        return self.carregamentoProfundor  

    def calcularForca(self):
        self.forca = self.calcularCarregamentoProfundor() * self.ce / 2
        return self.forca
    
    def calcularDistancia(self):
        self.distancia = self.ce * 100 / 3
        return self.distancia
    
