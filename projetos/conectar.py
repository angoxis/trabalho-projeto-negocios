import pandas as pd
from tinydb import TinyDB, Query
from projetos.banco import Pedido, Prontos, Clientes, Entrega


bd = TinyDB("pedidos.json")
usuario = Query()

bd1 = TinyDB("prontos.json")
user = Query()

bd2 = TinyDB("clientes.json")
user2 = Query()

bd3 = TinyDB("entrega.json")
user3 = Query()


def inserir(model: Pedido):
    bd.insert({"pedidoid": model.pedidoid, "nome": model.nome, "pedido": model.pedido, "pedidoes": model.pedidoes,
               "preco": model.preco, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
    print("inserido com sucesso")


def inseri(model: Prontos):
    bd1.insert({"pedidoid": model.pedidoid, "nome": model.nome, "pedido": model.pedido, "pedidoes": model.pedidoes,
                "preco": model.preco, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
    print("inserido com sucesso")


def inseri2(model: Clientes):
    bd2.insert({"pedidoid": model.pedidoid, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
    print("inserido com sucesso")


def inseri3(model: Entrega):
    bd2.insert({"pedidoid": model.pedidoid, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
    print("inserido com sucesso")


def mostrar():
    todos = bd.all()
    return todos


def mostrar2():
    todos = bd1.all()
    return todos


def mostrar3():
    todos = bd2.all()
    return todos


def mostrar4():
    todos = bd3.all()
    return todos


def deleta(pedidoid: int):
    if bd.search(usuario.pedidoid == str(pedidoid)):
        bd.remove(usuario.pedidoid == str(pedidoid))
        bd2.remove(usuario.pedidoid == str(pedidoid))
        print("usuario apagado com sucesso")
    else:
        print("usuario não encontrado")


def delet(pedidoid: int):
    if bd1.search(usuario.pedidoid == str(pedidoid)):
        bd1.remove(usuario.pedidoid == str(pedidoid))
        print("usuario apagado com sucesso")
    else:
        print("usuario não encontrado")


def deleta2(pedidoid: int):
    if bd3.search(usuario.pedidoid == str(pedidoid)):
        bd3.remove(usuario.pedidoid == str(pedidoid))
        print("usuario apagado com sucesso")
    else:
        print("usuario não encontrado")


def atualizar(pedidoid: int, model: Pedido):
    if bd.search(usuario.pedidoid == pedidoid):
        bd.remove(usuario.pedidoid == pedidoid)
        bd1.remove(usuario.pedidoid == pedidoid)
        bd2.remove(usuario.pedidoid == pedidoid)
        bd.insert({"pedidoid": model.pedidoid, "nome": model.nome, "pedido": model.pedido, "pedidoes": model.pedidoes,
                   "preco": model.preco, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
        bd1.insert({"pedidoid": model.pedidoid, "nome": model.nome, "pedido": model.pedido, "pedidoes": model.pedidoes,
                    "preco": model.preco, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
        bd2.insert({"pedidoid": model.pedidoid, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
        print("inserido com sucesso")
    else:
        print("esse pedido não existe")


def entregar(pedidoid: int, model: Entrega):
    if bd.search(usuario.pedidoid == pedidoid):
        bd.remove(usuario.pedidoid == pedidoid)
        bd2.remove(usuario.pedidoid == pedidoid)
        bd3.insert({"pedidoid": model.pedidoid, "nome": model.nome, "pedido": model.pedido, "pedidoes": model.pedidoes,
                   "preco": model.preco, "Cliente": model.cliente, "nc": model.nc, "endereco": model.endereco})
    else:
        print("esse pedido não existe")


def mostrartabela():
    todos = pd.DataFrame(bd)
    return todos


def buscaid(pedidoid):
    return bd.search(usuario.pedidoid == str(pedidoid))


def deletatd():
    bd1.drop_tables()
