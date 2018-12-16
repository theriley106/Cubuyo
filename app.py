from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import scramble
import csv
import os
DB_FILE = "static/database.csv"
app = Flask(__name__, static_url_path='/static')
SCRAMBLES = []




@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/genNew', methods=['GET'])
def newScramble():
	scrambleVal = str(scramble.genNew(25))
	SCRAMBLES.append(scrambleVal)
	return scrambleVal

@app.route("/complete/<timeVal>")
def submitTime(timeVal):
	scrambleVal = SCRAMBLES.pop(-1)
	try:
		timeVal = float(timeVal.replace("E", "."))
	except:
		timeVal = 0.0
	if (os.path.exists(DB_FILE) == False):
		writeType = 'w'
	else:
		writeType = 'a'
	with open(DB_FILE,writeType) as fd:
		writer = csv.writer(fd)
		writer.writerow([scrambleVal, timeVal])
	return ""

if __name__ == '__main__':
	SCRAMBLES.append("Test")
	submitTime("45E31423")
	app.run(host='127.0.0.1', port=5000)
