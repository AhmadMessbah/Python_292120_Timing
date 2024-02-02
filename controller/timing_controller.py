class TimingController:
    def save(self,  name, family, username, password, role, status=True):
        pass


    def edit(self,  id, name, family, username, password, role, status):
        pass

    def remove(self, id):
        pass


    def find_all(self):
        pass


    def find_by_id(self, id):
        try:
            logging.info(f"FIND BY ID {id}")
            return self.da.find_by_id(id)
        except Exception as e:
            return False


    def find_by_username(self, username):
        try:
            return self.da.find_by_username(username)
        except Exception as e:
            return False


    def find_by_username_and_password(self, username, password):
        try:
            return self.da.find_by_username_and_password(username, password)
        except Exception as e:
            return False