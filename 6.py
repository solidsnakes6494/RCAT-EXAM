import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function(theta, X, y):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    cost = -1 / m * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return cost

theta = np.zeros(X.shape[1])  
cost = cost_function(theta, X, y)
print("Cost:", cost)

"""
OUTPUT
Cost: 0.6931471805599452
"""
