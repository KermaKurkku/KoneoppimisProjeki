# !/usr/bin/python
# coding=utf-8

import numpy as np

from sklearn.neural_network import MLPRegressor
from sklearn import linear_model, gaussian_process
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import project_modules.csv_reader as csv_reader
import project_modules.utils as utils
from joblib import dump, load
from matplotlib import pyplot as plt

from sklearn.gaussian_process.kernels import RBF, WhiteKernel

lista = [
    [0.]
    , [0.01]
    , [0.02]
    , [0.03]
    , [0.04]
    , [0.05]
    , [0.06]
    , [0.07]
    , [0.08]
    , [0.09]
    , [0.1]
    , [0.11]
    , [0.12]
    , [0.13]
    , [0.14]
    , [0.15]
    , [0.16]
    , [0.17]
    , [0.18]
    , [0.19]
    , [0.2]
    , [0.21]
    , [0.22]
    , [0.23]
    , [1.]
    , [1.1]
    , [1.02]
    , [1.03]
    , [1.04]
    , [1.05]
    , [1.06]
    , [1.07]
    , [1.08]
    , [1.09]
    , [1.1]
    , [1.11]
    , [1.12]
    , [1.13]
    , [1.14]
    , [1.15]
    , [1.16]
    , [1.17]
    , [1.18]
    , [1.19]
    , [1.2]
    , [1.21]
    , [1.22]
    , [1.23]
    , [2.]
    , [2.01]
    , [2.02]
    , [2.03]
    , [2.04]
    , [2.05]
    , [2.06]
    , [2.07]
    , [2.08]
    , [2.09]
    , [2.1]
    , [2.11]
    , [2.12]
    , [2.13]
    , [2.14]
    , [2.15]
    , [2.16]
    , [2.17]
    , [2.18]
    , [2.19]
    , [2.2]
    , [2.21]
    , [2.22]
    , [2.23]
    , [3.]
    , [3.01]
    , [3.02]
    , [3.03]
    , [3.04]
    , [3.05]
    , [3.06]
    , [3.07]
    , [3.08]
    , [3.09]
    , [3.1]
    , [3.11]
    , [3.12]
    , [3.13]
    , [3.14]
    , [3.15]
    , [3.16]
    , [3.17]
    , [3.18]
    , [3.19]
    , [3.2]
    , [3.21]
    , [3.22]
    , [3.23]
    , [4.]
    , [4.01]
    , [4.02]
    , [4.03]
    , [4.04]
    , [4.05]
    , [4.06]
    , [4.07]
    , [4.08]
    , [4.09]
    , [4.1]
    , [4.11]
    , [4.12]
    , [4.13]
    , [4.14]
    , [4.15]
    , [4.16]
    , [4.17]
    , [4.18]
    , [4.19]
    , [4.2]
    , [4.21]
    , [4.22]
    , [4.23]
    , [5.]
    , [5.01]
    , [5.02]
    , [5.03]
    , [5.04]
    , [5.05]
    , [5.06]
    , [5.07]
    , [5.08]
    , [5.09]
    , [5.1]
    , [5.11]
    , [5.12]
    , [5.13]
    , [5.14]
    , [5.15]
    , [5.16]
    , [5.17]
    , [5.18]
    , [5.19]
    , [5.2]
    , [5.21]
    , [5.22]
    , [5.23]
    , [6.]
    , [6.01]
    , [6.02]
    , [6.03]
    , [6.04]
    , [6.05]
    , [6.06]
    , [6.07]
    , [6.08]
    , [6.09]
    , [6.1]
    , [6.11]
    , [6.12]
    , [6.13]
    , [6.14]
    , [6.15]
    , [6.16]
    , [6.17]
    , [6.18]
    , [6.19]
    , [6.2]
    , [6.21]
    , [6.22]
    , [6.23]]

# Kokeilemalla saatu
kernel = 1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(
    noise_level=1e-5, noise_level_bounds=(1e-10, 1e5)
)
regr = gaussian_process.GaussianProcessRegressor(kernel=kernel, alpha=0.0)

global data_X
global data_y
global data_X_train
global data_X_test
global data_y_train
global data_y_test

global data_y_pred


def set_data(data):
    global data_X
    global data_y
    data_X = np.array(list(data.keys())).reshape((-1, 1))
    data_y = np.array(list(data.values()))


def split_data():
    global data_X
    global data_y
    global data_X_train
    global data_X_test
    global data_y_train
    global data_y_test
    data_X_train = data_X  # [:-int((len(data_X) * 0.7))]
    data_X_test = data_X  # [-int((len(data_X) * 0.3)):]
    data_y_train = data_y  # [:-int((len(data_X) * 0.7))]
    data_y_test = data_y  # [-int((len(data_X) * 0.3)):]


def train():
    global regr
    regr.fit(data_X_train, data_y_train)


def validate_model():
    return {'score': regr.score(data_X_test, data_y_test),
            'cross val score': cross_val_score(regr, data_X_train, data_y_train, cv=5).mean(),
            'cross val st deviation': cross_val_score(regr, data_X_train, data_y_train, cv=5).std()}


def predict():
    global data_y_pred
    # print(data_X_test)
    data_y_pred = regr.predict(data_X_test)


def do_predict(day):
    # print(day)
    return regr.predict(day)


def get_coef():
    global regr
    return regr.coef_


def get_intercept():
    global regr
    return regr.intercept_


def get_prediction_coef():
    global data_y_test
    global data_y_pred
    return r2_score(data_y_test, data_y_pred)


def get_r2score():
    global data_X_train
    global data_y_train
    return r2_score(data_X_train, data_y_train)


def save_model(station_id):
    to_save = {'regr': regr,
               'data_X_test': data_X_test,
               'data_y_test': data_y_test,
               'data_X_train': data_X_train,
               'data_y_train': data_y_train}
    filename = 'models/station' + station_id + '_model.joblib.gz'
    dump(to_save, filename, compress='gzip')


def load_model(station_id):
    global regr
    global data_X_train
    global data_y_train
    global data_X_test
    global data_y_test
    filename = 'models/station' + station_id + '_model.joblib.gz'
    try:
        loaded = load(filename)
        regr = loaded['regr']
        data_X_train = loaded['data_X_train']
        data_y_train = loaded['data_y_train']
        data_X_test = loaded['data_X_test']
        data_y_test = loaded['data_y_test']
    except FileNotFoundError:
        print("mallia ei l??ytynyt")
        return -1


def plot_outputs(station):
    plt.clf()
    toinen_lista = list(range(len(data_y_pred)))
    plt.scatter(toinen_lista, data_y_test, color="red", label="Todelliset m????r??t")
    plt.plot(toinen_lista, data_y_pred, color="blue", linewidth=3, label="Ennuste")
    if len(toinen_lista[::24]) == 7:
        plt.xticks(toinen_lista[::24], ['MA','TI','KE','TO','PE','LA','SU'])
    plt.yticks()
    plt.xlabel('P??iv??')
    plt.ylabel('Py??rien m????r??')
    plt.title(station)
    plt.legend()
    filename = 'plots/' + station + '_plot.png'
    plt.savefig(filename)
