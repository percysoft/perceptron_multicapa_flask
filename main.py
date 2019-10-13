from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json()
    modelfile = './final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    x_question = pd.read_csv('./x_question.csv')
    prediction = model.predict(x_question);
    print(prediction);
    return jsonify({'class_id': 'hola', 'class_name': prediction[0]})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)