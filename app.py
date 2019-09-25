from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyC_v59Qddii5_xD4IWoDqujUI25pxJfywU"


@app.route('/')
def map():

    return render_template('map.html')
    

app = Flask(__name__,)
GoogleMaps(app)

@app.route("/")
def mapview():
# creating a map in the view
    mymap = Map(
    identifier="view-side",
    lat=37.4419,
    lng=-122.1419,
    markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
    identifier="sndmap",
    lat=37.4419,
    lng=-122.4519,
    markers=[
    {
    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    'lat': 37.4419,
    'lng': -122.1519,
    'infobox': "<b>Hello World</b>"
    },
    {
    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    'lat': 37.4300,
    'lng': -122.1400,
    'infobox': "<b>Hello World from other place</b>"
    }
    ]
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
   app.run(debug=True)