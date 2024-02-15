from aileron import Aileron
from aileronBiplano import AileronBiplano
from profundor import Profundor
from leme import Leme
import pandas as pd
import json

def run_json(config):
    with open("./inputs.json", "r") as f:
        inputs = json.load(f)

    if config == "monoplano":
        aileron = Aileron(inputs["aileron"]["areaDaAsa"], inputs["aileron"]["nMax"], inputs["aileron"]["peso"],
                        inputs["aileron"]["base"], inputs["aileron"]["altura"])
    else:
        aileron = AileronBiplano(inputs["aileron"]["areaDaAsa"], inputs["aileron"]["nMax"], inputs["aileron"]["peso"],
                                inputs["aileron"]["base"], inputs["aileron"]["altura"])

    profundor = Profundor(inputs["profundor"]["ch"], inputs["profundor"]["pTotal"], inputs["profundor"]["ce"])

    leme = Leme(inputs["leme"]["baseEV"], inputs["leme"]["baseLeme"], inputs["leme"]["altura"], inputs["leme"]["cargaEV"])

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