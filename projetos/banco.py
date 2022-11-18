class Pedido:
    def __init__(self, pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco):
        self.pedidoid = pedidoid
        self.nome = nome
        self.pedido = pedido
        self.pedidoes = pedidoes
        self.preco = preco
        self.cliente = cliente
        self.nc = nc
        self.endereco = endereco


class Prontos:
    def __init__(self, pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco):
        self.pedidoid = pedidoid
        self.nome = nome
        self.pedido = pedido
        self.pedidoes = pedidoes
        self.preco = preco
        self.cliente = cliente
        self.nc = nc
        self.endereco = endereco


class Clientes:
    def __init__(self, pedidoid, cliente, nc, endereco):
        self.pedidoid = pedidoid
        self.cliente = cliente
        self.nc = nc
        self.endereco = endereco


class Entrega:
    def __init__(self, pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco):
        self.pedidoid = pedidoid
        self.nome = nome
        self.pedido = pedido
        self.pedidoes = pedidoes
        self.preco = preco
        self.cliente = cliente
        self.nc = nc
        self.endereco = endereco
