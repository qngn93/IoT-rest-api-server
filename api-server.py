from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from time import sleep
import os
import datetime

from camera_pi import Camera

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

#storing pins and states in dict
pins = {
	23 : {'open' : 'GPIO 23', 'state' : GPIO.LOW},
	24 : {'lock' : 'GPIO 24', 'state' : GPIO.LOW}
}

#setting each pin as an output
#setting default at low
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

#default time set
@app.route("/")
def main():
	now = datetime.datatime.now()
	return now.strftime("%Y-%m-%d %H:%M")

def gen(camera):
	#video streaming function
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    #route to videostream
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

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
def openStatus():


@app.route("/getLockedStatus")
def lockStatus():



if __name__ == "__main__":
	try:
		app.run(host = '0.0.0.0', port = 8080, debug = True)
	except:
		pass