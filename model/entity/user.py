class User:
    def __init__(self, name, family, national_id, date_birth, phone_number, username, password, status=True):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.date_birth = date_birth
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.status = status

    def __repr__(self):
        return str(self.__dict__)
