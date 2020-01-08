import matplotlib.pyplot as plt
import sys
import matplotlib
from Model import Model
from GUI import GUI


class Environment(Model):
    def __init__(self):
        Model.__init__(self)
        self.make_param('Wepsen', 0)

    def reset(self):
        self.Wepsen = 0

    def draw(self):
        pass
        # plt.cla()


if __name__ == "__main__":
    Env = Environment()
    cx = GUI(Env)
    cx.start()
