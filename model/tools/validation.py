import re

def name_validator(name, message):
    if isinstance(name, str) and re.match("^[آ-ی\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)

def username_validator(username, message):
    if isinstance(username, str) and re.match("^[a-zA-Z]{3,30}$", username):
        return username
    else:
        raise ValueError(message)

def password_validator(password, message):
    if isinstance(password, str) and re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$", password):
        return password
    else:
        raise ValueError(message)


def national_id_validator(national_id, message):
    if re.match("^(\d{10}|\d{3}\-\d{6}\-\d)$", national_id):
        return national_id
    else:
        raise ValueError(message)

def date_birth_validator(date, message):
    if isinstance(date, str) and re.match("^([1][0-9][0-9][0-9])\.[0-1][0-9]\.(([0-2][0-9])|(30))$", date):
        return date
    else:
        raise ValueError(message)

