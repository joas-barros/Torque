from aileron import Aileron

class AileronBiplano(Aileron):
    def __init__(self, areaDaAsa, nmax, w, b, h):
        super().__init__(areaDaAsa, nmax, w, b, h)
        
    def calcularTorque(self):
       return (self.calcularForca() * self.calcularDistancia()) / 2
