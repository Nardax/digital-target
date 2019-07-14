class Target:
    def __init__(self, name):
        self._name = name
        self._isHit = False
        self._isLit = False

    def reset(self):
        self._isHit = False
        self._isLit = False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def isHit(self):
        return self._isHit

    @isHit.setter
    def isHit(self, value):
        self._isHit = value

    @property
    def isLit(self):
        return self._isLit

    @isLit.setter
    def isLit(self, value):
        self._isLit = value

