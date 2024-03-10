class LinearRegression:
    def __init__(self):
        # Initialize model parameters
        self.theta = None        # Coefficients
        self.alpha = 0.01        # Learning rate
        self.num_iterations = 1000  # Number of iterations for gradient descent
    
    def add_intercept(self, X):
        """Add intercept term to feature matrix."""
        ones = [[1] for _ in range(len(X))]
        return [[1] + x for x in X]
    
    def compute_cost(self, X, y, theta):
        """Compute the cost (mean squared error) for given theta."""
        m = len(y)
        predictions = [self.hypothesis(x, theta) for x in X]
        squared_errors = [(predictions[i] - y[i]) ** 2 for i in range(m)]
        cost = (1 / (2 * m)) * sum(squared_errors)
        return cost
    
    def hypothesis(self, x, theta):
        """Compute hypothesis (linear combination) for a single data point."""
        return sum([theta[i] * x[i] for i in range(len(x))])
    
    def gradient_descent(self, X, y):
        """Perform gradient descent to minimize cost function."""
        m = len(y)
        n = len(X[0])
        self.theta = [0] * n  # Initialize theta with zeros
        
        for _ in range(self.num_iterations):
            # Compute predictions
            predictions = [self.hypothesis(x, self.theta) for x in X]
            
            # Compute gradients
            gradients = [sum((predictions[i] - y[i]) * X[i][j] for i in range(m)) / m for j in range(n)]
            
            # Update theta using gradient descent
            self.theta = [self.theta[j] - self.alpha * gradients[j] for j in range(n)]
    
    def fit(self, X, y):
        """Fit the model to the training data."""
        X = self.add_intercept(X)
        self.gradient_descent(X, y)
    
    def predict(self, X):
        """Predict the target variable for new input data."""
        X = self.add_intercept(X)
        return [self.hypothesis(x, self.theta) for x in X]

# Example usage
# Create a LinearRegression object
model = LinearRegression()

# Example data
X_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 5, 4, 5]

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
X_test = [[6], [7]]
predictions = model.predict(X_test)
print(predictions)
