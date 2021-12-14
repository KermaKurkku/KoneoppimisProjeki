# !/usr/bin/python
# coding=utf-8

import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import project_modules.csv_reader as csv_reader
import project_modules.utils as utils
from joblib import dump, load
from matplotlib import pyplot as plt

regr = linear_model.LinearRegression()
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
    data_X_train = data_X[:-int((len(data_X) * 0.7))]
    data_X_test = data_X[-int((len(data_X) * 0.3)):]
    data_y_train = data_y[:-int((len(data_X) * 0.7))]
    data_y_test = data_y[-int((len(data_X) * 0.3)):]


def train():
    global regr
    regr.fit(data_X_train, data_y_train)
    # print('score',regr.score(data_X_test, data_y_test))
    # print('Cross val score', cross_val_score(regr, data_X_train, data_y_train, cv=5))


def predict():
    global data_y_pred
    data_y_pred = regr.predict(data_X_test)

def do_predict(timestamp):
    return regr.predict(np.array(timestamp).reshape(1, -1))

# The intercept (B0)
# print('intercept:', regr.intercept_)
# The coefficients (B1)
# print("Coefficients: \n", regr.coef_)
# The mean squared error
# print("Mean squared error: %.2f" % mean_squared_error(data_y_test, data_y_pred))
# The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: %.2f" % r2_score(data_y_test, data_y_pred))


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
    global regr
    filename = 'models/station' + station_id + '_model.joblib'
    dump(regr, filename)


def load_model(station_id):
    global regr
    filename = 'models/station' + station_id + '_model.joblib'
    print(filename)
    regr = load(filename)


def plot_outputs(station):
    plt.plot(data_X_test, data_y_test, color="red", linewidth=2)
    plt.plot(data_X_test, data_y_pred, color="blue", linewidth=3)

    plt.xticks()
    plt.yticks()
    plt.xlabel('Aika')
    plt.ylabel('pyörien määrä')
    plt.title(station)
    plt.show()
