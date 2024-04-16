import pandas as pd
import numpy as np

df=pd.read_csv("ventas_totales.csv")
#print(df.head())

#print(df.isnull().sum())

#Quitar nulos en 'salón ventas'
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
                                            # Redondea la media de 'salón ventas' a 1 decimal
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quitar nulos en 'tarjetas de crédito'
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)