from cerebro.src import database, login_manager
from flask_login import UserMixin
from datetime import datetime


class Legislacao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuario.id'))


class Anexo_Legislacao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    legislacao_id = database.Column(
        database.Integer, database.ForeignKey('legislacao.id'), nullable=False)
    nome_arquivo = database.Column(database.String(100), nullable=False)


class Posto_grad(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    sigla = database.Column(database.String(20), nullable=False)
    usuario = database.relationship(
        'Usuario', backref='posto_grad_usuarios', lazy=True)


class Quadro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    quadro = database.Column(database.String(20), nullable=False)
    descricao = database.Column(database.String(50), nullable=False)
    usuario = database.relationship(
        'Usuario', backref='quadro_usuarios', lazy=True)


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
    usuario = database.relationship(
        'Usuario', backref='setor_usuarios', lazy=True)


@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
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
    email = database.Column(database.String, nullable=False, unique=True)
    chamado = database.relationship('Chamado', backref='user', lazy=True)


class Tipo_chamado(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome_tipo_chamado = database.Column(database.String, nullable=False)


class Prioridade(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    urgencia = database.Column(database.String, nullable=False)


class Chamado(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    titulo_chamado = database.Column(database.String, nullable=False)
    descricao_chamado = database.Column(database.Text, nullable=False)
    id_tipo_chamado = database.Column(
        database.Integer, database.ForeignKey('tipo_chamado.id'), nullable=False)
    id_prioridade = database.Column(
        database.Integer, database.ForeignKey('prioridade.id'), nullable=False)
    setor_id = database.Column(
        database.Integer, database.ForeignKey('setor.id'), nullable=False)
    data_emissao = database.Column(database.DateTime, nullable=False, default=datetime.now)
