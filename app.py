import psycopg2

conn = psycopg2.connect(dbname = 'hsetest', user = 'hseuser',
							password = 'hsepass', host = 'localhost')

cursor = conn.cursor()
cursor.execute("SELECT * FROM test")
print(cursor.fetchone())
