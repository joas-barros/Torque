# Guia de uso do programa

- Esse programa foi desenvolvido para auxiliar o subsistema de cargas e aeroelasticidade na obtenção dos valores de torque requeridos nos servos motores das seguintes superficies de controle : Aileron, profundor e leme.
- Para utilizar o programa, primeiro devemos baixar esse repositorio em sua máquina, voce pode fazer isso de diversas formas, mas uma bastante simples, se voce possui o git instalado em sua máquina, é abrindo uma pasta vazia e digitando o seguinte comando em seu prompt de comando:

```
git clone git@github.com:joas-barros/Torque.git
```
- Após baixar o repositorio voce poderá escolher um dos arquivos executaveis, no repositorio, existem dois arquivos dependendo de como voce quer entrar com os dados, o runManual.py e o runJson.py, iremos abordar cada um deles.

## runManual.py

- Esse é o programa que permite que os dados sejam passados para o programa de forma manual.
- Para executa-lo, basta abrir o repositorio em qualquer editor de código de sua preferência, como o VScode, abrir o terminar e digitar o seguinte comando:

```
python runManual.py
```
- Logo após será aberto uma interface para que sejá digitado os inputs para o cálculo.
- Primeiramente o usuário deve digitar os inputs do aileron:

<div>
    <p align="center">
        <img src="imagens\aileron.png" height="200" tittle="aileron"> 
    </p>
</div>

- Em seguida o usuário deve digitar os inputs para o calculo do torque no profundor:

<div>
    <p align="center">
        <img src="imagens\profundor.png" height="200" tittle="profundor"> 
    </p>
</div>

- Por fim, ele deve dá entrada aos dados da última superficie de controle, o  Leme:

<div>
    <p align="center">
        <img src="imagens\leme.png" height="200" tittle="leme"> 
    </p>
</div>

- Com isso, o programa é finalizado e os resultados são mostrados na tela:

<div>
    <p align="center">
        <img src="imagens\saida.png" height="200" tittle="saida"> 
    </p>
</div>

## runJson.py

- Nesse outro programa, os dados não são passados pelo usuario manualmente no console, eles são chamados a partir de um arquivo Json.
- O arquivo dever ser entitulado inputs.json, deve estar na mesma pasta que os arquivos python e deve ser estruturado da seguinte forma:

<div>
    <p align="center">
        <img src="imagens\json.png" height="400" tittle="json"> 
    </p>
</div>

- Voce pode acessa-lo atraves de qualquer editor de texto, como o bloco de notas e modificá-lo de acordo com sua necessidade.

- Após passar todos os inputs para o arquivo inputs.json, voce deve executar o programa atraves do seguinte comando no prompt: 

```
python runJson.py
```
- Em seguida será mostrado os resultados na tela assim como foi no primeiro programa:

<div>
    <p align="center">
        <img src="imagens\saidajson.png" height="200" tittle="saidajson"> 
    </p>
</div>

## Resultados

- Em ambos os programas o resultado obtidos é salvo além de ser mostrado na tela.

- Primeiramente uma planilha de excel é gerada entitulada detalhamento.xlsx onde é salvo, além dos valores de torque, todos os valores intermediarios calculados pelo programa.

<div>
    <p align="center">
        <img src="imagens\planilha.png" height="200" tittle="planilha"> 
    </p>
</div>

- Por fim, um arquivo json é gerado chamado torques.json contendo os valores de torque calculados que podem ser posteriormente utilizados pelo subsistema de elétrica para o dimensionamento dos servos motores.

<div>
    <p align="center">
        <img src="imagens\torques.png" height="100" tittle="torques"> 
    </p>
</div>