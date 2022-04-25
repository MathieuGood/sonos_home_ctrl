import json
from flask import Flask, render_template, url_for
from soco import SoCo

app = Flask(__name__)

sonos = SoCo("192.168.1.30")


@app.route("/play")
def play():
    sonos.play()
    return "Ok"


@app.route("/pause")
def pause():
    sonos.pause()
    return "Ok"


@app.route("/next")
def next():
    sonos.next()
    return "Ok"


@app.route("/previous")
def previous():
    sonos.previous()
    return "Ok"


@app.route("/info-light")
def info_light():
    track = sonos.get_current_track_info()
    return json.dumps(track)


@app.route("/info")
def info():
    track = sonos.get_current_track_info()
    return json.dumps(track)


@app.route("/")
def index():
    track = sonos.get_current_track_info()
    return render_template("index.html", track=track)


if __name__ == "__main__":
    app.run(debug=True)
