"""
Linear Regression With SGD Example.
"""
from __future__ import print_function


from pyspark import SparkContext
import NewsAPI
import numpy as np
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

import time
import datetime

def CustomPredict(date_start, date_end, company):

# create spark context
    sc = SparkContext(appName="Model")
# create an api object
    api = NewsAPI.NewsAPI(date_start.month,date_start.day,date_start.year,date_end.month,date_end.day,date_end.year, company,'56283d7d6075b9d30773e1ceb440e1b2d029f438')
# load the prediction model for the company
    model = LinearRegressionModel.load(sc, company)
# getting data for the duration of time specified
    api.startGetData()
# get the sentiment average of the days
    l = api.getSentimentScore()
    mean_sent = np.mean(l)
    print ("\n\n\n\n\n" + str(mean_sent) + "\n\n\n\n\n")
# make the prediction using the loaded model
    pred = model.predict([mean_sent])
    print ("\n\n\n\n\n" + str(pred) + "\n\n\n\n\n")
# close the spark context
    sc.stop()
# return
    return pred

