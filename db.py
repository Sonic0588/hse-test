import xlrd
import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def parse_file(file, names, header_row):
	file_name = file.filename.split('.')[0]
	file_exten = file.filename.split('.')[1]

	# определение расширения файла csv или xls
	if file_exten == 'csv':

		# выделение первой строки в файле
		header = file.readline().decode('utf-8')
		file.seek(0)

		# определение разделителя в файле
		sniffer = csv.Sniffer()
		dialect = sniffer.sniff(header)

		# парсинг csv в DataFrame
		data = pd.read_csv(file, sep = dialect.delimiter.strip(), names = names, header = header_row)
		return file_name, data

	elif file_exten == 'xlsx':

		data = pd.read_excel(file)
		return file_name, data


def create_table(table_name, data):
	engine = create_engine("postgresql+psycopg2://hseuser:hsepass@localhost/hsetest")
	conn = engine.connect()
	data.to_sql(table_name, con = engine, if_exists = 'append')


