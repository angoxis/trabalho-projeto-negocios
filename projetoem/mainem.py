from flask import Flask, render_template, redirect
from flask.globals import request
from tinydb import database
from conectar import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST", "GET"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    numero = request.form["numero"]
    pedido = request.form["pedido"]
    pagamento = request.form["pagamento"]
    pedidos = Clientespb(nome, email, numero, pedido, pagamento)
    inserir(pedidos)
    return redirect("/")


@app.route("/cadastrar2", methods=["POST", "GET"])
def cadastrar2():
    nome = request.form["nome"]
    email = request.form["email"]
    numero = request.form["numero"]
    pedido = request.form["pedido"]
    pagamento = request.form["pagamento"]
    pedidos2 = Clientespm(nome, email, numero, pedido, pagamento)
    inserir2(pedidos2)
    return redirect("/")


@app.route("/cadastrar3", methods=["POST", "GET"])
def cadastrar3():
    nome = request.form["nome"]
    email = request.form["email"]
    numero = request.form["numero"]
    pedido = request.form["pedido"]
    pagamento = request.form["pagamento"]
    pedidos3 = Clientespp(nome, email, numero, pedido, pagamento)
    inserir3(pedidos3)
    return redirect("/")


@app.route("/cadastrar4", methods=["POST", "GET"])
def cadastrar4():
    nome = request.form["nome"]
    email = request.form["email"]
    jtc = request.form["jtc"]
    msg = request.form["msg"]
    duvida = Dvd(nome, email, jtc, msg)
    inserir4(duvida)
    return redirect("/")


@app.route("/redic")
def redic():
    return render_template("/pagina1.html")


@app.route("/redic2")
def redic2():
    return render_template("/pagina2.html")


@app.route("/redic3")
def redic3():
    return render_template("/pagina3.html")


@app.route("/redic4")
def redic4():
    return render_template("/duvidas.html")


if __name__ == "__main__":
    app.run(debug=True)
