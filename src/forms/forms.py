from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cerebro.src.models.models import Usuario
from flask_login import current_user


class FormCriarUsuario(FlaskForm):
    posto_grad_id = SelectField(
        'Posto Grad', choices=[])
    quadro_id = SelectField('Quadro', choices=[])
    nome_completo = StringField('Nome Completo', validators=[DataRequired()])
    nome_guerra = StringField('Nome Guerra')
    obm_id = SelectField('Obm', choices=[])
    username = StringField('Nome de usuário')
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[
                                      DataRequired(), EqualTo('senha')])
    botao_submit_criar = SubmitField('Criar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça Login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Mantenha-me logado')
    botao_submit_login = SubmitField('Entrar')


class FormPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    setor = SelectField('Setor', validators=[DataRequired()])
    botao_submit_editarperfil = SubmitField('Confirmar')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já existente na plataforma.')


class FormChamado(FlaskForm):
    usuario = SelectField('Usuário que está emitindo o chamado', choices=[])
    titulo_chamado = StringField('Título do chamado', validators=[DataRequired(), Length(2, 200)])
    descricao_chamado = TextAreaField('Descrição', validators=[DataRequired(), Length(600)])
    tipo_chamado = SelectField('Tipo do chamado', choices=[])
    prioridade_chamado = SelectField('Prioridade', choices=[])
    setor_chamado = SelectField('Setor', choices=[])
    botao_submit = SubmitField('Enviar chamado')
