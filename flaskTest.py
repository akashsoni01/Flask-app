from flask import Flask, render_template

posts = [
	{
	'title':'apple',
	'course':'swift 4',
	'descreption':'this course gives you all that you need for development'
	},
	{
	'title':'googel',
	'course':'kotlin',
	'descreption':'this course gives you all that you need for development'
	}
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')



if __name__ == '__main__':
    app.run(debug=True)

