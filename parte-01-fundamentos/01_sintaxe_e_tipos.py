# Sintaxe básica e tipos de dados em Python

# 1. Comentários
# Comentários começam com # e não são executados pelo Python.


# 2. Sintaxe básica
nome = "Ana"          # atribuição de variável
idade = 25             # inteiro

if idade >= 18:
    print(nome, "é maior de idade")  # recuo de 4 espaços define o bloco
else:
    print(nome, "é menor de idade")


# 3. Tipos de dados básicos

# Texto (str)
cidade = "São Paulo"

# Inteiro (int)
quantidade = 10

# Ponto flutuante (float)
preco = 19.99

# Booleano (bool): True ou False
ativo = True

# Lista (list): coleção ordenada e modificável
cores = ["azul", "verde", "vermelho"]

# Tupla (tuple): coleção ordenada e não modificável
coordenadas = (10, 20)

# Dicionário (dict): pares chave-valor
aluno = {"nome": "Carlos", "nota": 9}

# Conjunto (set): coleção sem elementos repetidos
numeros = {1, 2, 3, 3}

# Valor nulo (None)
observacao = None


# 4. Descobrindo o tipo de uma variável
print(type(cidade))       # <class 'str'>
print(type(quantidade))   # <class 'int'>
print(type(preco))        # <class 'float'>
print(type(ativo))        # <class 'bool'>


# 5. Operações comuns
texto = "Python"
print(texto.upper())                     # converte para maiúsculas
print(len(cores))                        # tamanho da lista
print(aluno["nome"])                     # acessa valor pela chave
print(numeros)                           # mostra {1, 2, 3}


# 6. Conversão entre tipos
numero_texto = "100"
numero_inteiro = int(numero_texto)
print(numero_inteiro + 50)               # 150

print(float("2.5"))                      # 2.5
print(str(42))                           # "42"
