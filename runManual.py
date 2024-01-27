from aileron import Aileron
from profundor import Profundor
from leme import Leme
import pandas as pd
from os import system

def exibirtitulo():
    system("cls")
    print("=======================================================")
    print("Cálculo do torque requerido nas superficies de controle")
    print("=======================================================")

exibirtitulo()
print("Inputs do Aileron:")
print("---------------------------")
areaDaAsa = float(input("Área da asa (m²): "))
nmax = float(input("Fator de carga máximo (Nmax): "))
w = float(input("Peso (Kg): "))
b = float(input("Base do aileron (m): "))
h = float(input("Altura do aileron (m): "))
aileron = Aileron(areaDaAsa, nmax, w, b, h)

exibirtitulo()
print("Inputs do Profundor:")
print("---------------------------")
ch = float(input("Corda da EH(m): "))
pTotal = float(input("Maior carga na EH(Kgf): "))
ce = float(input("Corda do profundor(m): "))
profundor = Profundor(ch, pTotal, ce)

exibirtitulo()
print("Inputs do Leme:")
print("---------------------------")
bEV = float(input("Base da EV(m): "))
bLeme = float(input("Base do leme(m): "))
h = float(input("Altura do leme(m): "))
la2 = float(input("Carga na EV sobre rajada(N): "))
leme = Leme(bEV, bLeme, h, la2)

exibirtitulo()
print("Outputs:")
print(f"Torque no aileron: {aileron.calcularTorque()} kgf.cm")
print(f"Torque no profundor: {profundor.calcularTorque()} kgf.cm")
print(f"Torque no leme: {leme.calcularTorque()} kgf.cm")
print("=======================================================")

outputs = pd.DataFrame({"Superficie de controle": ["Aileron", "Profundor", "Leme"],
                    "Torque (kgf.cm)": [aileron.calcularTorque(), profundor.calcularTorque(), leme.calcularTorque()]})

inputsAileron = pd.DataFrame(list(aileron.__dict__.items()), columns=["Aileron", "Inputs"])
inputsProfundor = pd.DataFrame(list(profundor.__dict__.items()), columns=["Profundor", "Inputs"])
inputsLeme = pd.DataFrame(list(leme.__dict__.items()), columns=["Leme", "Inputs"])

df_final = pd.concat([inputsAileron, inputsProfundor, inputsLeme, outputs], axis=1)

df_final.to_excel("detalhamento.xlsx", index=False)

outputs.to_json("torques.json", orient="records")

print("Gerado arquivo detalhamento.xlsx com os detalhes do cálculo")
print("Gerado arquivo torques.json com os valores dos torques")
