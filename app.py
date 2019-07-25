from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/upload", methods = ['POST'])
def upload():
	file = request.files
	print(file)
	# file_name, data = db.parse_file(file)
	# return file_name


if __name__ == "__main__":
    app.run(debug = True)