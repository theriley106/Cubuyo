from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import scramble

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/genNew', methods=['GET'])
def newScramble():
	return str(scramble.genNew(25))

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
