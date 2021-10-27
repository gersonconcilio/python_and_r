import numpy as np
import pandas as pd

#CARREGANDO DADOS
dados = pd.read_csv("Credit.csv")

#FORMATO
print(f"\n{dados.shape}\n")

#RESUMO
print(f"\n{dados.describe()}\n")

#PRIMEIROS DADOS 
print(f"\n{dados.head(5)}\n")

#ULTIMOS DADOS
print(f"\n{dados.tail(2)}\n")

#APENAS UMA COLUNA
print(f"\n{dados[['duration']]}\n")

#COLUNAS 1 ATÉ 3
print(f"\n{dados.loc[1 : 3]}\n")

#COLUNAS 1 E 3
print(f"\n{dados.loc[[1, 3]]}\n")

#FILTRANDO POR NOME DA COLUNA
print(f"\n{dados.loc[dados['purpose'] == 'radio/tv']}\n")
print(f"\n{dados.loc[dados['credit_amount'] > 18000]}\n")

#FILTRANDO DADOS ENTRE DUAS COLUNAS ESPECIFICAS
print(f"\n{dados[['checking_status', 'duration']].loc[dados['credit_amount'] > 18000]}\n") 

#RENOMENANDO COLUNAS
dados.rename(columns={'duration': 'duracao', 'purpose': 'propósito'}, inplace=True)
print(f"\nColuna Renomeada: \n{dados.head(1)}")

#EXCLUINDO UMA COLUNA
dados.drop('checking_status', axis=1, inplace=True)
print(f"\nColuna Excluida: \n{dados.head(1)}")

#VERIFICANDO DADOS NULOS
print(f"\nDados Nulos: \n{dados.isnull().sum()}")

#REMOVENDO DADOS NaN
dados.dropna()

#PREENCHENDO DADOS FALTANTES
dados['duracao'].fillna(0, inplace=True)


print(f"\n{dados.iloc[0 : 3, 0 : 5]}")
print(f"\n{dados.iloc[[0, 1, 2, 3, 7], 0 : 5]}")

#SÉRIES ---- SÉRIES ---- SÉRIES ---- SÉRIES ---- SÉRIES ---- SÉRIES ---- SÉRIES

#PODE SER CRIADO A PARTIR DE -> LISTAS, ARRAY NUMPY, DATAFRAME
print(f"\n\n\n\n----------------------SERIES--------------------------\n\n")
s1 = pd.Series([11, 22, 13, 44, 45, 16]) 
print(f"Criando a Partir de uma Lista: \n{s1}")

array = np.array([32, 13, 141, 2, 3, 1, 5])
s2 = pd.Series(array)
print(f"\nCriando a Partir de um Array Numpy: \n{s2}")

s3 = dados['propósito']
print(f"\nCriando a Partir do Trecho DataFrame: \n{s3}")
print(type(dados['propósito']))
print(type(dados[['propósito']]))