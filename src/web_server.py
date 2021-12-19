import pandas as pd
from flask import Flask
from flask import request
import json
import pickle

app = Flask(__name__)

with open('../models/rforestregressor.pkt', 'rb') as file:
    random_forest_regressor = pickle.load(file)

#тут пока только одна модель
models = [{"model_name":"random_forest_regressor"}]
#по идее стоит пробегаться по всем моделям в папке с помощью os.listdir

features_list = ['P1', 'P2', 'P3', 'P4',
       'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15',
       'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25',
       'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'P34', 'P35',
       'P36', 'P37']

@app.route("/", methods=['GET'])
def session_start():
    return 'session started'

@app.route("/api/show_models", methods=['GET'])
def show_models():

    models_list = json.dumps(models)
    return models_list

@app.route("/api/<model_to_use>/get_predict", methods=['POST'])
def predict(model=random_forest_regressor,
            features=features_list):

    data_to_predict = pd.read_json(request.data)[features_list]

    '''сюда кажется стоит добавить пайплайн обработки данных из json
        + добавить обработку ошибок,если пихаются лишние данные/если формат не валиден итж 
    '''

    model_prediction = model.predict(data_to_predict)

    prediction_json = json.dumps(model_prediction.to_list())

    return prediction_json


#app.run()


