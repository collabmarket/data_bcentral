import pandas as pd
import glob

# Listar archivos UF xls
lista_xls = glob.glob('rawdata/UF/ID_SERIE*')

# Opciones lectura de archivos xls
karg_xls = dict(skiprows=2, index_col=0)

# Opciones escrituda de archivos csv
karg_csv = dict(sep=';', decimal=',')

# Lista DataFrames UF
lista_df = []
for f in lista_xls:
    lista_df.append(pd.read_excel(f, **karg_xls))
# Concatena todos los archivos
aux = pd.concat(lista_df)
# Ordena por Fecha
aux = aux.sort_index()

# Guarda archivos UF csv
csvfname = 'data/uf.csv'
aux.to_csv(csvfname, **karg_csv)
