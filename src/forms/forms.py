from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_ckeditor import CKEditorField


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembre-se de mim')
    botao_submit_login = SubmitField('Entrar')


class FormCriarUsuario(FlaskForm):
    posto_grad_id = SelectField(
        'Posto Grad', choices=[])
    quadro_id = SelectField('Quadro', choices=[])
    nome_completo = StringField('Nome Completo', validators=[DataRequired()])
    nome_guerra = StringField('Nome Guerra')
    setor_id = SelectField('Setor', choices=[])
    username = StringField('Nome de usuário')
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[
                                      DataRequired(), EqualTo('senha')])
    botao_submit_criar = SubmitField('Criar')
