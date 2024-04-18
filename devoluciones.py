import pandas as pd

df=pd.read_excel("devoluciones.xlsx")
#print(df.head())

#print(df.isnull().sum())

df['CVE_VEND'] =df['CVE_VEND'].fillna(0)

df['CVE_PEDI'] =df['CVE_PEDI'].fillna('No registrada')

df['FECHA_CANCELA'] =df['FECHA_CANCELA'].fillna('No cancelada')

df['DOC_ANT'] =df['DOC_ANT'].fillna('000000')

valores_nulos=df.isnull().sum()
print(valores_nulos)

df.to_csv('DF_Devoluciones_limpio.csv')