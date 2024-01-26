class MedicalService:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return str(self.__dict__)

