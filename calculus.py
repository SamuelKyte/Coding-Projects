"""I'm definitely not a calc wiz. I used the textbook and also found the calc answers within dropbox. I worked backwards from the given answers to understand the workings of the functions."""

# NumPy is our numerical computational framework
import numpy as np

X = np.array([1, 2.5, 3, 3.25, 6, 8, 9.4])
y = np.array([0, 5, 7, 6.5, 9.5, 23.5, 18.7])

def model(x, m):
    """
    Our model f(x) = mx
    Receives: a data point x and the line gradient m
    Returns: a prediction for y
    """
    return x * m # f(x) = mx

def error_function(m):
    """
    Our error function J(m)
    This is done using the Mean Square Error (MSE) between our model and the data
    Receives: m, the gradient of the line
    Returns: J(m), the Mean Squared Error between the model and the data
    Hint: you can use the data itself (X and y) from this function
    """
     # Mean**2 Error Function
    numer = 0 # numerator
    n = len(X) # n =to the number of data points
    for i in range(n): # grab specific values from arrays
        x_data = X[i]
        y_data = y[i]
        
        numer += (y_data - model(x_data, m))**2 # mean**2 Error Function top

    return numer / n # return full function

def derivative(m):
     # https://towardsdatascience.com/gradient-descent-from-scratch-e8b75fa986cc
    """
    The derivation of the error_function J(m)
    Receives: m, the gradient of the line
    Returns: dJ/dm, the derivative of the error function with respect to m
    """
    # Derivation of Mean**2 Error Function
    numer = 0 # numerator
    n = len(X) # n =to the number of data points
    for i in range(n): # grab specific values from arrays
        x_data = X[i]
        y_data = y[i]

        # Calculate inner expression
        bracket = y_data - model(x_data, m) # inside of brackets
        numer += -2 * x_data * bracket # top of derivation
    
    return numer / n # return full function

def update_step(m, learning_rate=0.01):
    """
    Update the gradient m using the derivative of J(m)
    Receives: m, the gradient of the line
    Returns: a new and updated m
    """
    
    # How much to change m
    derivation = derivative(m) # derivative of m
    amount = learning_rate * derivation # derivation mult by learning rate

    # Change m
    return m - amount # return change

 # The below was already given within the calculus.py
m = -6
n_epochs = 5 # This is just the number of update steps you take

# Iterate for n epochs
for epoch in range(n_epochs):
    # Update and print m
    m = update_step(m)
    print(f'Epoch {epoch + 1}: m = {round(m,2)} and loss = {round(error_function(m), 2)}')

# Print Final Results
print("-----------------")
print("FINAL RESULTS")
print("-----------------")

print(f'm = {round(m,2)} and loss = {round(error_function(m), 2)}')


print("-----------------")