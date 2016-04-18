from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/api/prediction")
def getPrediction():
	start = request.args['start']
	end = request.args['end']
	company = request.args['company']

	print start
	print end
	print company

	return "True"

if __name__ == "__main__":
    app.run(debug=True)