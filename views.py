from flask import Flask, flash, render_template, request, redirect, send_from_directory, session, url_for
import requests
from main import app, db
from datetime import datetime
from sqlalchemy import or_
from helpers import recupera_imagem
from models import Cliente, Emprestimo, Livro, Usuario
import bcrypt


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None or not 'usuario_logado':
        return redirect(url_for('login'))

    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    lista = Livro.query.order_by(Livro.id)
    return render_template('index.html', livros=lista, nome=nome)


@app.route('/buscar', methods=['POST',])
def buscar_estante():
    lista = Livro.query.order_by(Livro.id)

    if request.form['busca']:
        lista = Livro.query.order_by(Livro.id).filter(or_(Livro.titulo.contains(request.form['busca']), Livro.autor.contains(
            request.form['busca']), Livro.isbn_10 == request.form['busca'], Livro.isbn_13 == request.form['busca']))
    else:
        return redirect(url_for('index'))

    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    return render_template('index.html', livros=lista, nome=nome)


@app.route('/cadastrar-livro')
def cadastro_livro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    dados = ''
    return render_template('cadastrar_livros.html', dados=dados, nome=nome)


@app.route('/cadastrar-livro/buscar', methods=['POST',])
def buscar_livro():
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{
        request.form['busca_livro']}'

    response = requests.get(url)
    data = response.json()

    if data['totalItems'] != 0:
        for datas in data['items']:
            data = datas['volumeInfo']

        nome = data['title']
        autor = data['authors'][0]
        lancamento = data['publishedDate']
        sinopse = data["description"]
        isbn_10 = data['industryIdentifiers'][0]['identifier']
        isbn_13 = data['industryIdentifiers'][1]['identifier']

        dados = {'nome': nome, 'autor': autor, 'lancamento': lancamento,
                 'descricao': sinopse, 'isbn_10': isbn_10, 'isbn_13': isbn_13}

        nome = Usuario.query.filter_by(email=session['usuario_logado']).first()

        return render_template('cadastrar_livros.html', dados=dados, nome=nome)

    flash('ISBN não encontrado')
    return redirect(url_for('cadastro_livro'))


@app.route('/salvar', methods=['POST',])
def salvar_livro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    lancamento = request.form['lancamento']
    isbn_10 = request.form['isbn10']
    isbn_13 = request.form['isbn13']
    sinopse = request.form['descricao']
    quantidade = request.form['quantidade']

    livro = Livro.query.filter_by(isbn_10=isbn_10).first()

    if livro:
        flash('O livro já existe!')
        return redirect(url_for('cadastro_livro'))

    novo_livro = Livro(titulo=titulo, autor=autor, lancamento=lancamento,
                       sinopse=sinopse, isbn_10=isbn_10, isbn_13=isbn_13, quantidade=quantidade)
    db.session.add(novo_livro)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa{novo_livro.id}.jpg')

    flash(novo_livro.titulo+' Foi cadastrado com sucesso!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    if len(nome_arquivo) < 5:
        nome_arquivo = 'capa'+nome_arquivo+'.jpg'

    return send_from_directory('uploads', nome_arquivo)


@app.route('/editar/<int:id>')
def editar_livro(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima='editar_livro'))

    dados = Livro.query.filter_by(id=id).first()
    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    capa_jogo = recupera_imagem(id)
    return render_template('editar_livros.html', dados=dados, capa_jogo=capa_jogo, nome=nome)


@app.route('/deletar/<int:id>')
def deletar_livro(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima='editar_livro'))

    dados = Livro.query.filter_by(id=id).delete()
    db.session.commit()

    flash('Livro deletado com sucesso!')

    return redirect(url_for('index'))


@app.route('/atualizar', methods=['POST',])
def atualizar_livro():
    livro = Livro.query.filter_by(id=request.form['id']).first()
    livro.titulo = request.form['titulo']
    livro.autor = request.form['autor']
    livro.lancamento = request.form['lancamento']
    livro.isbn_10 = request.form['isbn10']
    livro.isbn_13 = request.form['isbn13']
    livro.sinopse = request.form['descricao']
    livro.quantidade = request.form['quantidade']

    db.session.add(livro)
    db.session.commit()

    if request.files['arquivo']:
        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{upload_path}/capa{livro.id}.jpg')

    flash('Alterações feitas com sucesso!')
    return redirect(url_for('index'))


@app.route('/cadastrar-leitor')
def cadastro_leitor():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()

    return render_template('cadastrar_leitor.html', nome=nome)


@app.route('/salvar-leitor', methods=['POST',])
def salvar_leitor():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cep = request.form['cep']
    endereco = request.form['endereco']
    numero = request.form['numero']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    telefone = request.form['telefone']
    email = request.form['email']

    leitor = Cliente.query.filter_by(cpf=cpf).first()

    if leitor:
        flash('O livro já existe!')
        return redirect(url_for('cadastro_livro'))

    novo_leitor = Cliente(nome=nome, cpf=cpf, cep=cep,
                          endereco=endereco, numero=numero,
                          bairro=bairro, cidade=cidade,
                          telefone=telefone, email=email)
    db.session.add(novo_leitor)
    db.session.commit()

    flash(novo_leitor.nome+' Foi cadastrado com sucesso!')
    return redirect(url_for('index'))


@app.route('/buscar-leitor', methods=['POST',])
def buscar_leitor():

    cpf = request.form['busca_leitor']

    if not request.form['busca_leitor']:
        return redirect(url_for('cadastro_leitor'))

    cliente = Cliente.query.filter_by(cpf=cpf).first()
    if not cliente:
        return redirect(url_for('cadastro_leitor'))

    id = cliente.id_cliente
    return redirect(url_for('editar_leitor', id=id))


@app.route('/editar-leitor/<int:id>')
def editar_leitor(id):
    cliente = Cliente.query.filter_by(id_cliente=id).first()
    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    emprestimos = Emprestimo.query.filter_by(cliente_id_cliente=id)
    return render_template('editar_leitor.html', cliente=cliente, nome=nome, emprestimos=emprestimos)


@app.route('/atualizar-leitor', methods=['POST',])
def atualizar_leitor():
    cliente = Cliente.query.filter_by(id_cliente=request.form['id']).first()
    cliente.nome = request.form['nome']
    cliente.cpf = request.form['cpf']
    cliente.cep = request.form['cep']
    cliente.endereco = request.form['endereco']
    cliente.numero = request.form['numero']
    cliente.bairro = request.form['bairro']
    cliente.cidade = request.form['cidade']
    cliente.telefone = request.form['telefone']
    cliente.email = request.form['email']

    db.session.add(cliente)
    db.session.commit()

    flash('Alterações feitas com sucesso!')
    return redirect(url_for('index'))


@app.route('/deletar-leitor/<int:id>')
def deletar_leitor(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    cliente = Cliente.query.filter_by(id_cliente=id).delete()
    db.session.commit()

    flash('Cliente deletado com sucesso!')

    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuario.query.filter_by(email=request.form['email']).first()

    senha = request.form['senha']
    senha = senha.encode('utf-8')

    if usuario:
        if bcrypt.checkpw(senha, usuario.senha.encode('utf-8')):
            session['usuario_logado'] = usuario.email
            flash('Bem vindo ' + usuario.user+'!!!')
            return redirect(url_for('index'))

    flash('Dados incorretos')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Desconectado!')
    return redirect(url_for('login'))


@app.route('/cadastrar_usuario')
def cadastrar_usuario():
    return render_template('cadastrar_usuario.html')


@app.route('/salvar-usuario', methods=['POST',])
def salvar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmacao = request.form['confirmacao']

    if senha != confirmacao:
        flash('As senhas não batem, preencha novamente!'+senha+confirmacao)
        return redirect(url_for('cadastrar_usuario'))

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario:
        flash('O usuario já existe!')
        return redirect(url_for('cadastrar_usuario'))

    session['usuario_logado'] = email

    hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    novo_usuario = Usuario(nome=nome, user=email,
                           email=email, senha=hashed, admin=0)
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Bem vindo ' + nome+'!!!')
    return redirect(url_for('index'))


@app.route('/emprestimos')
def emprestimo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None or not 'usuario_logado':
        return redirect(url_for('login'))

    lista = Emprestimo.query.all()
    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    return render_template('emprestimos.html', nome=nome, lista=lista)


@app.route('/admin')
def admin():
    if 'usuario_logado' not in session or session['usuario_logado'] == None or not 'usuario_logado':
        return redirect(url_for('login'))

    nome = Usuario.query.filter_by(email=session['usuario_logado']).first()
    if nome.admin == 0:
        flash('Não tem permissão!')
        return redirect(url_for('index'))

    lista = Usuario.query.all()
    return render_template('admin.html', lista=lista, nome=nome)


@app.route('/delete-user/<string:user>')
def deletar_user(user):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    usuario = Usuario.query.filter_by(user=user).delete()
    db.session.commit()

    flash('Usuario deletado com sucesso!')

    return redirect(url_for('admin'))


@app.route('/alterar-user/<string:user>', methods=['POST',])
def alterar_user(user):
    usuario = Usuario.query.filter_by(user=user).first()
    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.user = request.form['email']
    usuario.admin = request.form['admin']

    db.session.add(usuario)
    db.session.commit()

    flash('Alteração feita com sucesso!!!')
    return redirect(url_for('admin'))
