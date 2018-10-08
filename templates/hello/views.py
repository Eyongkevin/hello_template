from templates import app
from flask import render_template

@app.route('/')
@app.route('/hello')
def index():
	return render_template("index.html")



