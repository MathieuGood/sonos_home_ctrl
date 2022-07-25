from soco import discover
from flask import Flask, render_template, request

# http://127.0.0.1:5000/?vol=2&bass=2&treb=2
# http://127.0.0.1:5000/?spname=salon

app = Flask(__name__)

def get_speakers():
    return list(discover())
    
def get_volume(speaker):
    return speaker.volume

def get_eq(speaker):
    return speaker.bass, speaker.treble

def get_nightmode(speaker):
    return 'ok'

def get_dialogmode(speaker):
    return 'ok'

def get_info(speakers):
    spk_info = []
    
    for spk in speakers:
        spk_dict = {}
        spk_dict['name'] = spk.player_name
        spk_dict['volume'] = spk.volume
        spk_dict['bass'] = spk.bass
        spk_dict['treble'] = spk.treble
        spk_info.append(spk_dict)

    return spk_info


@app.route("/")
def function():
    # vol = request.args['vol']
    speakers = get_speakers()
    info = get_info(speakers)
    
    return render_template("index.html", speakers=info)


def main():
    speakers = get_speakers()
    print(get_info(speakers))




if __name__ == '__main__':
    # main()
    app.run(debug=True)
