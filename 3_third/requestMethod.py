from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index ():
	return "homepage it is </br> method used : %s" % request.method

if __name__ == "__main__" :
	app.run(debug=True)