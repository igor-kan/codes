import math
import random

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = []

    def fit(self, X):
        self.centroids = random.sample(X, self.k)
        for _ in range(self.max_iters):
            clusters = [[] for _ in range(self.k)]
            for x in X:
                distances = [math.dist(x, c) for c in self.centroids]
                closest_idx = distances.index(min(distances))
                clusters[closest_idx].append(x)
            
            new_centroids = []
            for cluster in clusters:
                if not cluster:
                    new_centroids.append(random.choice(X))
                else:
                    new_centroids.append([sum(dim) / len(cluster) for dim in zip(*cluster)])
            
            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids

    def predict(self, X):
        predictions = []
        for x in X:
            distances = [math.dist(x, c) for c in self.centroids]
            predictions.append(distances.index(min(distances)))
        return predictions
