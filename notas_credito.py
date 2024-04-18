import pandas as pd

df = pd.read_excel('notas_credito.xlsx')
#print(df.isnull().sum())

df['CVE_VEND'] =df['CVE_VEND'].fillna(0)
df['CVE_PEDI'] =df['CVE_PEDI'].fillna('No registrada')
df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna('No cancelada')

valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('DF_NotasCredito_limpio.csv')