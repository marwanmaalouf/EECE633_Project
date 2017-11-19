# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:23:10 2017

@author: Marwan
"""

## TODOS:
## 1. Read the data from the file
## 2. Rename Columns
## 3. Clean and spit time dependant columns

## Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re




def cleanData(data):
    data[['Appointment_ScheduledDate']] = data.Appointment_ScheduledDate.apply(np.datetime64)
    data['Appointment_ScheduledDate_Year'] = data.Appointment_ScheduledDate.apply(lambda x: x.year)
    data['Appointment_ScheduledDate_Month'] = data.Appointment_ScheduledDate.apply(lambda x: x.month)
    data['Appointment_ScheduledDate_Date'] = data.Appointment_ScheduledDate.apply(lambda x: x.day)
    data['Appointment_ScheduledDate_Hour'] = data.Appointment_ScheduledDate.apply(lambda x: x.hour)
    data['Appointment_ScheduledDate_Minute'] = data.Appointment_ScheduledDate.apply(lambda x: x.minute)
    data['Appointment_ScheduledDate_Second'] = data.Appointment_ScheduledDate.apply(lambda x: x.second)

    
    data[['Appointment_Date']] = data.Appointment_Date.apply(np.datetime64)
    data['Appointment_Date_Year'] = data.Appointment_Date.apply(lambda x: x.year)
    data['Appointment_Date_Month'] = data.Appointment_Date.apply(lambda x: x.month)
    data['Appointment_Date_Day'] = data.Appointment_Date.apply(lambda x: x.day)
    data = data.apply(cleanTimeStamps, axis= 1)
    print(data.head())

    

## main
filename = './Missed_Appointment.csv'
raw_columns = ['Patient_ID', 'Appointment_ID', 
    'Patient_Gender', 'Appointment_ScheduledDate',
    'Appointment_Date', 'Patient_Age', 
    'Patient_Neighbourhood', 'Patient_Scholarship',
    'Patient_Hypertension', 'Patient_Diabetes',
    'Patient_Alcoholism', 'Patient_Handicap',
    'SMS_Received', 'No_Show']

raw_data = pd.read_csv(filename)
raw_data.columns = raw_columns
raw_data.info()
print(raw_data.head())
cleanData(raw_data)
