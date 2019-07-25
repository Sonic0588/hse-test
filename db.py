import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select

def parse_file(file):
	file_name = file.filename
	data = pd.read_csv(file)
	return file_name, data



engine = create_engine("postgresql+psycopg2://hseuser:hsepass@localhost/hsetest")
conn = engine.connect()
# data.to_sql('test_csv', con = engine, if_exists = 'append')


# titles = str(data.dtypes).lower().split()
# #print(titles)

# for id in range(len(titles)):
# 	if titles[id] == 'object':
# 		titles[id] = 'TEXT,'
# 	elif 'int' in titles[id]:
# 		titles[id] = 'INT,'
# 	elif 'float' in titles[id]:
# 		titles[id] = 'FLOAT,'

# titles = ' '.join(titles[:-2]).split(',')
# titles = titles[:-1]

# query = '''CREATE TABLE test_csv({0})'''.format(','.join(titles))
# cursor.execute(query)

# conn.commit()

# with open('test_csv.csv', 'r') as f:
# 	next(f)
# 	cursor.copy_from(f, 'test_csv', sep = ',')

# conn.commit()
