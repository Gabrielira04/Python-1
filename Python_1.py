import pandas as pd


arquivo_teste = 'testepy1.xlsx'

df = pd.read_excel(arquivo_teste, sheet_name = 'testepy') 

print (df)
