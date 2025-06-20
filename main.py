import flask, os
import stream
from flask import Flask, send_from_directory, Response 
app = Flask(__name__)

@app.route("/stream/<type>/<frequency>")
def streamRoute(type, frequency):
    if type == "fm":
        print("Opening FM stream: " + frequency)
        feed = stream.openFM(frequency)
        def generate():
            try:
                while True:
                    chunk = feed.stdout.read(4096)
                    if not chunk:
                        break
                    print("returning chunk")
                    yield chunk
            finally:
                feed.wait()
                feed.stdout.close()


                
        return Response(generate(), mimetype="audio/mpeg")
app.run(host="0.0.0.0", port=8234)
