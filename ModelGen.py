from __future__ import print_function


from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

if __name__ == "__main__":

    sc = SparkContext(appName="Model")

    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.replace(',', ' ').split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile("BAC.csv")
    parsedData = data.map(parsePoint)

    # Build the model
    model = LinearRegressionWithSGD.train(parsedData, iterations=5, step=0.1)
    #save the model
    model.save(sc, "../BAC")
