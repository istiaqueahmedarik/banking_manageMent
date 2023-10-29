from User import User


class Admin(User):
    def __init__(self, name, password, account):
        super().__init__(name, password, account)
        self.power = 1
