class Target:
    def __init__(self, name):
        self.name = name
        self.isHit = False
        self.isLit = False

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value

    name = property(get_name, set_name)

    def get_isHit(self):
        return self.isHit

    def set_isHit(self, value):
        self.isHit = value

    isHit = property(get_isHit, set_isHit)

    def get_isLit(self):
        return self.isLit

    def set_isLit(self, value):
        self.isLit = value

    isLit = property(get_isLit, set_isLit)

