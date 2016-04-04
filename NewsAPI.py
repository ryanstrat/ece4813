import requests
import time
import datetime

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

	def startGetData(self):
		start = datetime.date(self.ys,self.ms,self.ds)
		startunix = str(time.mktime(start.timetuple()))[0:10]

		end = datetime.date(self.ye,self.me,self.de)
		endunix = str(time.mktime(end.timetuple()))[0:10]

		url = 'https://access.alchemyapi.com/calls/data/GetNews?apikey=' + self.apikey + '&return=enriched.url.enrichedTitle.docSentiment&start=' + startunix + '&end=' + endunix + '&q.enriched.url.enrichedTitle.entities.entity=|text=' + self.company + ',type=company|&q.enriched.url.enrichedTitle.docSentiment.type=positive&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=finance&count=25&outputMode=json'

		self.raw = requests.get(url)

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
		return times

	def getSentiment(self):
		sentiment = []
		for sent in self.results:
			sentimentzzz = sent['source']['enriched']['url']['enrichedTitle']['docSentiment']['score']
			sentiment.append(sentimentzzz)
		return sentiment