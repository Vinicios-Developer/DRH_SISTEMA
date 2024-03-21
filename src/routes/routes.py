from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from cerebro.src import app, bcrypt, database
from cerebro.src.forms.forms import FormLogin, FormCriarUsuario
from cerebro.src.models.models import Usuario, Posto_grad, Quadro, Setor, Obm


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Você já está logado.', 'alert-info')
        return redirect(url_for('login'))

    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        email = Usuario.query.filter_by(email=form_login.email.data).first()

        if email and bcrypt.check_password_hash(email.senha, form_login.senha.data):
            login_user(email, remember=form_login.lembrar_dados.data)
            flash('Login feito com sucesso!', 'alert-success')

            if email.username == 'Vinicios':
                return redirect(request.args.get('next', url_for('usuarios')))
            return redirect(url_for('login'))
        else:
            flash('Falha no Login, e-mail ou senha incorretos.', 'alert-danger')

    return render_template('login_user.html', form_login=form_login)


@app.route('/criar-usuario', methods=['GET', 'POST'])
def criarUsuario():
    form_criar_usuario = FormCriarUsuario()

    form_criar_usuario.posto_grad_id.choices = [
        (posto.id, posto.sigla) for posto in Posto_grad.query.all()]
    form_criar_usuario.quadro_id.choices = [
        (quadro.id, quadro.quadro) for quadro in Quadro.query.all()]
    form_criar_usuario.setor_id.choices = [
        (setor.id, f"{setor.setor}/{setor.obm_setor.sigla}") for setor in Setor.query.join(Obm).all()
    ]

    if form_criar_usuario.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form_criar_usuario.senha.data)
        usuarios = Usuario(posto_grad_id=form_criar_usuario.posto_grad_id.data,
                         quadro_id=form_criar_usuario.quadro_id.data,
                         nome_completo=form_criar_usuario.nome_completo.data,
                         nome_guerra=form_criar_usuario.nome_guerra.data,
                         setor_id=form_criar_usuario.setor_id.data,
                         username=form_criar_usuario.username.data,
                         email=form_criar_usuario.email.data,
                         senha=senha_cript)
        database.session.add(usuarios)
        database.session.commit()
        flash("Usuário cadastrado com sucesso!", "alert-success")
        return redirect(url_for("login"))
    return render_template('criarUsuario.html', form_criar_usuario=form_criar_usuario)

