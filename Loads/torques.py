import json
import pandas as pd


# Importing input data from json file
def import_input_data():
    with open('input_data.json') as f:
        data = json.load(f)
    return data

# Torque functions
def aileron_monoplane(inputs):
    area = inputs['aileron']['base'] * inputs['aileron']['height']

    xCentroid = inputs['aileron']['base'] / 2
    yCentroid = inputs['aileron']['height'] / 2

    Cc = inputs['aileron']['height']

    force = (area / inputs['aileron']['wingArea']) * inputs['aileron']['nmax'] * inputs['aileron']['weight']

    distance = Cc * 100 / 2

    return force * distance


def aileron_biplane(inputs):
    return aileron_monoplane(inputs) / 2


def elevator(inputs):
    horizontalEmpenageLoading = 2 * inputs['elevator']['horizontalEmpennageLoad'] / (inputs['elevator']['horizontalEmpennageChord'] * 9.81)
    elevatorLoading = horizontalEmpenageLoading * inputs['elevator']['elevatorChord'] / inputs['elevator']['horizontalEmpennageChord']

    force = elevatorLoading * inputs['elevator']['elevatorChord'] / 2

    distance = inputs['elevator']['elevatorChord'] * 100 / 3

    return force * distance


def rudder(inputs):
    verticalEmpenageArea = inputs['rudder']['verticalEmpennageBase'] * inputs['rudder']['height']
    rudderArea = inputs['rudder']['rudderBase'] * inputs['rudder']['height']

    rudderPercentage = rudderArea / verticalEmpenageArea

    force = rudderPercentage * inputs['rudder']['verticalEmpennageLoadUnderBurst'] / 9.81

    distance = inputs['rudder']['rudderBase'] * 100 / 2

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