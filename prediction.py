"""
Linear Regression With SGD Example.
"""
from __future__ import print_function


from pyspark import SparkContext
import NewsAPI
import numpy as np
# $example on$
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
# $example off$

import time
import datetime

def CustomPredict(date_start, date_end, company):

    sc = SparkContext(appName="ModelPredict")


    api = NewsAPI.NewsAPI(date_start.month,date_start.day,date_start.year,date_end.month,date_end.day,date_end.year, company,'56283d7d6075b9d30773e1ceb440e1b2d029f438')

    sameModel = LinearRegressionModel.load(sc, "/"+company)

    l = api.getSentimentScore()

    mean_sent = np.mean(l)

    return model.predict([mean_sent])

'''
    # $example on$
    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.replace(',', ' ').split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile("data/mllib/ridge-data/lpsa.data")
    parsedData = data.map(parsePoint)
#    parsedData = [LabeledPoint(1, [1]), LabeledPoint(2, [2]), LabeledPoint(3, [3]), LabeledPoint(4, [4]), LabeledPoint(5, [5])]
    # Build the model
    model = LinearRegressionWithSGD.train(sc.parallelize(parsedData), iterations=5, step=0.1)

    # Evaluate the model on training data
#    valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
#    MSE = valuesAndPreds \
#        .map(lambda (v, p): (v - p)**2) \
#        .reduce(lambda x, y: x + y) / valuesAndPreds.count()
#    print("Mean Squared Error = " + str(MSE))
    print("prediction\n\n\n\n")
    print("prediction with .5 is " + str(model.predict([.5])) + "\n\n\n\n\n")
    print("prediction with -.2 is " + str(model.predict([-.2])) + "\n\n\n\n\n")
    # Save and load model
    model.save(sc, "target/tmp/lin_test3")
#    sameModel = LinearRegressionModel.load(sc, "target/tmp/lin_test2")
    # $example off$
'''