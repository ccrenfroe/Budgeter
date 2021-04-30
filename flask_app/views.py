from flask_app import app
from flask import render_template
from utils.plaid_utils import plaidtils
@app.route('/')
def hello():
    return render_template("base.html")

@app.route("/create_link_token", methods=['GET','POST'])
def create_link_token():
    print("entering route!")
    plaidtils.create_link_token()
    return render_template("base.html")