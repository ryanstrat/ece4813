#1.  call the default constructor: variable = NewsAPI.NewsAPI(1,1,2015,3,1,2015,'GOOGLE','35b806d26e76f895fe31669dea30f528c36c94e6')
#2.  try to get data : variable.startGetData(), it will returns success if it is works or error (Check API key if it returns error)
#3.  get the sentiment score in list format double: variable.getSentiment()
#4.  get the Difference price percentage in list format double: variable.getDifferencePercentage(). For now, difference price will return 0 if the news date is on the weekend or holiday
#5.  install yahoo-finance API: pip install yahoo-finance
#6.  another API Key for Alchemy: 56283d7d6075b9d30773e1ceb440e1b2d029f438


#Verison 1.0: Only do the NewsAPI (Get only the sentimentscore and timestamp)
#Version 1.1: Get the stock price
#Version 1.2: Get the sentiment score and type

import requests
import time
import datetime
from yahoo_finance import Share
from pprint import pprint

class NewsAPI:
	#Default Constructor
	def __init__(self,ms,ds,ys,me,de,ye,company,apikey):
		#Start Date in int (Month, Day, Year)
		self.ms = ms
		self.ds = ds
		self.ys = ys
		#End Date in int (Month, Day, Year)
		self.me = me
		self.de = de
		self.ye = ye
		#Company Name and AlchemyAPI key
		self.company = company
		self.apikey = apikey
		#Results global variable
		self.rawdata = ''
		self.rawjson = ''
		self.results = ''
		self.times = ''
	#Try to get the data
	def startGetData(self):
		start = datetime.date(self.ys,self.ms,self.ds)
		startunix = str(time.mktime(start.timetuple()))[0:10]

		end = datetime.date(self.ye,self.me,self.de)
		endunix = str(time.mktime(end.timetuple()))[0:10]
		#Sent the API address
		url = 'https://access.alchemyapi.com/calls/data/GetNews?apikey=' + self.apikey + '&return=enriched.url.enrichedTitle.docSentiment&start=' + startunix + '&end=' + endunix + '&q.enriched.url.enrichedTitle.entities.entity=|text=' + self.company + ',type=company|&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=finance&count=200&outputMode=json'
		#Request the data
		self.raw = requests.get(url)
	
		#I will change with for loop, so that we can have a set number of try to get the info given the response is taking long
		
		while (self.raw.status_code != 200):
			sleep(1)
			
		self.rawjson = self.raw.json()
		
		if (self.rawjson['status'] == 'ERROR'):
			return 'Cannot Get the DATA'
		else:	
			self.results = self.rawjson['result']['docs']
			return 'success'


	def getTimeStamp(self):
		times = []
		for time in self.results:
				timeszzz = time['timestamp']
				times.append(timeszzz)
		self.times = times
		return times

	def getSentimentScore(self):
		sentiment = []
		for sent in self.results:
			sentimentzzz = sent['source']['enriched']['url']['enrichedTitle']['docSentiment']['score']
			sentiment.append(sentimentzzz)
		return sentiment

	def getSentimentType(self):
		sentiment = []
		for sent in self.results:
			sentimentzzz = sent['source']['enriched']['url']['enrichedTitle']['docSentiment']['type']
			sentiment.append(sentimentzzz)
		return sentiment
		
	def getDifferencePercentage(self):
	 	closing = []
	 	shareName = Share(self.company)
	 	# shareName = Share('AMZN')
	 	startDate=''
	 	endDate=''
	 	hist=''
	 	for t in self.times:
	 		todayTimeStamp = t
	 		yesterdayTimeStamp = t-86400
	 		startDate = str(datetime.datetime.fromtimestamp(todayTimeStamp).strftime('%Y-%m-%d'))
	 		yesterdayDate=str(datetime.datetime.fromtimestamp(yesterdayTimeStamp).strftime('%Y-%m-%d'))
	 		todayHist = shareName.get_historical(startDate, startDate)
	 		yesterdayHist = shareName.get_historical(yesterdayDate,yesterdayDate)
	 		while(len(todayHist)==0):
	 			todayTimeStamp = todayTimeStamp+86400
	 			startDate = str(datetime.datetime.fromtimestamp(todayTimeStamp).strftime('%Y-%m-%d'))
	 			todayHist = shareName.get_historical(startDate, startDate)
	 		
	 		while(len(yesterdayHist)==0):
	 			yesterdayTimeStamp= yesterdayTimeStamp-86400
				yesterdayDate=str(datetime.datetime.fromtimestamp(yesterdayTimeStamp).strftime('%Y-%m-%d'))
	 			yesterdayHist = shareName.get_historical(yesterdayDate,yesterdayDate)
	 			
	 		closingPriceToday = float(todayHist[0]['Close'])
	 		closingPriceYesterday = float(yesterdayHist[0]['Close'])
	 		difference = (float(closingPriceYesterday) - float(closingPriceToday))*100.0/float(closingPriceYesterday)
	 		diff2 = float(format(difference, '.3f'))
	 		
	 		closing.append(diff2)
	 	return closing
