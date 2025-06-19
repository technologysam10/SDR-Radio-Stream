import flask, os, stream
from flask import Flask, send_from_directory 
app = Flask(__name__)

@app.route("/stream/<type>/<frequency>")
def stream(type, frequency):
    if type == "fm":
        print("Opening FM stream:" + frequency)
        stream.openFM(frequency)

app.run(host="0.0.0.0", port=8234)
