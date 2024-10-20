import random
import math

class Boson:
    isFermion = False

    def __init__(self, name, spin, momentum):
        self.name = name
        self.spin = spin
        self.momentum = momentum

    def PrintInfo(self):
        print(f"Name: {self.name}, Spin: {self.spin}, Momentum: {self.momentum}, isFermion: {Boson.isFermion}")

class Higgs(Boson):
    MassSigma = 1

    def __init__(self, momentum):
        super().__init__(name="Higgs", spin=0, momentum=momentum)
        self.MassMean = 125

    def Energy(self):
        mass = random.gauss(self.MassMean, Higgs.MassSigma)
        return math.sqrt(self.momentum**2 + mass**2)