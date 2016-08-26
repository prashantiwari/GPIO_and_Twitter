import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

APP_KEY = 'TwjyVF0Elh2uAr8JNTQeJQdK6'
APP_SECRET = '5NUizxk8g8JaCjZuTHNakHXwdFpVy40OIXgDG1Vf8uQAnoQZOK'
OAUTH_TOKEN = '760761114334523392-yPZOICLEEinxjnDXDIAWMILPVyBn5qA'
OAUTH_TOKEN_SECRET = 'ujwt9LxRfmJ1oB24WW8lZGFmX6eUwuxPND46RdM9VGeJX'

TERMone = '#testing'
TERMtwo = '#testingagain'

LEDone = 22
LEDtwo = 11


class BlinkyStreamerone(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LEDone, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LEDone, GPIO.LOW)

class BlinkyStreamertwo(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LEDtwo, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LEDtwo, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LEDone, GPIO.OUT)
GPIO.output(LEDone, GPIO.LOW)

GPIO.setup(LEDtwo, GPIO.OUT)
GPIO.output(LEDtwo, GPIO.LOW)

# Create streamer
try:
        streamone = BlinkyStreamerone(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        streamone.statuses.filter(track=TERMone)
        
        streamtwo = BlinkyStreamertwo(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        streamtwo.statuses.filter(track=TERMtwo)
        
except KeyboardInterrupt:
        GPIO.cleanup()
