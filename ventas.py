import pandas as pd
import numpy as np

df=pd.read_csv("ventas_totales.csv")
#print(df.head())

#print(df.isnull().sum())

#Quitar nulos en 'salón ventas'
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
                                            # Redondea la media de 'salón ventas' a 1 decimal


#Quitar nulos en 'tarjetas de crédito'
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))

#Quitar nulos en 'tarjetas de crédito'
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#print(df['otros_medios'].describe())
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Rellena valores nulos con ffill
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()

#Rellena valores nulos con bfill
df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()

#Rellena valores nulos con 0
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()


df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1))
valores_nulos=df.isnull().sum()

df['lacteos'] =df['lacteos'].fillna(0)
valores_nulos=df.isnull().sum()

df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1))
valores_nulos=df.isnull().sum()

df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill')
valores_nulos=df.isnull().sum()

df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill')
valores_nulos=df.isnull().sum()

df['indumentaria_calzado_textiles_hogar'] =df['indumentaria_calzado_textiles_hogar'].fillna(round(df['indumentaria_calzado_textiles_hogar'].mean(),1))
valores_nulos=df.isnull().sum()

df['electronicos_articulos_hogar'] =df['electronicos_articulos_hogar'].fillna(round(df['electronicos_articulos_hogar'].median(),1))
valores_nulos=df.isnull().sum()

df['otros'] =df['otros'].fillna(round(df['otros'].mean(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('Ventas_totales_limpio.csv')