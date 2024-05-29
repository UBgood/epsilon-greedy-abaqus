# Import required libraries 
import numpy as np 
import matplotlib.pyplot as plt 

# Define Action class 
class Arms: 
    def __init__(self, m): 
        #range values min and max. N remains and m defines its number. 
        self.m = m 
        self.mean = 0
        self.mini = 0
        self.maxi = 1
        self.N = 0

    # Choose a random action 
    def choose(self): 
        return np.random.randn() + self.m 

    # Update the action-value estimate
    #Update number of steps instead 
    def update(self, x): 
        self.N += 1
        self.mean = (1 - 1.0 / self.N)*self.mean + 1.0 / self.N * x 


def run_experiment(m1, m2, m3, eps, N): 
	
    arms = [Arms(m1), Arms(m2), Arms(m3)] 

    data = np.empty(N) 
        
    for i in range(N): 
        # epsilon greedy 
        p = np.random.random() 
        if p < eps: 
            j = np.random.choice(3) 
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
