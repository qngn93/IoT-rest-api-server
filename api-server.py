from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
import datetime
app = Flask(__name__)


@app.route("/")
def main():
	now = datetime.datatime.now()
	return now.strftime("%Y-%m-%d %H:%M")

@app.route("/lock")
def lock():


@app.route("/unlock")
def unlock():


@app.route("/open")
def open():


@app.route("/close")
def close():

@app.route("/")
def getOpenStatus():
	

@app.route("/")
def getLockStatus():



if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 8080, debug = True)