import json
import pandas as pd


# Importing input data from json file
def import_input_data():
    with open('input_data.json') as f:
        data = json.load(f)
    return data

# Torque functions
def aileron_monoplane(inputs):
    area = inputs['aileron']['base'] * inputs['aileron']['altura']

    xCentroid = inputs['aileron']['base'] / 2
    yCentroid = inputs['aileron']['altura'] / 2

    Cc = inputs['aileron']['altura']

    force = (area / inputs['asa']['areaDaAsa']) * inputs['asa']['nmax'] * inputs['peso']

    distance = Cc * 100 / 2

    return force * distance


def aileron_biplane(inputs):
    return aileron_monoplane(inputs) / 2


def elevator(inputs):
    horizontalEmpenageLoading = 2 * inputs['profundor']['pTotal'] / (inputs['profundor']['ch'] * 9.81)
    elevatorLoading = horizontalEmpenageLoading * inputs['profundor']['ce'] / inputs['profundor']['ch']

    force = elevatorLoading * inputs['profundor']['ce'] / 2

    distance = inputs['profundor']['ce'] * 100 / 3

    return force * distance


def rudder(inputs):
    verticalEmpenageArea = inputs['leme']['baseEV'] * inputs['leme']['h']
    rudderArea = inputs['leme']['baseLeme'] * inputs['leme']['h']

    rudderPercentage = rudderArea / verticalEmpenageArea

    force = rudderPercentage * inputs['leme']['cargaEV'] / 9.81

    distance = inputs['leme']['baseLeme'] * 100 / 2

    return force * distance

# Organizing results in a pandas dataframe
def commandTorquesMonoplane():
    inputs = import_input_data()

    aileron = aileron_monoplane(inputs)
    elevator = elevator(inputs)
    rudder = rudder(inputs)

    results = {
        'Torque in Aileron (kgf/cm)': [aileron],
        'Torque in Elevator (kgf/cm)': [elevator],
        'Torque in Rudder (kgf/cm)': [rudder]
    }

    return pd.DataFrame(results)

def commandTorquesBiplane():
    inputs = import_input_data()

    aileron = aileron_biplane(inputs)
    elevator = elevator(inputs)
    rudder = rudder(inputs)

    results = {
        'Torque in Aileron (kgf/cm)': [aileron],
        'Torque in Elevator (kgf/cm)': [elevator],
        'Torque in Rudder (kgf/cm)': [rudder]
    }

    return pd.DataFrame(results)


# Exporting results to a json file
def outputsJson(df):
    df.to_json('torques.json')

# Exporting results to a csv file
def outputsCsv(df):
    df.to_csv('torques.csv')