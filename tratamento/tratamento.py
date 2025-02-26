import pandas as pd

df = pd.read_csv(r'C:\Users\nohan\Desktop\Programas\Dados\arquivos\dados_loja.csv')

df.rename(columns={'Unnamed: 0':'ID'}, inplace=True)

df['cliente'] = df.cliente.astype('string')
df['email'] = df.email.astype('string')
df['endereco'] = df.endereco.astype('string')
df['data_compra'] = pd.to_datetime(df.data_compra)
df['produto'] = df.produto.astype('string')
df['quantidade_comprada'] = df.quantidade_comprada.astype('int')

df['data_compra'] = df['data_compra'].dt.date

df = df.to_excel('C:\\Users\\nohan\\Desktop\\Programas\\Dados\\arquivos\\dados_loja_tratados.xlsx')