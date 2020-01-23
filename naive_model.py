import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import split
from numpy import array
from sklearn.metrics import mean_squared_error
from math import sqrt

def read_csv(filename):
    data = pd.read_csv(filename,infer_datetime_format=True,
                        index_col=['datetime'])
    data.index = pd.to_datetime(data.index)
    return data

def train_test_split(data):
    #     splitting the data 80/20
    data = data[:-24]
    train_size = int(0.8*data.shape[0])
    test_size = int(0.2*data.shape[0])
    train, test = data[:train_size], data[-test_size:]
    train = array(split(train, len(train)/24))
    test = array(split(test, len(test)/24))
#     returning an array of data in shape (days, hours, variables)
    return train, test

def daily_persistence(history):
#     empty list for values
    values = list()
#     last_day is history -1
    last_day = history[-1]
#     now need hourly predictions so need to create a list of numbers -1, -24
# also need to reverse the list because the last value is the last hour
    numbers = [i for i in range(1,25)]
    for i in numbers:
        value = last_day[-i, 0]
        values.append(value)
    return values[::-1]

def weekly_persistence(history):
#     -7 gets the value from last week
    last_week = history[-7]
#     gets the value of global active power for all rows
    return last_week[:, 0]

def weekly_oya_persistence(history):
#     this gets the value from 364 days ago i.e. 52 weeks ago
    last_week = history[-364]
#     gets the value of global active power for all rows
    return last_week[:, 0]

def evaluate_model(model_func, train, test):
    # history is a list of weekly data
    history = [x for x in train]
    # walk-forward validation over each week
    predictions = list()
    for i in range(len(test)):
        # predict the week
        yhat_sequence = model_func(history)
        # store the predictions
        predictions.append(yhat_sequence)
        # get real observation and add to history for predicting the next week
        history.append(test[i, :])
    predictions = array(predictions)
    # evaluate predictions days for each week
    score, scores = evaluate_forecasts(test[:, :, 0], predictions)
    return score, scores

def summarize_scores(name, score, scores):
    s_scores = ', '.join(['%.1f' % s for s in scores])
    print('%s: [%.3f] %s' % (name, score, s_scores))
    
def evaluate_forecasts(actual, predicted):
    scores = list()
    # calculate an RMSE score for each day
    for i in range(actual.shape[1]):
        # calculate mse
        mse = mean_squared_error(actual[:, i], predicted[:, i])
        # calculate rmse
        rmse = sqrt(mse)
        # store
        scores.append(rmse)
    # calculate overall RMSE
    s = 0
    for row in range(actual.shape[0]):
        for col in range(actual.shape[1]):
            s += (actual[row, col] - predicted[row, col])**2
    score = sqrt(s / (actual.shape[0] * actual.shape[1]))
    return score, scores

def scores_and_visualisations(model_dict, train, test):
    hours = ["%.2d:00" % x for x in range(0,24)]

    plt.figure(figsize=(16, 9))
    for name, func in model_dict.items():
        # evaluate and get scores
        score, scores = evaluate_model(func, train, test)
        # summarize scores
        summarize_scores(name, score, scores)
        # plot scores
        plt.plot(hours, scores, marker='o', label=name)
        plt.ylabel('Global Active Power')
        plt.legend()