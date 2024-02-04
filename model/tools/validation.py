import re


def name_validator(name, message):
    if isinstance(name, str) and re.match("^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)


def username_validator(username, message):
    if isinstance(username, str) and re.match("^[a-zA-Z]{3,30}$", username):
        return username
    else:
        raise ValueError(message)


def password_validator(password, message):
    if isinstance(password, str) and re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$",
                                              password):
        return password
    else:
        raise ValueError(message)


def national_id_validator(national_id, message):
    if re.match("^(\d{10}|\d{3}\-\d{6}\-\d)$", national_id):
        return national_id
    else:
        raise ValueError(message)

def phone_number_validator(phone_number, message):
    if re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone_number):
        return phone_number
    else:
        raise ValueError(message)

def date_validator(date, message):
    if isinstance(date, str) and re.match("^([1][0-9][0-9][0-9])\.[0-1][0-9]\.(([0-2][0-9])|(30))$", date):
        return date
    else:
        raise ValueError(message)


def time_validator(time, message):
    if isinstance(time, str) and re.match("^([01]\d|2[0-3]):([0-5]\d)$", time):
        return time
    else:
        raise ValueError(message)
