from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

countries = [{
    'country' : "tunisie",
    'lat' : "",
    'lon' :""
    }]
cities = [{
    'city' : "ariana",
    'lat' : "36.862499",
    'lon' :"10.195556",
    'weather' :"cloudy"
    },
    {
    'city' : "tunis",
    'lat' : "33.886917",
    'lon' :"9.537499",
    'weather':"sunny"
    }]



@app.route("/")
def index():
    return render_template("index.html", cities=cities , city={'city' : "tunis",
    'lat' : "33.886917",
    'lon' :"9.537499",
    'weather':"sunny"})

@app.route('/<string:cityname>')
def displayCityDetail(cityname):
    
    searchedcity = ""
    for city in cities:
        if( cityname== city['city']):
            searchedcity = city 
    return render_template("index.html" , cities=cities, city = searchedcity)

@app.route('/city-click',methods=['POST'])
def cityClick():
    cities = [{
    'city' : "ariana",
    'lat' : "36.862499",
    'lon' :"10.195556",
    'weather' :"cloudy"
    },
    {
    'city' : "tunis",
    'lat' : "33.886917",
    'lon' :"9.537499",
    'weather':"sunny"
    }]
    json_data = request.get_json()
    print(json_data)
    searchedcity = ""
    for city in cities:
        if(json_data['id'] == city['city']):
            searchedcity = city
    print("seached")
    print(searchedcity)

    return redirect("map.html" , cities=cities , city = searchedcity)

@app.route('/map')
def map():
    countries = [{
        'country' : "tunisie",
        'lat' : "",
        'lon' :""
    }]
    cities = [{
        'city' : "ariana",
        'lat' : "36.862499",
        'lon' :"10.195556"
    },
    {
        'city' : "tunis",
        'lat' : "33.886917",
        'lon' :"9.537499"
    }]
    return render_template("map.html", data= {'countries':countries , 'cities' : cities})

if __name__ == "__main__":
    app.run(debug=True)