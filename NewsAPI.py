import requests
import time
import datetime
from yahoo_finance import Share
from pprint import pprint

class NewsAPI:
	def __init__(self,ms,ds,ys,me,de,ye,company,apikey):
		self.ms = ms
		self.ds = ds
		self.ys = ys

		self.me = me
		self.de = de
		self.ye = ye

		self.company = company
		self.apikey = apikey

		self.rawdata = ''
		self.rawjson = ''
		self.results = ''
		self.times = ''
		
	def startGetData(self):
		start = datetime.date(self.ys,self.ms,self.ds)
		startunix = str(time.mktime(start.timetuple()))[0:10]

		end = datetime.date(self.ye,self.me,self.de)
		endunix = str(time.mktime(end.timetuple()))[0:10]

		url = 'https://access.alchemyapi.com/calls/data/GetNews?apikey=' + self.apikey + '&return=enriched.url.enrichedTitle.docSentiment&start=' + startunix + '&end=' + endunix + '&q.enriched.url.enrichedTitle.entities.entity=|text=' + self.company + ',type=company|&q.enriched.url.enrichedTitle.docSentiment.type=positive&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=finance&count=25&outputMode=json'

		self.raw = requests.get(url)
	
		#I will change with for loop, so that we can have a set number of try to get the info given the response is taking long
		time.sleep(2)
		if self.raw.status_code == 200:
			self.rawjson = self.raw.json()
			self.results = self.rawjson['result']['docs']
			return 'success'
		else:
			return 'failed'

	def getTimeStamp(self):
		times = []
		for time in self.results:
				timeszzz = time['timestamp']
				times.append(timeszzz)
		self.times = times
		return times

	def getSentiment(self):
		sentiment = []
		for sent in self.results:
			sentimentzzz = sent['source']['enriched']['url']['enrichedTitle']['docSentiment']['score']
			sentiment.append(sentimentzzz)
		return sentiment
		
	 def getClosingPrice(self):
	 	shareName = Share(self.company)
	 	startDate=''
	 	endDate=''
	 	hist=''
	 	for t in self.times:
	 		startDate = str(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d'))
	 		endDate=startDate
	 		hist = shareName.get_historical(startDate, endDate)
	 		if(len(hist)==0):
	 			closingPrice = '0'
	 			closing.append(closingPrice)
	 		else:	
	 			closingPrice = hist[0]['Close']
	 			closing.append(closingPrice)
	 	return closingPrice
