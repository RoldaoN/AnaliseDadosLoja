#Fazendo as Importações necessárias
import random
import pandas as pd
from faker import Faker
fake = Faker('pt-BR')
fake.seed_locale('pt-BR')

#Criando dados dos Clientes
cliente = []
email = []
endereco = []
cpf = []

for x in range(6):
    primeiro_nome = fake.first_name()
    ultimo_nome = fake.last_name()
    nome_completo = primeiro_nome + ' ' + ultimo_nome
    cliente.append(nome_completo)
    compania = fake.company().split()[0].strip(',')
    endereco.append(fake.address())
    cpf.append(fake.cpf())

##Criação dos emails para os clientes
list_of_domains = (
    'com',
    'com.br',
    'net',
    'net.br',
    'org',
    'org.br',
    'gov',
    'gov.br'
)
for x in range(6):
    dns_org = fake.random_choices(
        elements=list_of_domains,
        length=1
    )[0]
    email.append(f"{primeiro_nome}.{ultimo_nome}@{compania}.{dns_org}".lower())

#Criando os Produtos da Loja
produto=[
    'Celular',
    'Tablet',
    'Notebook',
    'Monitor',
    'Impressora',
    'Fones de Ouvido'
]

#Criando o Preço dos Produtos
preco = []
for x in produto:
    preco_aleatorio = round(random.uniform(1000, 6000), 2)
    preco.append(float(preco_aleatorio))

#Criando a quantidade de vendas de cada item
quantidade = []

for x in range(6):
    quantidade.append(float(random.randint(1, 10)))

#Criando o Valor da compra baseado na quantidade de itens comprados e no preço
valor_compra = []

for x in range(len(quantidade)):
    valor = round(quantidade[x] * preco[x], 2)
    valor_compra.append(float(valor))

#Criando o Dia em que as compras foram feitas
data_compra = []

for x in range(6):
    data_compra.append(fake.date())

#Transformando as listas criadas em um DataFrame
df = pd.DataFrame({'cliente': pd.Series(cliente), 'cpf': pd.Series(cpf),
                   'email': pd.Series(email), 'endereco': pd.Series(endereco),
                   'data_compra': pd.Series(data_compra), 'produto': pd.Series(produto),
                   'preco_unitario': pd.Series(preco), 'quantidade_comprada': pd.Series(quantidade),
                   'valor_total': pd.Series(valor_compra)})

#Importando o DataFrame para CSV
df = df.to_csv('C:\\Users\\nohan\\Desktop\\Programas\\Dados\\arquivos\\dados_loja.csv', index=False)