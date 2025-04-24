import re

def validate_email_format(email: str) -> bool:
    """Valida que el correo tenga formato @uab.edu.bo"""
    return re.match(r'^[\w\.-]+@uab\.edu\.bo$', email) is not None