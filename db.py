import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select

def parse_file(file):
	file_name = file.filename.split('.')[0]
	data = pd.read_csv(file)
	return file_name, data

def create_table(table_name, data):
	engine = create_engine("postgresql+psycopg2://hseuser:hsepass@localhost/hsetest")
	conn = engine.connect()
	data.to_sql(table_name, con = engine, if_exists = 'append')


