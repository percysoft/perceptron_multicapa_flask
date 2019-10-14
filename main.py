from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json
import csv

app = Flask(__name__)

def calc_percentage(value,cant):
  return False

def prediction_percentage(question):
  detachment = question[5] +question[13] + question[21] + question[29] + question[31] + question[32] + question[36]
  humiliation = question[6] +question[14] + question[22] + question[30] + question[35] + question[39] + question[40]
  sex = question[1] +question[9] + question[17] + question[25] + question[33] + question[38]
  coercion = question[0] +question[8] + question[16] + question[24] + question[37] + question[41]
  physic = question[4] +question[12] + question[19] + question[20] + question[28]
  gender = question[2] +question[10] + question[18] + question[26] + question[34]
  punishment = question[7] +question[15] + question[23]
  instrument = question[3] +question[11] + question[27]
  result = {
      'detachment': {
        'detachment_sum': detachment,
        'detachment_percentage': detachment,
      },
      'humiliation': {
        'humiliation_sum': humiliation,
        'humiliation_percentage': humiliation,
      },
      'sex': {
        'sex_sum': sex,
        'sex_percentage': sex,
      },
      'coercion': {
        'coercion_sum': coercion,
        'coercion_percentage': coercion,
      },
      'physic': {
        'physic_sum': physic,
        'physic_percentage': physic,
      },
      'gender': {
        'gender_sum': gender,
        'gender_percentage': gender,
      },
      'punishment': {
        'punishment_sum': punishment,
        'punishment_percentage': punishment,
      },
      'instrument': {
        'instrument_sum': instrument,
        'instrument_percentage': instrument,
      },
    }
  return result

def prediction_value(value):
  if(value == 'si'):
    return True
  else:
    return False

def write_csv(name_csv,indiceQuestion,questions_points):
  with open(name_csv, mode='w') as prediction_file:
      prediction_writer = csv.writer(prediction_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      prediction_writer.writerow(indiceQuestion)
      prediction_writer.writerow(questions_points)

@app.route('/predict', methods=['POST'])
def predict():
    questions_points = request.json['questions_points']
    indiceQuestion = ['Col2','Col3','Col4','Col5','Col6','Col7','Col8','Col9','Col10','Col11','Col12','Col13','Col14','Col15','Col16','Col17','Col18','Col19','Col20','Col21','Col22','Col23','Col24','Col25','Col26','Col27','Col28','Col29','Col30','Col31','Col32','Col33','Col34','Col35','Col36','Col37','Col38','Col39','Col40','Col41','Col42','Col43']
    write_csv('question.csv',indiceQuestion,questions_points)
    modelfile = './final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    x_question = pd.read_csv('./question.csv')
    prediction = model.predict(x_question)
    percentage  = prediction_percentage(questions_points)

    return jsonify({
      'questions_points': questions_points,
      'prediction': prediction[0],
      'prediction_value': prediction_value(prediction[0]),
      'percentage': percentage
    })

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)