 # I found the answer in dropbox and worked backwards

 # import packages
import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5
start_val = 0
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

 
 # create function to generate a straight line
def generate_straight_line(X, params = np.array([2, -5])):
    
    X_input = np.empty((2, X.shape[0]))
    X_input[0,:] = X
    X_input[1,:] = 1
    
    print(params.shape) # print to console
    print(X_input.shape) # print to console
    return np.dot(params, X_input) # return values




plt.figure() # generate figure
plt.plot(X, generate_straight_line(X)) # plot function
plt.title("f(x) = 2x - 5") # add title
plt.xlabel("X") # add x axis label
plt.ylabel("Y") # add y axis label
plt.savefig("answer.png") # give image a name