#Dados exercicio 2 e 3
nomes=['Laura','Paula','Thiago','Daniela','Isabela','Enzo','Vinicius']
#Dados exercicio 2
produtos=['Dadinho','Suco','Bolo','Cafe','Sorvete','Refrigerante','Capuccino']
a=nomes
b=produtos
y=len(nomes)
#
def listaa(c, d):
    n=0
    for i in range(y):
        print(c[n],'-',d[n])
        n=n+1
listaa(a, b) 
