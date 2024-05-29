# Import required libraries 
import numpy as np 
import matplotlib.pyplot as plt 

# Define Action class 
class Arms: 
    def __init__(self, m): 
        #range values min and max. N remains and m defines its number. 
        self.m = m  #fixed reward vale for action
        self.mean = 0 # mean reward of the action
        #self.mini = 0
        #self.maxi = 1
        self.N = 0 (number of iterations)

    # Choose a random action 
    def choose(self): 
        return np.random.randn() + self.m #means the random action gets mean reward

    # Update the action-value estimate
    #Update number of steps instead 
    def update(self, x): 
        self.N += 1
        self.mean = (1 - 1.0 / self.N)*self.mean + 1.0 / self.N * x # then it is updated into the iteration


def run_experiment(m1, m2, m3, eps, N): #eps is the ideal value we try to maintain possibilly over n iterations 
    arms = [Arms(m1), Arms(m2), Arms(m3)] # list of range of values 

    data = np.empty(N) 
        
    for i in range(N): 
        # epsilon greedy 
        p = np.random.random() #take arbitrary action
        if p < eps: #let p be the deformation value which could be a range 

            j = np.random.choice(3) #The purpose of using np.random.choice(3) in this context is to ensure that during the exploration phase, the algorithm randomly selects one of the three actions, providing a way to gather more information about all actions rather than sticking to the currently known best action.
        else: 
            j = np.argmax([a.mean for a in arms]) 
        x = arms[j].choose() 
        arms[j].update(x) 
     
        

        # for the plot 
    data[i] = x 
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1) 

    # plot moving average ctr 
    # plt.plot(cumulative_average) 
    # plt.plot(np.ones(N)*m1) 
    # plt.plot(np.ones(N)*m2) 
    # plt.plot(np.ones(N)*m3) 
    # plt.xscale('log') 
    # plt.show() 

    for a in arms: 
        print(a.mean) 

    return cumulative_average 



if __name__ == '__main__': 
	
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000) 
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000) 
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000) 
