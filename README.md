# AnaliseDadosLoja

Mini projeto para criação de dados fakes para estudo de base de dados.

Usando a biblioteca Faker, criei um pequeno arquivo CSV para importar todos os dados e depois fazer uma saída de dados transformados em XLSX.

Para o tratamento e criação dos dados usei a Biblioteca Pandas para melhor visualização, edição e tratamento dos dados, visando uma melhor autonomia em questão de performance e editabilidade.

# Criação de Clientes

Com a biblioteca Faker fui criando cada campo necessário para a tabela experimento.
Iniciando com a localização do Faker.

```python
  from faker import Faker
  fake = Faker('pt-BR')
  fake.seed_locale('pt-BR')
```
Partindo da localização pude criar os 'clientes' conforme a necessidade, gerando itens como:
  - Primeiro Nome;
  - Último Nome;
  - Email;
  - Endereço;
  - CPF

# Criando Produtos

A priemira que fiz para o desenvolvimento dos produtos da loja foi decidir quais itens gostaria de incluir, criando uma lista deles.

Com a lista de itens criada, o próximo passo foi criar uma variação de preço para cada item da lista, usando o random como um meio de criar um valor aleatório e decímal para cada produto.

Definido os valores unitários de cada produto, o random foi utilizado novamente para selecionar o valor de produtos comprados por um dos clientes.

Com o valor unitário definido e a quantidade adquirida de cada cliente, pode-se fazer o calculo do valor final de compra.

Finalizando todos os itens necessários para esta tabela, foi criado um DataFrame para armazenar e exportar essas informações em formato CSV, para um fututo tratamento.

```python
  df = pd.DataFrame({'cliente': pd.Series(cliente), 'cpf': pd.Series(cpf),
                   'email': pd.Series(email), 'endereco': pd.Series(endereco),
                   'data_compra': pd.Series(data_compra), 'produto': pd.Series(produto),
                   'preco_unitario': pd.Series(preco), 'quantidade_comprada': pd.Series(quantidade),
                   'valor_total': pd.Series(valor_compra)})

  df = df.to_csv('C:\\Users\\nohan\\Desktop\\Programas\\Dados\\arquivos\\dados_loja.csv', index=False)
```
