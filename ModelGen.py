from __future__ import print_function


from pyspark import SparkContext
# $example on$
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
# $example off$

if __name__ == "__main__":

    sc = SparkContext(appName="Model")

    # $example on$
    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.replace(',', ' ').split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile("BAC.csv")
    parsedData = data.map(parsePoint)

    # Build the model
    model = LinearRegressionWithSGD.train(parsedData, iterations=5, step=0.1)

    sameModel = LinearRegressionModel.load(sc, "BAC")
