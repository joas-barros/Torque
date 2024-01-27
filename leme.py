from template import SuperficieDeControle

class Leme(SuperficieDeControle):
    def __init__(self, bEV, bLeme, h, la2):
        self.bEV = bEV
        self.bLeme = bLeme
        self.h = h
        self.areaEV = bEV * h
        self.areaLeme = bLeme * h
        self.la2 = la2
        self.porcentagemLeme = self.calcularPorcentagemLeme()
    
    def calcularPorcentagemLeme(self):
        self.porcentagemLeme = self.areaLeme / self.areaEV
        return self.porcentagemLeme    

    def calcularForca(self):
        self.forca = self.porcentagemLeme * self.la2 / 9.81
        return self.forca
    
    def calcularDistancia(self):
        self.distancia = self.bLeme * 100 / 2
        return self.distancia
    
