

#執行 flask --app app run --debug

from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.jinja.html")