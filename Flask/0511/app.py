from flask import Flask,render_template,request
import datasource


app = Flask(__name__)
@app.route("/")
def index():
    stock_data = datasource.get_stock_data(stockid=2330)    
    return render_template("index.jinja.html",data=stock_data)


@app.route("/features/")
def features():
    
    return render_template("features.jinja.html")

@app.route("/priceing/")
def priceing():
    
    return render_template("priceing.jinja.html")

@app.route("/about/")
def about():
    return render_template("about.jinja.html")

@app.route("/form/",methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return render_template("form.jinja.html")
    
    rows = datasource.get_stockid()
    return render_template("form.jinja.html",rows=rows)
    





    