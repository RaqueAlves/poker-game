class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = []
        self.role = "normal"
        self.active = True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def chips(self):
        return self.__chips
    
    @chips.setter
    def chips(self, chips):
        self.__chips = chips

    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def active(self):
        return self.__active
    
    @active.setter
    def active(self, active):
        self.__active = active
