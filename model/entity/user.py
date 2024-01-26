class User:
    def __init__(self, name, family, username, password, role, status=True):
        self.id = None
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role
        self.status = status

    def __repr__(self):
        return str(self.__dict__)
