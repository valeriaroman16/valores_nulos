import pandas as pd

df=pd.read_excel("clientes.xlsx")
#print(df.head())

#print(df.isnull().sum())

df['RFC']=df['RFC'].fillna('XAXX010101000')

df['NOMBRE'] = df['NOMBRE'].fillna('Se desconoce')
valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('DF_Clientes_limpio.csv')