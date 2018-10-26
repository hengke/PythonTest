import psycopg2


SQL = "SELECT * FROM main.\"Album\";"
print(SQL)
with psycopg2.connect(database="xlwingsDatabaseTest", user="postgres", password="zhhkhengke", host="127.0.0.1", port="5432") as pg_conn:
    with pg_conn.cursor() as pg_curs:
        pg_curs.execute(SQL)
        rows = pg_curs.fetchall()


# Get the result and column names
col_names = [col[0] for col in pg_curs.description]
print(col_names)

for row in rows:
    print(row)