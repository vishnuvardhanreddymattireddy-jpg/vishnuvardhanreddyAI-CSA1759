import numpy as np

# XOR input
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# XOR output
Y = np.array([[0],
              [1],
              [1],
              [0]])

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights randomly
np.random.seed(1)
weights_input_hidden = np.random.uniform(size=(2,4))
weights_hidden_output = np.random.uniform(size=(4,1))

# Training
learning_rate = 0.1
epochs = 10000

for _ in range(epochs):
    
    # Forward propagation
    hidden_layer = sigmoid(np.dot(X, weights_input_hidden))
    output_layer = sigmoid(np.dot(hidden_layer, weights_hidden_output))
    
    # Error
    error = Y - output_layer
    
    # Backpropagation
    d_output = error * sigmoid_derivative(output_layer)
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer)
    
    # Update weights
    weights_hidden_output += hidden_layer.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate

# Predictions
print("Predictions:")
print(np.round(output_layer))
