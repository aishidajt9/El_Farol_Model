import random
import numpy as np

class rule:
    """defines a rule class which is differentiated by id number"""
    def __init__(self, id):
        self.id = id
        self.performance = 0

    def predict(self, hist):
        if self.id == 0: # the same as last week's
            if len(hist) < 1:
                return random.randint(0, 100)
            else:
                return hist[-1]
        if self.id == 1: # a mirror image around 50 of last week's
            if len(hist) < 1:
                return random.randint(0, 100)
            else:
                return 100 - hist[-1]
        if self.id == 2: # an average of the last four weeks
            if len(hist) < 1:
                return random.randint(0, 100)
            else:
                return np.mean(hist[-4:])
        if self.id == 3: # the trend in last 8 weeks, bounded by 0, 100
            if len(hist) < 2:
                return random.randint(0, 100)
            else:
                t = list(range(len(hist[-8:])))
                lm = np.polyfit(t, hist[-8:], 1)
                pred = np.poly1d(lm)(len(hist[-8:]))
                return min(100, max(0, pred))
        if self.id == 4: # the same as 2 weeks ago
            if len(hist) < 2:
                return random.randint(0, 100)
            else:
                return hist[-2]
        if self.id == 5: # the same as 5 weeks ago
            if len(hist) < 5:
                return random.randint(0, 100)
            else:
                return hist[-5]
        if self.id == 6: # always 100
            return 100
        if self.id == 7: # always 0
            return 0
        if self.id == 8: # always random
            return random.randint(0, 100)
        if self.id == 9: # an average of the entire weeks
            if len(hist) < 1:
                return random.randint(0, 100)
            else:
                return np.mean(hist)
        if self.id == 10: # the trend in the entire weeks, bounded by 0, 100
            if len(hist) < 2:
                return random.randint(0, 100)
            else:
                t = list(range(len(hist)))
                lm = np.polyfit(t, hist, 1)
                pred = np.poly1d(lm)(len(hist))
                return min(100, max(0, pred))
        if self.id == 11: # an average of the last eight weeks
            if len(hist) < 1:
                return random.randint(0, 100)
            else:
                return np.mean(hist[-8:])
        if self.id == 12: # the trend in last 4 weeks, bounded by 0, 100
            if len(hist) < 2:
                return random.randint(0, 100)
            else:
                t = list(range(len(hist[-4:])))
                lm = np.polyfit(t, hist[-4:], 1)
                pred = np.poly1d(lm)(len(hist[-4:]))
                return min(100, max(0, pred))
        
    def evaluate(self, crowd_history):
        self.last_pred = self.predict(crowd_history[:-1])

        if self.last_pred >= 60:
            self.last_happy = 0
        elif crowd_history[-1] >= 60:
            self.last_happy = -1
        else:
            self.last_happy = 1
        self.performance += self.last_happy

if __name__ == "__main__":
    # test
    crowd_history = [44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22, 35]
    r = rule(0)
    for t in range(len(crowd_history)):
        r.predict(crowd_history[0:t])
        r.evaluate(crowd_history[0:(t+1)])
        print(r.last_pred, r.last_happy, r.performance)
