class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.iterations):
            for i in range(n_samples):
                y_predicted = sum(X[i][j] * self.weights[j] for j in range(n_features)) + self.bias
                error = y_predicted - y[i]
                for j in range(n_features):
                    self.weights[j] -= self.lr * (1 / n_samples) * X[i][j] * error
                self.bias -= self.lr * (1 / n_samples) * error

    def predict(self, X):
        return [sum(x[j] * self.weights[j] for j in range(len(x))) + self.bias for x in X]
