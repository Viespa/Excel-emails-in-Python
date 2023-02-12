import pandas as pd

# Carga el archivo de Excel en un DataFrame de pandas
df = pd.read_excel("data.xlsx")

# Selecciona la columna "nombre_de_la_columna"
emails = df["Email"]

emails_unique =emails.unique().tolist()
print(emails_unique)

