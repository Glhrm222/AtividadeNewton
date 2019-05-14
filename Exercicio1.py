#Dados exercício 1
x=str(input('ForneÃ§a o produto: ')) 
def valor(produto):
    if x == 'Salgado':
        return 'Salgado -> 4,00'
    elif x == 'Refrigerante':
        return 'Refrigerante -> 4,50'
    elif x == 'Suco':
        return 'Suco -> 5,00'
    elif x == 'Sorvete':
        return 'Sorvete -> 6,00'
    elif x == 'Cafe':
        return 'Cafe -> 4,00'
    elif x == 'Capuccino':
        return 'Capuccino -> 4,00'
    elif x == 'Bolo':
        return 'Bolo -> 4,50'
    elif x == 'Dadinho':
        return 'Dadinho -> 0,50'
    else:
        return 'Naoo vendemos esse produto'
print(valor(x))
