# El Farol model (with the fixed rule)
# Arthur 1994

#%%
import matplotlib.pyplot as plt

#%%
# agent class which only has the fixed rule
class Fixed_rule_agent:
    def __init__(self):
        self.move_history = []
        self.happy_history = []
    
    def move(self, crowd_history):# 1:go, 0:stay
        if not crowd_history:
            self.current_move = 1
        elif crowd_history[-1] < 60:
            self.current_move = 1
        else:
            self.current_move = 0
        self.move_history.append(self.current_move)
        return self.current_move
    
    def happiness(self, crowd):
        if self.current_move == 0:
            self.current_happy = 0
        elif crowd >= 60:
            self.current_happy = -1
        else:
            self.current_happy = 1
        self.happy_history.append(self.current_happy)
        return self.current_happy


#%%
# bar class
class Bar:
    def __init__(self):
        self.costumer = []
    
    def count(self, agents):
        num_costumer = sum(agents)
        self.costumer.append(num_costumer)
        return num_costumer

#%%
# creating agent instances
agents = [Fixed_rule_agent() for i in range(100)]
# creating a El Farol instance
El_Farol = Bar()


#%%
for t in range(10):
    moves = [a.move(El_Farol.costumer) for a in agents]
    crowd = El_Farol.count(moves)
    happys = [a.happiness(crowd) for a in agents]

#%%
plt.plot(El_Farol.costumer)
plt.show()

