from flask import Flask
from flask_cors import CORS, cross_origin
import serial

PORT="/dev/ttyUSB1"

OPEN=b'O'
CLOSE=b'C'
STATUS=b'S'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

status = {'opened': False}

sp = serial.Serial(PORT, 115200, timeout=1)

@app.route("/")
@cross_origin()
def root():
    return status

@app.route("/open")
@cross_origin()
def open():
    # open
    sp.write(OPEN)
    status['opened'] = True
    return status

@app.route("/close")
@cross_origin()
def close():
    # open
    sp.write(CLOSE)
    status['opened'] = False
    return status
