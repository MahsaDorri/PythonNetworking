import time
import random
import json

# Start ID initially set to 111
start_id = 111

# Function to create and return a dictionary containing sample data
def create_data():
    global start_id
    
    # Increment start_id for each payload
    start_id += 1
    
    # Define sample data in a dictionary
    data = {
        'id': start_id,                                    #sequence number
        'patient': 'John Doe',                             #name of patient
        'time': time.asctime(),                            #time this was generated
        'heart_rate': int(random.gauss(80, 1)),            #heart rate
        'respiratory_rate': int(random.gauss(12,2)),       #respiratory rate
        'heart_rate_variability': 65,                      #???
        'body_temperature': random.gauss(99, 0.5),         #temperature
        'blood_pressure': {                                #subkey
            'systolic': int(random.gauss(105,2)),          #systolic pressure
            'diastolic': int(random.gauss(70,1))           #diastolic pressure
        },
        'activity': 'Walking'                              #activity
    }
    
    return data

# Function to print dictionary contents in a human-readable format
def print_data(data):
    print('ID:', data['id'])
    print('Patient:', data['patient'])
    print('Time:', data['time'])
    print('Heart Rate:', data['heart_rate'])
    print('Respiratory Rate:', data['respiratory_rate'])
    print('Heart Rate Variability:', data['heart_rate_variability'])
    print('Body Temperature:', data['body_temperature'])
    print('Blood Pressure:', data['blood_pressure'])
    print('Activity:', data['activity'])
    print()
