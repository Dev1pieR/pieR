from flask import Flask, request, render_template, redirect, url_for
from services.funcionalidades import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

#ROTAS FORNECEDOR

@app.route("/fornecedor")
def fornecedor():
    data = listar_fornecedores()
    return render_template("fornecedor.html", data=data)

@app.get('/fornecedor/<nome>')
def fornecedor_nome(nome):
    data = listar_fornecedor_nome(nome)
    return render_template("fornecedor_nome.html", data=data)

@app.route('/fornecedor/update', methods=['GET','PATCH'])
def att_fornecedor():
    if request.method == 'PATCH':
        data = request.json
        print(data)
        if data['nome'] in listar_fornecedor_nome(data['nome'])['nome']:
            alterar_fornecedor(data)
            return ('ok', 200)
        else: return ('ok', 400)
    return render_template('alterar_fornecedor.html')

@app.route('/fornecedor_del', methods=['GET','DELETE'])
def delet_fornecedor():
    if request.method == 'DELETE':
        nome = request.json['nome']
        if nome in listar_fornecedor_nome(nome)['nome']:

            deletar_fornecedor(nome)
            return ('ok', 200)
        else: return ('ok', 400)
            
    return render_template("deletar_fornecedor.html")

@app.route("/cadastro_fornecedor", methods=['GET','POST'])
def cadastro_fornecedor():
    if request.method=='POST':
        data = request.form
        return cadastrar_fornecedor(nome=data['nome'] , endereco=data['endereco'] , contato=data['contato'] , cnpj=data['cnpj'] )
    return render_template("cadastro_fornecedor.html")


#ROTAS PRODUTOS

@app.route("/cadastro_produto")
def cadastro():
    return render_template("cadastro_produto.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

#ROTAS PEDIDOS

@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html")



if __name__ == '__main__':
    app.run(debug=True)