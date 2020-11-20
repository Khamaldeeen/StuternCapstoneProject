import os
from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import tensorflow as tf
from tensorflow import keras 
import requests
import numpy as np

app = Flask(__name__)
model = keras.models.load_model('myModel')

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        genders = request.form['genders']
        if genders == 'male':
            genders = np.array([0, 1])
        else:
            genders = np.array([1, 0])
        polyuria = request.form['polyuria']
        if polyuria == 'yes':
            polyuria = np.array([0, 1])
        else:
            polyuria = np.array([1, 0])
        polydipsia = request.form['polydipsia']
        if polydipsia == 'yes':
            polydipsia = np.array([0, 1])
        else:
            polydipsia = np.array([1, 0])
        s_weakness = request.form['s-weakness']
        if s_weakness == 'yes':
            s_weakness = np.array([0, 1])
        else:
            s_weakness = np.array([1, 0])
        weakness = request.form['weakness']
        if weakness == 'yes':
            weakness = np.array([0, 1])
        else:
            weakness = np.array([1, 0])
        polyphagia = request.form['polyphagia']
        if polyphagia == 'yes':
            polyphagia = np.array([0, 1])
        else:
            polyphagia = np.array([1, 0])
        genital = request.form['genital']
        if genital == 'yes':
            genital = np.array([0, 1])
        else:
            genital = np.array([1, 0])
        visual = request.form['visual']
        if visual == 'yes':
            visual = np.array([0, 1])
        else:
            visual = np.array([1, 0])
        itching = request.form['itching']
        if itching == 'yes':
            itching = np.array([0, 1])
        else:
            itching = np.array([1, 0])
        irritab = request.form['irritab']
        if irritab == 'yes':
            irritab = np.array([0, 1])
        else:
            irritab = np.array([1, 0])
        d_healing = request.form['d-healing']
        if d_healing == 'yes':
            d_healing = np.array([0, 1])
        else:
            d_healing = np.array([1, 0])
        paresis = request.form['paresis']
        if paresis == 'yes':
            paresis = np.array([0, 1])
        else:
            paresis = np.array([1, 0])
        s_muscle = request.form['s-muscle']
        if s_muscle == 'yes':
            s_muscle = np.array([0, 1])
        else:
            s_muscle = np.array([1, 0])
        alopecia = request.form['alopecia']
        if alopecia == 'yes':
            alopecia = np.array([0, 1])
        else:
            alopecia = np.array([1, 0])
        obesity = request.form['obesity']
        if obesity == 'yes':
            obesity = np.array([0, 1])
        else:
            obesity = np.array([1, 0])
        
        output = model.predict(np.array([np.concatenate((genders, polyuria, polydipsia, 
                                s_weakness, weakness, polyphagia, genital, visual, 
                                itching, irritab, d_healing, paresis, s_muscle, alopecia, obesity), axis=0)]))
        if output < 1:
            #output = output * 100
            return render_template('result.html', prediction = 'Negative')
        else:
            return render_template('result.html', prediction =  'Positive')
    else:
      return render_template('index.html')

@app.route('/')


def result():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)