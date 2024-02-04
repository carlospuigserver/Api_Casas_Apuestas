import sqlite3
import pandas as pd
conn = sqlite3.connect('bookmaker.db')

# Ejecutar la consulta y cargar los datos en un DataFrame
df_clientes = pd.read_sql_query("SELECT id, nombre, apellido, email, activado FROM clientes", conn)
# Guardar el DataFrame en un archivo CSV
df_clientes.to_csv('TAREA/CSV/clientes.csv', index=False)  # index=False para no incluir el índice del DataFrame en el archivo

# Cerrar la conexión
conn.close()

# Ahora df_clientes contiene tus datos y puedes comenzar tu análisis
