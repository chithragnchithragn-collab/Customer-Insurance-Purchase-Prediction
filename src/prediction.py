import pickle
import numpy as np
import pandas as pd
#Loas the saved model
with open('random_forest_model.pkl', 'rb') as file:
    model_rf = pickle.load(file)
#Load the saved scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
#Get customer input for prediction
age = float(input("Enter age: "))
salary = float(input("Enter salary: "))
#Prepare input
customer_input = pd.DataFrame([[age, salary]], columns=['Age', 'EstimatedSalary'])
#Scale the input
customer_scaled = scaler.transform(customer_input)
#Predict
prediction = model_rf.predict(customer_scaled)
if prediction[0] == 1:
    print("The customer is likely to purchase insurance.")
else:
    print("The customer is unlikely to purchase insurance.")