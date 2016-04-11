import statistics

class DataManipulation:

	def __init__(timestamp, stockprice, sentimenttype, sentimentscore):

		self.timestamp = timestamp
		self.stockprice = stockprice
		self.sentimenttype = sentimenttype
		self.sentimentscore = sentimentscore


		#split the data

		#1. seperate the good, bad, and neutral

		#2. check if the article is for the next day (in case it outs before the market close or it is holiday) and add to the next following open market day

		#3. make the goodsentiment with score, timestamp, and stockprice

		#4. make the badsentiment with score, timestamp, and stockprice



	#function for linearize the sample data	
	def yearLinear(self):

		result = []
		return result


	#function for linearize the population data	
	def wholeLinear(self):

		result = []
		return result

	#function write to csv
	def writetocsv(self):
