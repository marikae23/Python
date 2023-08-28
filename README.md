# Python
Python é uma linguagem de programação popular. Foi criada por Guido van Rossum e lançada em 1991. Python pode ser usado em um servidor para criar aplicações web, pode ser usado junto com software para criar fluxos de trabalho, pode se conectar a sistemas de bancos de dados. Também pode ler e modificar arquivos, pode ser usado para lidar com grandes volumes de dados e realizar matemática complexa e pode ser usado para prototipagem. rápida ou para desenvolvimento de software pronto para produção.

## Built-in Data Types:
>[!IMPORTANT]
>- Text Type:	     str;
>- Numeric Types:	 int, float, complex;
>- Sequence Types:	 list, tuple, range;
>- Mapping Type:	   dict;
>- Set Types:	     set, frozenset;
>- Boolean Type:	   bool;
>- Binary Types:    bytes, bytearray, memoryview;
>- None Type:	     NoneType;

## Python Numbers:
> [!NOTE]
>Existem três tipos numéricos em Python:
>- int;
>- float;
>- complex;

**Exemplo**
```ruby
# Variáveis de tipos numéricos são criadas quando você atribui um valor a elas:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Para verificar o tipo de qualquer objeto em Python, use a função "type()":
print(type(x))
print(type(y))
print(type(z))
```
<Details>
<summary>TIPOS NÚMERICOS!</summary>
  
## INT
  
Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado.

```ruby
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```
## FLOAT
Float, ou "número de ponto flutuante", é um número, positivo ou negativo, que contém um ou mais decimais.

```ruby
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float também pode ser números científicos com um "e" para indicar a potência de 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

## COMPLEX
Números complexos são escritos com um "j" como parte imaginária:

```ruby
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```
<Details>
  <summary>CONVERSÃO!</summary>
Você pode converter de um tipo para outro com os métodos int(), float() e complex():

```ruby
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```
</Details>
</Details>

# Dúvidas?
Pergunta: Qual a diferença entre aspas simples e duplas para criar strings?
>Resposta: Não há diferença funcional entre aspas simples e duplas para criar strings em Python. Você pode usar qualquer uma delas para delimitar strings.

Pergunta: Como verificar o tipo de uma variável em Python?
>Resposta: Você pode usar a função embutida type() para verificar o tipo de uma variável. Por exemplo: tipo = type(42) retornará <class 'int'>.

Pergunta: Como fazer um loop em uma lista?
>Resposta: Você pode usar um loop for para percorrer os elementos de uma lista. Por exemplo:

```ruby
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)
```

Pergunta: Como definir uma função em Python?
>Resposta: Para definir uma função em Python, você usa a palavra-chave def, seguida do nome da função e seus parâmetros. Exemplo:

```ruby
def saudacao(nome):
    print("Olá, " + nome + "!")
```

```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```
