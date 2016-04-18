from flask import Flask
from flask import render_template
from flask import request
from datetime import *
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/api/prediction")
def getPrediction():
	start = request.args['start']
	end = request.args['end']
	company = request.args['company']

	startDate =  datetime.strptime(start, "%m/%d/%Y").date()
	endDate =  datetime.strptime(end, "%m/%d/%Y").date()

	return "True"

if __name__ == "__main__":
    app.run(debug=True)