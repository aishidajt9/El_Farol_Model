# El Farol model (with a bundle of rules)
# Arthur 1994

#%%
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from rule import rule # rule.py

#%%
class Agent:
    """defines a agent class"""
    def __init__(self, rule_nums):
        self.rule_currents = random.sample(rule_nums, random.choice(rule_nums) + 1)
        self.rules = [rule(i) for i in self.rule_currents]
        self.current_rule = None
    
    def rule_choice(self, crowd_history):
        if len(crowd_history) < 1:
            self.current_rule = random.choice(self.rules)
        else:
            performs = [r.performance for r in self.rules]
            maxperforms = [i for i, x in enumerate(performs) if x == max(performs)]
            self.current_rule = self.rules[random.choice(maxperforms)]
    
    def move(self, crowd_history):
        if self.current_rule.predict(crowd_history) >= 60:
            return 0
        else:
            return 1
    
    def evaluate(self, crowd_history):
        [r.evaluate(crowd_history) for r in self.rules]

#%%
# bar class
class Bar:
    """defines a bar class"""
    def __init__(self):
        self.costumer_history = []
    
    def count(self, agents):
        current_costumer = sum(agents)
        self.costumer_history.append(current_costumer)
        return current_costumer

#%%
###### simulation execution part ######

# number of rules, max 13 so far...
num_rule = 13
all_rule_nums = list(range(num_rule))
# creating agent instances
num_agent = 100
agents = [Agent(all_rule_nums) for i in range(num_agent)]
# creating a El Farol instance
El_Farol = Bar()

trial = 200
for t in range(trial):
    [a.rule_choice(El_Farol.costumer_history) for a in agents]
    moves = [a.move(El_Farol.costumer_history) for a in agents]
    El_Farol.count(moves)
    [a.evaluate(El_Farol.costumer_history) for a in agents]


#%%
# num of actual costumer visited the bar
plt.plot(El_Farol.costumer_history)
plt.ylim([0, 100])
plt.show()

#%%
# applied rule distribution at the last trial
last_rules = [a.current_rule.id for a in agents]
last_rules_dist = Counter(last_rules)
last_rules_dist = sorted(last_rules_dist.items(), key=lambda x:x[0])
rules, count = zip(*last_rules_dist)
plt.bar(rules, count)
plt.show()
