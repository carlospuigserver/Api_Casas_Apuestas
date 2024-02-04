import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect('bookmaker.db')

# Ejecutar la consulta y cargar los datos en un DataFrame
df_clientes = pd.read_sql_query("SELECT id, nombre, apellido, email, activado FROM clientes", conn)
# Guardar el DataFrame en un archivo CSV
df_clientes.to_csv('TAREA/CSV/clientes.csv', index=False)  # index=False para no incluir el índice del DataFrame en el archivo

# Cerrar la conexión
conn.close()

# Ahora df_clientes contiene tus datos y puedes comenzar tu análisis
df_clientes['dominio_email'] = df_clientes['email'].apply(lambda x: x.split('@')[1])
df_clientes['dominio_email'].value_counts().plot(kind='bar')
plt.title('Frecuencia de Dominios de Correo Electrónico')
plt.xlabel('Dominio')
plt.ylabel('Frecuencia')
plt.show()

# Contar cuántos clientes están activados
print("Clientes activados:", df_clientes['activado'].sum())



# Gráfico de barras para mostrar el número de clientes activados vs no activados
plt.figure(figsize=(6,4))
df_clientes['activado'].value_counts().plot(kind='bar')
plt.title('Distribución de Clientes Activados y No Activados')
plt.xlabel('Estado de Activación')
plt.ylabel('Cantidad de Clientes')
plt.xticks(ticks=[0, 1], labels=['Activados', 'No Activados'], rotation=0)
plt.show()
