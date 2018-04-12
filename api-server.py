from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from time import sleep
import os
import datetime

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
	23 : {'open' : 'GPIO 23', 'state' : GPIO.LOW},
	24 : {'lock' : 'GPIO 24', 'state' : GPIO.LOW}
}

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)


@app.route("/")
def main():
	now = datetime.datatime.now()
	return now.strftime("%Y-%m-%d %H:%M")

@app.route("/lock")
def lock():
	GPIO.output(lock, GPIO.HIGH)

@app.route("/unlock")
def unlock():
	GPIO.output(lock, GPIO.LOW)

@app.route("/open")
def open():
	GPIO.output(open, GPIO.HIGH)

@app.route("/close")
def close():
	GPIO.out(open, GPIO.LOW)


@app.route("/getOpenStatus")
def OpenStatus():


@app.route("/getLockedStatus")
def LockStatus():



if __name__ == "__main__":
	try:
		app.run(host = '0.0.0.0', port = 8080, debug = True)
	except:
		pass