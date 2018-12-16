from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import scramble
import csv
import os
import random

DB_FILE = "static/{0}.csv"
app = Flask(__name__, static_url_path='/static')
SCRAMBLES = {}

def newSession():
	return "".join([str(random.randint(1,10)) for i in range(10)])

@app.route('/', methods=['GET'])
def index():
	sessionID = newSession()
	return redirect(url_for('mySession', sessionID=sessionID))

@app.route('/session/<sessionID>', methods=['GET'])
def mySession(sessionID):
	if (os.path.exists(DB_FILE.format(sessionID)) == False):
		with open(DB_FILE.format(sessionID),'a') as fd:
			writer = csv.writer(fd)
			writer.writerow(["Scramble", "Time"])
	return render_template("index.html")

@app.route('/genNew/<sessionID>', methods=['GET'])
def newScramble(sessionID):
	scrambleVal = str(scramble.genNew(25))
	if sessionID not in SCRAMBLES:
		SCRAMBLES[sessionID] = []
	SCRAMBLES[sessionID].append(scrambleVal)
	return scrambleVal

@app.route("/complete/<sessionID>/<timeVal>")
def submitTime(sessionID, timeVal):
	try:
		scrambleVal = SCRAMBLES[sessionID].pop(-1)
		timeVal = float(timeVal.replace("E", "."))
		with open(DB_FILE.format(sessionID),'a') as fd:
			writer = csv.writer(fd)
			writer.writerow([scrambleVal, timeVal])
	except:
		pass
	return ""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
