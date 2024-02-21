import json
import pandas as pd


# Importing input data from json file
def import_input_data():
    with open('inputs.json') as f:
        data = json.load(f)
    return data

# Torque functions
def Aileron_monoplane(inputs):
    area = inputs['aileron']['base'] * inputs['aileron']['height']

    xCentroid = inputs['aileron']['base'] / 2
    yCentroid = inputs['aileron']['height'] / 2

    Cc = inputs['aileron']['height']

    force = (area / inputs['aileron']['wingArea']) * inputs['aileron']['maxLoadFactor'] * inputs['aileron']['weight']

    distance = Cc * 100 / 2

    return force * distance


def Aileron_biplane(inputs):
    return Aileron_monoplane(inputs) / 2


def Elevator(inputs):
    horizontalEmpenageLoading = 2 * inputs['elevator']['horizontalEmpennageLoad'] / (inputs['elevator']['chordHorizontalEmpennage'] * 9.81)
    elevatorLoading = horizontalEmpenageLoading * inputs['elevator']['chordElevator'] / inputs['elevator']['chordHorizontalEmpennage']

    force = elevatorLoading * inputs['elevator']['chordElevator'] / 2

    distance = inputs['elevator']['chordElevator'] * 100 / 3

    return force * distance


def Rudder(inputs):
    verticalEmpenageArea = inputs['rudder']['verticalEmpennageBase'] * inputs['rudder']['height']
    rudderArea = inputs['rudder']['rudderBase'] * inputs['rudder']['height']

    rudderPercentage = rudderArea / verticalEmpenageArea

    force = rudderPercentage * inputs['rudder']['verticalEmpennageLoadUnderBurst'] / 9.81

    distance = inputs['rudder']['rudderBase'] * 100 / 2

    return force * distance

# Organizing results in a pandas dataframe
def commandTorquesMonoplane():
    inputs = import_input_data()

    aileron = Aileron_monoplane(inputs)
    elevator = Elevator(inputs)
    rudder = Rudder(inputs)

    results = {
        'Aileron': [aileron],
        'Elevator': [elevator],
        'Rudder': [rudder]
    }

    return pd.DataFrame(results)

def commandTorquesBiplane():
    inputs = import_input_data()

    aileron = Aileron_biplane(inputs)
    elevator = Elevator(inputs)
    rudder = Rudder(inputs)

    results = {
        'Aileron': [aileron],
        'Elevator': [elevator],
        'Rudder': [rudder]
    }

    return pd.DataFrame(results)


# Exporting results to a json file
def outputsJson(df):
    df.to_json('torques.json', orient="records")

# Exporting results to a csv file
def outputsCsv(df):
    df.to_csv('torques.csv', index=False)