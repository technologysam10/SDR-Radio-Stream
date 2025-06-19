import flask, os
import stream
from flask import Flask, send_from_directory 
app = Flask(__name__)

@app.route("/stream/<type>/<frequency>")
def streamRoute(type, frequency):
    if type == "fm":
        print("Opening FM stream: " + frequency)
        feed = stream.openFM(frequency)
        while True:
            chunk = feed.read(4096)
            return chunk
app.run(host="0.0.0.0", port=8234)
