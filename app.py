"""Web app."""
import flask
from flask import Flask, render_template, request, redirect, url_for
from ml_model import fetch_data
import pickle
import base64
import requests
app = flask.Flask(__name__)

data = [{'name':'Delhi', "sel": "selected"}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
# data = [{'name':'India', "sel": ""}]
months = [{"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": "selected"}]
cities = [{'name':'Delhi', "sel": "selected"}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}, {'name':'New York', "sel": ""}, {'name':'Los Angeles', "sel": ""}, {'name':'London', "sel": ""}, {'name':'Paris', "sel": ""}, {'name':'Sydney', "sel": ""}, {'name':'Beijing', "sel": ""}]

model = pickle.load(open("flood_rf_model.pkl", 'rb'))

@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

@app.route('/plots.html')
def plots():
    return render_template('plots.html')

@app.route('/heatmaps.html')
def heatmaps():
    return render_template('heatmaps.html')

@app.route('/satellite.html')
def satellite():
    direc = "processed_satellite_images/Delhi_July.png"
    with open(direc, "rb") as image_file:
        image = base64.b64encode(image_file.read())
    image = image.decode('utf-8')
    return render_template('satellite.html', data=data, image_file=image, months=months, text="Delhi in January 2022")

@app.route('/satellite.html', methods=['GET', 'POST'])
def satelliteimages():
    place = request.form.get('place')
    date = request.form.get('date')
    data = [{'name':'Delhi', "sel": ""}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
    months = [{"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": ""}]
    for item in data:
        if item["name"] == place:
            item["sel"] = "selected"
    
    for item in months:
        if item["name"] == date:
            item["sel"] = "selected"

    text = place + " in " + date + " 2022"

    direc = "processed_satellite_images/{}_{}.png".format(place, date)
    with open(direc, "rb") as image_file:
        image = base64.b64encode(image_file.read())
    image = image.decode('utf-8')
    return render_template('satellite.html', data=data, image_file=image, months=months, text=text)

@app.route('/predicts.html')
def predicts():
    return render_template('predicts.html', cities=cities, cityname="Information about the city")

@app.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    try:
        cityname = request.form["city"]
        cities = [{'name':'Delhi', "sel": ""}, {'name':'Mumbai', "sel": ""}, {'name':'Bangalore', "sel": ""},{'name':'Pune', "sel": ""}]
        for item in cities:
            if item['name'] == cityname:
                item['sel'] = 'selected'
        print(cityname)

        city = str(cityname)

        df = fetch_data.get_data(city)

        prediction = model.predict(df)


        if str(prediction[0]) == "0":
            pred = "Safe"
        else:
            pred = "Unsafe"

            #'tempmax','temp','humidity','precip','precipprob','precipcover','snowdepth','windspeed','cloudcover'
        
        return render_template('predicts.html', cityname="Information about " + cityname, cities=cities, temp=round(df['temp'][0], 2), maxt=round(df['tempmax'][0], 2), wspd=round(df['windspeed'][0], 2), cloudcover=round(df['cloudcover'][0], 2), percip=round(df['precip'][0], 2), humidity=round(df['humidity'][0], 2), pred = pred)
    except:
        return render_template('predicts.html', cities=cities, cityname="Oops, we weren't able to retrieve data for that city.")

if __name__ == "__main__":
    app.run(debug=True)