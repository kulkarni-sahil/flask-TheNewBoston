from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "home page"

#routing to different page
@app.route('/tuna')
def tuna():
	return "this is tuna page"


# string variables
@app.route('/user/<name>')
def user(name):
	return "hello there %s" % name

@app.route('/post/<int:post_id>')
def post(post_id):
	return "<h2>post id is %s</h2>" % post_id


if __name__ =="__main__":
	app.run(debug=True)