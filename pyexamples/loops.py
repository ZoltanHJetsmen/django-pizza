s = 'hello world'

for char in s:
    print(char)

pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'presunto'
    },
    {
        'nome': 'Marco',
        'sabor': 'portuguesa'
    }
]

for pedido in pedidos:
    print('Nome: {0} Sabor: {1}'.format(pedido['nome'], pedido['sabor'])) 
    print(pedido['nome'], pedido['sabor'])


