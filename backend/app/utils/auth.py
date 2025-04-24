# auth.py
import jwt
from datetime import datetime, timedelta
from flask import current_app

def generar_token(user_id):
    payload = {
        'sub': user_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

# validators.py
import re

def validate_email_format(email):
    return re.match(r'^[\w\.-]+@uab\.edu\.bo$', email) is not None

def decodificar_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload.get('sub')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

