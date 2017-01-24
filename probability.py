import random
import time
from collections import defaultdict


class Coin:
    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.state = ''

    def flip(self):
        flip = random.randrange(0, 2)
        if flip == 0:
            self.state = "Tail"
            self.tails += 1
        else:
            self.state = "Head"
            self.heads += 1
        return str(self.state)

    def simulate(self, trials, save=None):
        text = ''
        for i in range(trials):
            flip = self.flip()
            text += str(i+1).rjust(len(str(trials))) + '. ' + flip + '\n'

        heads = round(self.heads / trials, 4) * 100
        tails = round(self.tails / trials, 4) * 100

        if save:
            filename = "tests/simulation_" + time.strftime("%Y%m%d_%H%M")
            test_file = open(filename+".txt", "w")
            test_file.write("Trials: {}\n".format(trials))
            test_file.write("Heads: {}, {}%\n".format(self.heads, heads))
            test_file.write("Tails: {}, {}%\n\n".format(self.tails, tails))
            test_file.write(text)

            test_file.close()

        print("Heads: {}, {}%".format(self.heads, heads))
        print("Tails: {}, {}%".format(self.tails, tails))


class Dice:
    """An abstraction of a regular 6-sided dice."""
    def simulate(self, trials):
        """
        Roll dice for the number of trials and return the counts.
        :param trials: number of times to roll dice
        :return: dict
        """
        sides = defaultdict(int)
        for i in range(trials):
            side = self.roll()
            sides[side] += 1
        return dict(sides)

    @staticmethod
    def roll():
        return random.randint(1, 6)


def main():
    # coin = Coin()
    # print(coin.flip())
    # coin.simulate(1000, True)

    dice = Dice()
    print(dice.simulate(100))


if __name__ == '__main__':
    main()
