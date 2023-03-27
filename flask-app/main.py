from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def hello():
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
    return render_template("index.html" , cities=cities)

@app.route('/city-click',methods=['POST'])
def cityClick():
    json_data = request.get_json()
    print(json_data)
    return "clicked"

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