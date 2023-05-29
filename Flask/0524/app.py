from flask import Flask,render_template
import plotly.express as px
import plotly
import json

app = Flask(__name__)

@app.route("/")
def index():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip",trendline="ols")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.jinja.html',graphJSON=graphJSON)

@app.route("/index1")
def index1():
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country')
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index1.jinja.html',graphJSON=graphJSON)

@app.route("/index2")
def index2():
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
    fig.update_traces(textposition="bottom right")
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index2.jinja.html',graphJSON=graphJSON)