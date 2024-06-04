from main import db


class Livro(db.Model):
    __tablename__ = "livro"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(20), nullable=False)
    lancamento = db.Column(db.Date, nullable=False)
    sinopse = db.Column(db.String(4000), nullable=False)
    isbn_10 = db.Column(db.String(20), nullable=False)
    isbn_13 = db.Column(db.String(20), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Titulo: %r>' % self.titulo


class Usuario(db.Model):
    __tablename__ = "usuario"
    nome = db.Column(db.String(50), nullable=False)
    user = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False, primary_key=True)
    senha = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<user: %r>' % self.user


class Cliente(db.Model):
    __tablename__ = "cliente"
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(90), nullable=False)
    cpf = db.Column(db.String(45), nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(255))
    numero = db.Column(db.String(20))
    bairro = db.Column(db.String(55))
    cidade = db.Column(db.String(55))
    telefone = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<nome: %r>' % self.nome


class Emprestimo(db.Model):
    __tablename__ = "emprestimo"
    id_emprestimo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_saida = db.Column(db.Date, nullable=False)
    data_retorno = db.Column(db.Date, nullable=False)
    cliente_id_cliente = db.Column(
        db.Integer, db.ForeignKey('cliente.id_cliente'))
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'))

    cliente = db.relationship('Cliente', foreign_keys=cliente_id_cliente)
    livro = db.relationship('Livro', foreign_keys=livro_id)

    def __init__(self, cliente_id_cliente, livro_id, data_saida, data_retorno):
        self.cliente_id_cliente = cliente_id_cliente
        self.livro_id = livro_id
        self.data_saida = data_saida
        self.data_retorno = data_retorno

    def __repr__(self):
        return '<Emprestimo: {} - {} - {}'.format(self.id_emprestimo, self.cliente.nome, self.livro.titulo)
