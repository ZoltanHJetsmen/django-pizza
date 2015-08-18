pedidos = []


def adicionaPedidos(nome, sabor):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor

    pedidos.append(pedido)

print(pedidos)
adicionaPedidos('mario', 'pepperoni')
adicionaPedidos('marco', 'portuguesa')
print(pedidos)
