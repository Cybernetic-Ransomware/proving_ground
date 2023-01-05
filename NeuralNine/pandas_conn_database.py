import sqlite3
import pandas as pd


conn = sqlite3.connect('mydb_test.db')
cur = conn.cursor()


try:
    cur.execute("""DROP TABLE people""")
    conn.commit()
except sqlite3.OperationalError:
    print("Can't find a table, probably DB file has been removed.")
    pass


cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    ssn INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL
)
""")

try:
    cur.execute("""
    INSERT INTO people (ssn, name, age) VALUES 
    (105, 'John', 25),
    (121, 'Eliot', 45),
    (131, 'Jessica', 66),
    (551, 'Anthony', 65),
    (241, 'Paul', 33)
    """)
    conn.commit()
except sqlite3.IntegrityError:
    print('Failed to INSERT, recorods already exist.')
    pass



sql = pd.read_sql_query('SELECT * FROM people', conn)
df = pd.DataFrame(sql, columns=['ssn', 'name', 'age'])
print(df.head())


try:
    new_df = pd.DataFrame({
        'ssn': [123, 124, 125],
        'name': ['Giorgio', 'Jojo', 'Kujo'],
        'age': [48, 47, 49]
    })
    new_df.to_sql('people', con=conn, if_exists='append', index=False)
except sqlite3.IntegrityError:
    print('Failed to INSERT, recorods already exist.')
    pass


sql = pd.read_sql_query('SELECT * FROM people', conn)
df = pd.DataFrame(sql, columns=['ssn', 'name', 'age'])
print('*' * 20)
print(df.head())
