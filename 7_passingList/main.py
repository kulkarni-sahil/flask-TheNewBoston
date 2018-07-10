from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "home"

@app.route('/shopping')
def shopping():
	shoppingList = ["a","b","c"]
	return render_template("shopping.html", shoppingList=shoppingList)

if __name__ == "__main__":
	app.run(debug=True)