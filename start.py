from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

'''
@app.route("/home/<user>")
def name(user):
	return f"<h1>Hello {user}!</h1>"'''


@app.route("/homes/<user>")
def users(user):
	example_safe = 'this is <strong>Bold</strong>'
	return render_template("user.html",user=user,example_safe= example_safe)


'''
#using for loop in jinja
@app.route("/homes/<user>")
def users(user):
	pizza = [10,"cheese\n","chicken"]
	return render_template("user.html",user=user,pizza= pizza)

'''


#create custom error pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#internal server error thing
@app.errorhandler(500)
def page_not_found(e):
	return render_template("404.html"), 500


if __name__ == "__main__":
	app.run(debug = True)