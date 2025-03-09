import cloudpickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

def predict_PHA(asteroid, pipe, le, sfs, rf):
    asteroid = pd.DataFrame(data=asteroid, index=[0])
    albedo = 0.0615
    asteroid["diametro"] = (1329/albedo)*np.power(10, -0.4*asteroid["H"])
    X_test = pipe.transform(asteroid)
    X_test = sfs.transform(X_test)
    pred = rf.predict(X_test)
    return le.inverse_transform(np.ravel(pred))[0]

with open('../model/HAP_model.bin', 'rb') as f_in:
    pipe, le, sfs, rf = cloudpickle.load(f_in)

app = Flask('PHA-asteroids')

@app.route('/predict', methods=['POST'])
def predict():
    asteroid = request.get_json()
    prediction = predict_PHA(asteroid, pipe, le, sfs, rf)
    result = {'PHA': str(prediction)}
    return jsonify(result)

@app.route('/')
def index():
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
    
##'H' 'i' 'om' 'w' 'ma' 'n' 'moid' 'class