import argparse
from flask import Flask, render_template, request, Response, send_file, jsonify
import joblib
import os
import sys
sys.path.append('../templates')

import json
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Local source code
from transforms import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = '..'
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates') 
TEST_DATA = 'test_input.json'

app = Flask(__name__)

filepath = './.temp/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST', 'GET'])
def predict():  
    if request.method == 'GET':
        input_json = request.get_json()
        data = pd.read_json(input_json, orient='records')
        features = data.drop(columns='quality')
        
        # Pipeline transformation
        X = pipeline.transform(features)

        # Model prediction
        y_pred = model.predict(X)

        # Map
        if y_pred == 0:
            prediction = 'bad'
        elif y_pred == 1:
            prediction = 'good'


    return jsonify({'prediction': prediction})

@app.route('/api/test/predict', methods=['POST', 'GET'])
def predict_test():  
    pipeline = joblib.load(os.path.join('..', 'models', 'pipeline.pkl'))
    model = joblib.load(os.path.join('..', 'models', 'random_forest_1000est_2leaf_depth40.pkl'))
    data = read_test_data()
    features = data
    # Pipeline transformation
    X = pipeline.transform(features)
    # Model prediction
    y_pred = model.predict(X)
    # Map
    if y_pred == 0:
        prediction = 'bad'
    elif y_pred == 1:
        prediction = 'good'

    return jsonify({'prediction': prediction})


def read_test_data():
    return pd.read_json(TEST_DATA, orient='records')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=4567, type=int)
    parser.add_argument('--host', default='0.0.0.0', type=str)
    args = vars(parser.parse_args()) 

    # Load pipeline:
    pipeline = joblib.load(os.path.join('..', 'models', 'pipeline.pkl'))
    model = joblib.load(os.path.join('..', 'models', 'random_forest_1000est_2leaf_depth40.pkl'))

    app.run(host=args['host'], port=args['port'], debug=True)