from tinydb import TinyDB, Query
from banco import *

bd = TinyDB("Clientespb.json")
usuario = Query()

bd2 = TinyDB("Clientespm.json")
user2 = Query()

bd3 = TinyDB("Clientespp.json")
user3 = Query()

bd4 = TinyDB("Dvd.json")
user4 = Query()


def inserir(model: Clientespb):
    bd.insert({"nome": model.nome, "email": model.email, "numero": model.numero, "pedido": model.pedido, "pagamento": model.pagamento})
    print("inserido com sucesso")


def inserir2(model: Clientespm):
    bd2.insert({"nome": model.nome, "email": model.email, "numero": model.numero, "pedido": model.pedido, "pagamento": model.pagamento})
    print("inserido com sucesso")


def inserir3(model: Clientespp):
    bd3.insert({"nome": model.nome, "email": model.email, "numero": model.numero, "pedido": model.pedido, "pagamento": model.pagamento})
    print("inserido com sucesso")


def inserir4(model: Dvd):
    bd4.insert({"nome": model.nome, "email": model.email, "jtc": model.jtc, "msg": model.msg})
    print("inserido com sucesso")
