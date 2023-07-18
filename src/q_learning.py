import numpy as np
class Game():
    def __init__(self):
        self.action = [-1, 1]
        self.state = list(range(0))
        self.reward = [-1 for i in range(9)]
        self.reward[0] = -100
        self.reward.append(100)
        self.score = 0
        self.currState = 2
    
    def reset(self):
        self.currState = 2
        self.score = 0
    
    def take_action(self, action):
        self.currState += action

        reward= self.reward[self.currState]
        self.score += reward 
        self.tp()
        return  reward, self.checkWin()
    

    
    def checkWin(self):
        if(self.score>=500):
            return 1
        elif(self.score<=-100):
            return -1
        else:
            return 0                   
    
    def tp(self):
        if(self.currState == 9 or self.currState == 0):
            self.currState = 3
    def pickRandomStep(self):
        return np.random.choice(self.action)
    def actionMap(self, action):
        if action >0:
            return 1
        else:
            return -1

class Model():
    # A hardcoded model for solving a custom made game
    def __init__(self,nEpisode, maxIter, decay, learningRate):
        self.qTable = np.zeros((10,2))
        self.nEpisode = nEpisode
        self.maxIter = maxIter
        self.env = Game()
        self.eps = 1
        self.decay = 0.005
        self.alpha = learningRate
        self.gamma = 0.8
    
    def epsGreedy(self, eps):
        prob = np.random.uniform(0,1)
        if prob>eps:
            return self.env.actionMap(np.argmax(self.qTable[self.env.currState]))
        else:
            return self.env.pickRandomStep()
        
    def ReLu(self,x):
        return max(0,x) 
    
    def reset(self):
        self.qTable = np.zeros((10,2))
        
    def train(self):
        for episode in range(self.nEpisode):
            print(f"episode {episode}")
            self.env.reset()
            eps = self.eps - self.decay*episode
            for iteration in range(self.maxIter):
                print(f"iteration {iteration}")
                # Pick an action
                previous_state = self.env.currState
                action = self.epsGreedy(eps)
                reward, condition = self.env.take_action(action)
                self.qTable[previous_state,self.ReLu(action)] = reward + \
                    self.alpha*( reward+self.gamma*max(self.qTable[self.env.currState]) - self.qTable[previous_state,self.ReLu(action)])
                print(self.qTable)
                if condition:
                    break
                
    
    def autoplay(self):
        self.env.reset()
        steps = []
        condition = 0
        while not condition:
            print(self.env.currState)
            print(self.env.reward)
        
            action = self.epsGreedy(0)
            steps.append(action)
            _, condition = self.env.take_action(action=action)
        print(steps)
    
    def printQTable(self):
        pass
                
                
                
        