import pandas as pd
import numpy as np
df=pd.read_excel('Fujo_caja_proyectado.xlsx')  

# print("hola")
df = df.fillna(0)
# print(df)

df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col5']
df.to_excel("charts.xlsx",index = False)
# dfd[['Pais','Empresa','Tienda','Caja','Serie','Numero','Linea','Articulo','Total','x']] = dfd['Datos'].str.split(',', 17, expand=True
dfn=pd.read_excel('charts.xlsx')

print(dfn.iloc[0]['cadena'])
