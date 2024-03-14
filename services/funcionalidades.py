
from datetime import datetime

import mysql.connector


db = mysql.connector.connect(
        host="localhost",
        user="Pedro",
        password="PhgD12*@",
        database="web2"
    )




# ==== funcionalidades produtos ==== #
def listar_produto():
    cursor=db.cursor()
    cursor.execute("select * from produtos")
    produtos = cursor.fetchall()
    return produtos


def listar_produto_id(id):
    cursor=db.cursor()
    cursor.execute(f"select * from produtos where id={id}")
    produtos = cursor.fetchone()
    return produtos

# print(listar_produto_id(6))

def produto_existe(nome_produto, fornecedor_id):
    cursor=db.cursor()
    cursor.execute(f"select * from produtos where nome='{nome_produto}' and fornecedor_id={fornecedor_id}")
    produto = cursor.fetchone()
    return produto

# print(produto_existe("Kiks", 1))



def alterar_preço_produto(id, preco):
    produto_existe = listar_produto_id(id)
    if produto_existe:
        cursor=db.cursor()
        cursor.execute(f"update produtos set preco={preco} where id={id}")
        return "Preço alterado com sucesso"
    else: 
        return "Produto não encontrado"

# print("antes:", listar_produto_id(3))
# print (alterar_preço_produto(2, 1100))
# print("depois:", listar_produto_id(1))

def cadastrar_produto(nome, descricao, codigo_de_barras, preco, quantidade, fornecedor_id, alcoolico):
    produto = produto_existe(nome, fornecedor_id)
    if not produto:
        cursor=db.cursor()
        cursor.execute(f"INSERT INTO produtos(nome, descricao, codigo_de_barras, preco, quantidade, fornecedor_id, alcoolico) VALUES ('{nome}', '{descricao}', '{codigo_de_barras}', {preco}, {quantidade}, {fornecedor_id}, {alcoolico});")
        db.commit()
        return "Produto cadastrado com sucesso!"
    else:
        return "Produto ja cadastrado"


# print(cadastrar_produto("HorseWhite", "Bom demaizi", "1233466", 100.90, 15, 1, 1))



def deletar_produto(id):
    produto_existe = listar_produto_id(id)
    if produto_existe:
        cursor=db.cursor()
        cursor.execute(f"delete from produtos where id={id}")
        db.commit()
        return ("Produtos deletados com sucesso!")
    else:
        return(f"Produto {id} não existe")

# print (deletar_produto(3))


# ==== funcionalidades fornecedor ==== #
def listar_fornecedores():
    cursor=db.cursor(dictionary=True)
    cursor.execute("select * from fornecedores")
    fornecedores = cursor.fetchall()
    return fornecedores


def listar_fornecedor_nome(nome):
    cursor=db.cursor(dictionary=True)
    cursor.execute(f"select * from fornecedores where nome='{nome}'")
    fornecedores = cursor.fetchone()
    return fornecedores

# print(listar_fornecedor_nome("Sophia"))

def alterar_fornecedor(data:dict):
    if (data["contato"] !='')and(data["endereco"] !=''):
        cursor=db.cursor()
        cursor.execute(f"update fornecedores set contato='{data['contato']}', endereco='{data['endereco']}' where nome='{data['nome']}'")
        db.commit()
        
    
    elif data["contato"] !='':
        cursor=db.cursor()
        cursor.execute(f"update fornecedores set contato='{data['contato']}' where nome='{data['nome']}'")
        db.commit()
        
    
    elif data["endereco"] !='':
        cursor=db.cursor()
        cursor.execute(f"update fornecedores set endereco='{data['endereco']}' where nome='{data['nome']}'")
        db.commit()



# print(alterar_fornecedor(2, endereco="Rua. Piroka"))


def cadastrar_fornecedor(nome, cnpj, contato, endereco):
    fornecedor_existe = listar_fornecedor_nome(nome)
    if not fornecedor_existe:
        cursor=db.cursor()
        cursor.execute(f"INSERT INTO fornecedores(nome, cnpj, contato, endereco) VALUES ('{nome}', '{cnpj}', '{contato}', '{endereco}')")
        db.commit()
        return 'Fornecedor cadastrado com sucesso!'
    else:
        return 'Fornecedor ja existe!'
    
# print(cadastrar_fornecedor("Wesleyyyyy", "11199091123", "R. Interlagos"))


def deletar_fornecedor(nome):
    fornecedor_existe = listar_fornecedor_nome(nome)
    if fornecedor_existe:
        cursor=db.cursor()
        cursor.execute(f"delete from fornecedores where nome='{nome}'")
        db.commit()


#print(deletar_fornecedor("Sophia"))



# ==== funcionalidades do clientes ==== #
    
def cliente_existe(nome_cliente, endereco_cliente):
    cursor=db.cursor()
    cursor.execute(f"select * from clientes where nome='{nome_cliente}' and endereco='{endereco_cliente}'")
    cliente = cursor.fetchone()
    return cliente



def cadastrar_cliente(nome, contato, endereco):
    cliente = cliente_existe(nome, endereco)
    if not cliente:
        cursor=db.cursor()
        cursor.execute(f"INSERT INTO clientes(nome, contato, endereco) VALUES ('{nome}', '{contato}', '{endereco}');")
        db.commit()
        return "Cliente cadastrado com sucesso!"
    else:
        return "Cliente ja cadastrado"
# print(cadastrar_cliente("Sophia", "11989128912", "R. Topazio"))


def alterar_cliente(id, contato=None, endereco=None):
    if contato and endereco:
        cursor=db.cursor()
        cursor.execute(f"update clientes set contato='{contato}', endereco='{endereco}'")
        db.commit()
        return "Contato e endereço alterados com sucesso"
    
    elif contato:
        cursor=db.cursor()
        cursor.execute(f"update clientes set contato='{contato}' where id={id}")
        db.commit()
        return "Contato alterado com sucesso"
    
    elif endereco:
        cursor=db.cursor()
        cursor.execute(f"update clientes set endereco='{endereco}' where id={id}")
        db.commit()
        return "Endereço alterado com sucesso"
    
    else:
        return "Nenhum valor foi passado para alteração!"

# print(alterar_cliente(2, endereco="Rua. Whashington"))
# print(alterar_cliente(2, contato="11910138017"))


def listar_cliente_id(id):
    cursor=db.cursor()
    cursor.execute(f"select * from clientes where id='{id}'")
    cliente = cursor.fetchone()
    return cliente


def deletar_cliente(id):
    cliente_existe = listar_cliente_id(id)
    if cliente_existe:
        cursor=db.cursor()
        cursor.execute(f"delete from clientes where id='{id}'")
        db.commit()
        return ("Cliente deletado com sucesso!")
    else:
        return(f"Cliente {id} não existe")

# print(deletar_cliente(2))


# ==== funcionalidades pedidos ==== #

def listar_pedido_id(id):
    cursor=db.cursor()
    cursor.execute(f"select * from pedido where id='{id}'")
    pedido = cursor.fetchone()
    return pedido


def cadastrar_pedido(cliente_id, produto, quantidade, preco_unitario, total ):
    pedido_existe = listar_pedido_id(id)
    if not pedido_existe:
        cursor=db.cursor()
        cursor.execute(f"INSERT INTO pedido (cliente_id, produto, quantidade, preco_unitario, total, data_pedido) VALUES ('{cliente_id}', '{produto}', '{quantidade}', '{preco_unitario}', '{total}', '{datetime.now()}')")
        db.commit()
        return 'Pedido cadastrado com sucesso!'
    else:
        return 'Pedido ja existente!'
# print(cadastrar_pedido(1, "Jack", 4, 2.90, 11.60))


def alterar_pedido(cliente, vendedor):
    pass

def deletar_pedido(id):
    pass



