from flask import Flask, render_template, redirect, make_response
from conectar import *
from flask.globals import request

app = Flask(__name__)


@app.route("/")
def index():
    if request.authorization and request.authorization.username == "username" and request.authorization.password == "senha":
        result = mostrar()
        return render_template("index.html", result=result)
    return make_response('obrigatorio o login', 401, {'WWW-Authenticate': 'Basic realm="login required"'})


@app.route("/concluidos")
def pag2():
    result = mostrar2()
    return render_template("concluidos.html", result=result)


@app.route("/pedidos")
def pag3():
    result = mostrar()
    return render_template("pedidos.html", result=result)


@app.route("/clientes")
def pag4():
    result = mostrar3()
    return render_template("clientes.html", result=result)


@app.route("/entregas")
def pag5():
    result = mostrar4()
    return render_template("entregas.html", result=result)


@app.route("/cadastrar", methods=["POST", "GET"])
def cadastrar():
    pedidoid = request.form["pedidoid"]
    nome = request.form["nome"]
    pedido = request.form["pedido"]
    pedidoes = request.form["pedidoes"]
    preco = request.form["preco"]
    cliente = request.form["cliente"]
    nc = request.form["nc"]
    endereco = request.form["endereco"]
    pedidos = Pedido(pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco)
    pronto = Prontos(pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco)
    cli = Clientes(pedidoid, cliente, nc, endereco)
    inserir(pedidos)
    inseri(pronto)
    inseri2(cli)
    return redirect("/")


@app.route("/deletar/<int:pedidoid>")
def deletar(pedidoid):
    try:
        deleta(pedidoid)
        delet(pedidoid)
        return redirect("/")

    except:
        return "algo aconteceu"


@app.route('/atualizar/<int:pedidoid>', methods=["POST", "GET"])
def atualiza(pedidoid):
    if request.method == 'POST':
        pedidoid = request.form["pedidoid"]
        nome = request.form["nome"]
        pedido = request.form["pedido"]
        pedidoes = request.form["pedidoes"]
        preco = request.form["preco"]
        cliente = request.form["cliente"]
        nc = request.form["nc"]
        endereco = request.form["endereco"]
        pedidos = Pedido(pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco)
        try:
            atualizar(pedidoid, pedidos)
            return redirect('/')
        except:
            return 'algo deu errado'
    else:
        pedidos = buscaid(pedidoid)
        return render_template('atualiza.html', pedidos=pedidos)


@app.route('/entrega/<int:pedidoid>', methods=["POST", "GET"])
def entrega(pedidoid):
    if request.method == 'POST':
        pedidoid = request.form["pedidoid"]
        nome = request.form["nome"]
        pedido = request.form["pedido"]
        pedidoes = request.form["pedidoes"]
        preco = request.form["preco"]
        cliente = request.form["cliente"]
        nc = request.form["nc"]
        endereco = request.form["endereco"]
        entrega = Entrega(pedidoid, nome, pedido, pedidoes, preco, cliente, nc, endereco)
        try:
            entregar(pedidoid, entrega)
            return redirect('/pedidos')
        except:
            return 'algo deu errado'
    else:
        entrega = buscaid(pedidoid)
        return render_template('verificar.html', pedidos=entrega)


@app.route("/concluido/<int:pedidoid>", methods=["POST", "GET"])
def concluidos(pedidoid):
    try:
        deleta(pedidoid)
        return redirect("/")
    except:
        return "algo aconteceu"


@app.route("/deletar2/<int:pedidoid>")
def deletar2(pedidoid):
    try:
        delet(pedidoid)
        return redirect("/concluidos")

    except:
        return "algo aconteceu"


@app.route("/deletar3/<int:pedidoid>")
def deletar3(pedidoid):
    try:
        deleta2(pedidoid)
        return redirect("/entregas")

    except:
        return "algo aconteceu"


@app.route("/redi")
def redi():
    return redirect("/concluidos")


@app.route("/redic")
def redic():
    return redirect("/entregas")


@app.route("/vol")
def vol():
    return redirect("/")


@app.route("/cli")
def cli():
    return redirect("/clientes")


@app.route("/dltd")
def dltd():
    try:
        deletatd()
        return redirect("/concluidos")

    except:
        return "algo deu errado"


if __name__ == "__main__":
    app.run(debug=True)
