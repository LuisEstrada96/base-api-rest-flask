from functools import wraps
from flask import request, abort
from config.config import auth as configAuth

def auth(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        try:
            if request.headers['apikey'] and request.headers['apikey'] == configAuth['apikey']:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        except:
            abort(401)
    return decorated_function
