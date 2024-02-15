from runManual import run_manual, exibirtitulo
from runJson import run_json
from os import system

exibirtitulo()
escolha = int(input("""
Escolha a configuração da aeronave:
[1] - Monoplano
[2] - Biplano
"""))

if escolha == 1:
    config = "monoplano"
else:
    config = "biplano"

exibirtitulo()
escolha = int(input("""
Escolha o modo de entrada:
[1] - Manual
[2] - Json
"""))

system("cls")

if escolha == 1:
    run_manual(config)
else:
    run_json(config)