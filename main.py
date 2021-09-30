# 9aa6ce3812f80c24068cabf559194696
import requests
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'ruhtra'
api_key = '9aa6ce3812f80c24068cabf559194696'

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == 'POST':
        session['city'] = request.form['city'].lower()
        return redirect(url_for("mid"))
    return render_template("search.html")

@app.route("/search")
def mid():
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={session['city']}&appid={api_key}").json()
    if response['cod'] == 200:
        session['temperature'] = str(round(response['main']['temp'] - 273))
        return redirect(url_for("results"))
    else:
        return render_template("error.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == '__main__':
    app.run(debug=True)