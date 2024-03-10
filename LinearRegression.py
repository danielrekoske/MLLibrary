import numpy as np

class LinearRegression:
    def __init__(self):
        self.theta = None
        self.alpha = 0.01 
        self.num_iterations = 1000 
    
    @staticmethod
    def add_intercept(X):
        return np.hstack((np.ones((X.shape[0], 1)), X))
    
    @staticmethod
    def compute_cost(X, y, theta):
        m = len(y)
        h = np.dot(X, theta)
        cost = (1 / (2 * m)) * np.sum((h - y) ** 2)
        return cost
    
    def gradient_descent(self, X, y):
        m, n = X.shape
        self.theta = np.zeros(n)
        
        for _ in range(self.num_iterations):
            h = np.dot(X, self.theta)
            self.theta -= (self.alpha / m) * np.dot(X.T, (h - y))
    
    def fit(self, X, y):
        X = self.add_intercept(X)
        self.gradient_descent(X, y)
    
    def predict(self, X):
        X = self.add_intercept(X)
        return np.dot(X, self.theta)
