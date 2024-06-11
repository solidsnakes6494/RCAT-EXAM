import numpy as np

class LinearRegression:
    def fit(self, X, y, learning_rate=0.01, n_iterations=1000):
        n_samples, n_features = X.shape

        self.weights = np.zeros((n_features,1))

        self.bias = 0

        for _ in range(n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3*X + noise

model = LinearRegression()

model.fit(X, y)

X_new = np.array([[0], [2]])
predictions = model.predict(X_new)
print("Predictions:", predictions)
"""
OUTPUT
Predictions: [[ 3.78160501]
 [10.34691046]]
 """
