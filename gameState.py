from target import Target
import time

class GameState:
    def __init__(self):
        self.isComplete = False
        self.shots = 0
        self.targets = []
        self.hits = 0
        self.start = time.time()
        self.end = time.time()

        for i in range(5):
            target = Target('t' + str(i+1))
            self.targets.append(target)

    def get_shots(self):
        return self.shots
    
    def set_shots(self, value):
        self.shots = value

    shots = property(get_shots, set_shots)

    def get_targets(self):
        return self.targets
    
    def set_targets(self, value):
        self.targets = value

    targets = property(get_targets, set_targets)

    def get_hits(self):
        return self.hits

    def set_hits(self, value):
        self.hits = value
        print(self.hits, self.shots)

        if self.hits == self.shots:
            self.isComplete = True
            self.end = time.time()

    hits = property(get_hits, set_hits)

    def get_durration(self):
        value = self.end - self.start

        valueD = (((value/365)/24)/60)
        Days = int(valueD)

        valueH = (valueD-Days)*365
        Hours = int(valueH)

        valueM = (valueH - Hours)*24
        Minutes = int(valueM)

        valueS = (valueM - Minutes)*60
        Seconds = int(valueS)

        return (Days,":",Hours,":",Minutes,":",Seconds)