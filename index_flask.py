from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('http://data.citedia.com/r1/parks/?crs=EPSG:4326', headers={'User-Agent': 'parking/index_flask.py'})
    all_data = r.text
    all_data_json = json.loads(all_data)

    parks = []
    coordonees = []

    for p in all_data_json['parks']:
        parks.append(p)

    for c in all_data_json['features']['features']:
        coordonees.append(c)


    return render_template('index.html', parks =parks, coordonees=coordonees)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)
