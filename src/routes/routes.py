from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from cerebro.src import app, bcrypt, database
from cerebro.src.forms.forms import FormLogin, FormCriarUsuario, FormCriarNoticia
from cerebro.src.models.models import Users


@app.route("/login")
def login():

    if current_user.is_authenticated:
        flash('Você já está logado.', 'alert-info')
        return redirect(url_for('home'))

    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Users.query.filter_by(username=form_login.username.data).first()

        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash('Login feito com sucesso!', 'alert-success')

            if usuario.username == 'Vinicios':
                return redirect(request.args.get('next', url_for('usuarios')))
            return redirect(url_for('home'))
        else:
            flash('Falha no Login, e-mail ou senha incorretos.', 'alert-danger')

    return render_template('login_user.html', form_login=form_login)
