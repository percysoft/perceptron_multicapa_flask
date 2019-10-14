from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json
import csv

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json()
    indiceQuestion = ['Col2','Col3','Col4','Col5','Col6','Col7','Col8','Col9','Col10','Col11','Col12','Col13','Col14','Col15','Col16','Col17','Col18','Col19','Col20','Col21','Col22','Col23','Col24','Col25','Col26','Col27','Col28','Col29','Col30','Col31','Col32','Col33','Col34','Col35','Col36','Col37','Col38','Col39','Col40','Col41','Col42','Col43']
    arrayQuestion = [2,1,3,0,0,3,0,2,0,0,0,0,0,1,1,2,0,1,0,0,0,0,1,3,0,0,0,0,0,2,0,1,3,1,0,0,0,2,0,0,0,3]
    with open('question.csv', mode='w') as employee_file:
      employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      employee_writer.writerow(indiceQuestion)
      employee_writer.writerow(arrayQuestion)
    modelfile = './final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    x_question = pd.read_csv('./question.csv')
    prediction = model.predict(x_question);
    print(prediction);
    return jsonify({'class_id': 'hola', 'class_name': prediction[0]})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)