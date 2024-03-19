from cerebro.src import database, login_manager
from datetime import datetime
from flask_login import UserMixin


class Legislacao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))


class Anexo_Legislacao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    legislacao_id = database.Column(
        database.Integer, database.ForeignKey('legislacao.id'), nullable=False)
    nome_arquivo = database.Column(database.String(100), nullable=False)
    created = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)
    modified = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)


class Posto_grad(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    sigla = database.Column(database.String(20), nullable=False)
    usuario = database.relationship(
        'Users', backref='posto_grad_usuarios', lazy=True)


class Quadro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    quadro = database.Column(database.String(20), nullable=False)
    descricao = database.Column(database.String(50), nullable=False)
    usuario = database.relationship(
        'Users', backref='quadro_usuarios', lazy=True)


class Obm(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    sigla = database.Column(database.String(15), nullable=False)
    descricao = database.Column(database.String(100), nullable=False)
    endereco = database.Column(database.String(200), nullable=False)
    setor = database.relationship('Setor', backref='obm_setor', lazy=True)


class Setor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    obm_id = database.Column(
        database.Integer, database.ForeignKey('obm.id'), nullable=False)
    setor = database.Column(database.String(50), nullable=False)
    created = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)
    modified = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)
    usuario = database.relationship(
        'Users', backref='setor_usuarios', lazy=True)


@login_manager.user_loader
def load_usuario(id_usuario):
    return Users.query.get(int(id_usuario))


class Users(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    posto_grad_id = database.Column(
        database.Integer, database.ForeignKey('posto_grad.id'), nullable=False)
    quadro_id = database.Column(
        database.Integer, database.ForeignKey('quadro.id'), nullable=False)
    nome_completo = database.Column(database.String(100), nullable=False)
    nome_guerra = database.Column(database.String(50), nullable=False)
    setor_id = database.Column(
        database.Integer, database.ForeignKey('setor.id'), nullable=False)
    username = database.Column(database.String(20), nullable=False)
    senha = database.Column(database.String(256), nullable=False)
    created = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)
    modified = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)