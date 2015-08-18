pedidos = []


def adicionaPedidos(nome, sabor, observacao='None'):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao
    return (pedido)

pedidos.append(adicionaPedidos('mario', 'pepperoni'))
pedidos.append(adicionaPedidos('marco', 'portuguesa', 'dobro de presunto'))

for pedido in pedidos:
    template = 'Nome: {nome}\nSabor: {sabor}'
    print(template.format(**pedido))
    if pedido['observacao']:
        print('Observacao: {}'.format(pedido['observacao']))
    print('-'*20)
