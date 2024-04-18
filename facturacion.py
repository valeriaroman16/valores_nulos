import pandas as pd

df = pd.read_excel('facturacion.xlsx')
print(df.isnull().sum())

df['CVE_VEND'] =df['CVE_VEND'].fillna(0)

df['FECHA_ENTREGA'] =df['FECHA_ENTREGA'].fillna('00000')

df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna('No cancelada')

valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('DF_Facturacion_limpio.csv')