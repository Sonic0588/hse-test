from flask import Flask, render_template, request
import db
import json

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

	# задаю значения для DataFrame по умолчанию
	header_row = 0
	names = None

	# проверяю есть ли доп. параметры
	if 'params' in request.form:
		params = json.loads(request.form['params'])

		# переназначаю параметры из request
		if 'alt_names_col' in params:
			names = params['alt_names_col']

		if 'header_row' in params:
			header_row = int(params['header_row'])

	# получаю имя файла и данные в виде DataFrame
	file_name, data = db.parse_file(file, names, header_row)

	# создание таблицы в базе данных и внесение данных в таблицу
	db.create_table(file_name, data)

	return "Ok"


if __name__ == "__main__":
    app.run(debug = True)