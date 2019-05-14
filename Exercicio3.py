#Dados exercicio 2 e 3
nomes=['Laura','Paula','Thiago','Daniela','Isabela','Enzo','Vinicius']
#Dados exercicio 2
produtos=['Dadinho','Suco','Bolo','Cafe','Sorvete','Refrigerante','Capuccino']
precos=[0.50, 5.00, 4.50, 4.00, 6.00, 4.50, 6.00]
a=nomes
b=produtos
c=precos
y=len(nomes)
def listab(f, g, h) :
    n=0
    for i in range(y):
        print(f[n],'-', g[n],'-', h[n])
        n=n+1
listab(a, b, c)             
    
