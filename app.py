from flask import Flask, render_template, request
import db

app = Flask(__name__)

# путь формы для загрузки файла
@app.route("/")
def hello():
    return render_template('index.html')

# путь парсинга csv и отправки данных в базу данных
@app.route("/upload", methods = ['POST'])
def upload():
	# получаю файл из request
	file = request.files['file']

	# получаю имя файла и данные в виде DataFrame
	file_name, data = db.parse_file(file)

	# создание таблицы в базе данных и внесение данных в таблицу
	db.create_table(file_name, data)

	return "Ok"

if __name__ == "__main__":
    app.run(debug = True)