from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Import the ridge model and scaler model
ridge_model = pickle.load(open('models/ridge_model.pkl', 'rb'))
scaler_mdoel = pickle.load(open('models/scaler_model.pkl', 'rb'))

# Predict Page
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data = scaler_mdoel.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data)

        return render_template('home.html', results=result[0])

    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")