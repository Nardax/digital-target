from target import Target
import time

class GameState:
    def __init__(self):
        self.shots = 0
        self.targets = []
        self.hits = 0
        self.start = time.time()
        self.end = time.time()

        for i in range(5):
            target = Target('t' + str(i+1))
            self.targets.append(target)

    def reset(self):
        self.shots = 0
        self.hits = 0
        self.start = time.time()
        
        for t in self.targets:
            t.reset

    @property
    def allTargetsHit(self):
        for t in self.targets:
            if t.isHit == False:
                return False
        
        return True

    @property
    def isComplete(self):
        print(self.hits, self.shots)
        return (self.hits >= self.shots)

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