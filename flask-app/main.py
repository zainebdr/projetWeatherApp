from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/historique')
def hist():
    return render_template("historique.html")

if __name__ == "__main__":
    app.run(debug=True)