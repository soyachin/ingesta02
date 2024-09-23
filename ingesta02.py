import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
  host="98.82.247.140",
  user="root",
  password="utec",
  database="tienda"
)

c = mysql.connector.connect(**db_config)

q = "SELECT * FROM fabricantes;"
df = pd.read_sql(query, c)

file = 'dump.csv'
data_frame.to_csv(file, index=False)
print(f"Exportado a '{file}' !")
