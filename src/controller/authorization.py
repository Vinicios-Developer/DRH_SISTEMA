from functools import wraps
from flask import abort, redirect, url_for
from flask_login import current_user


def authorize_obm(obm_id):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                if current_user.username == 'Vinicios' or current_user.obm_id == obm_id:
                    return func(*args, **kwargs)
                else:
                    abort(403)  # Código HTTP 403 Forbidden
            else:
                # Caso o usuário não esteja autenticado
                return redirect(url_for('login'))
        return wrapper
    return decorator
