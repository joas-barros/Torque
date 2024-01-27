from template import SuperficieDeControle

class Aileron(SuperficieDeControle):
    def __init__(self, areaDaAsa, nmax, w, b, h):
        self.areaDaAsa = areaDaAsa
        self.nmax = nmax
        self.w = w
        self.b = b
        self.h = h
        self.areaAileron = self.b * self.h
        self.centroideX = self.b / 2
        self.centroideY = self.h / 2
        self.Cc = self.h

    def calcularForca(self):
        self.forca = (self.areaAileron / self.areaDaAsa) * self.nmax * self.w
        return self.forca
    
    def calcularDistancia(self):
        self.distancia = self.Cc * 100 / 2
        return self.distancia
    
