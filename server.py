from flask import Flask, render_template, send_from_directory, request, make_response, session
from flask_sock import Sock
from components.user_database import getUser, createUser, getUserBySessionToken, sendChatMessage, getRooms, getRoom
import json

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)

if __name__ == "__main__":
	app.run(debug=True)