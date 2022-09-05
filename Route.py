from flask import Flask, render_template
from app import app
# (C) ROUTES
# (C1) BOOKING PAGE
@app.route("/")
def index():
 return render_template("home.html")
 
# (C2) THANK YOU PAGE
@app.route("/thank")
def thank():
  return render_template("templatesthank.html")

