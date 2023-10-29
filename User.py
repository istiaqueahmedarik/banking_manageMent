class User:
    def __init__(self, name, password, account):
        self.name = name
        self.password = password
        self.account = account
        self.power = 0
        self.loggedIn = False

    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setAccount(self, account):
        self.account = account
    def getAccount(self):
        return self.account
    def setPower(self, power):
        self.power = power
    def getPower(self):
        return self.power
    def setLoggedIn(self, loggedIn):
        self.loggedIn = loggedIn
    def getLoggedIn(self):
        return self.loggedIn
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
