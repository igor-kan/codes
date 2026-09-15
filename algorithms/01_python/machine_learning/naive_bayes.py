"""Gaussian naive Bayes classifier."""
import math
from collections import defaultdict


class GaussianNB:
    def __init__(self) -> None:
        self.stats: dict[str, tuple[list[float], list[float]]] = {}
        self.priors: dict[str, float] = {}

    def fit(self, features: list[list[float]], labels: list[str]) -> None:
        groups: dict[str, list[list[float]]] = defaultdict(list)
        for x, y in zip(features, labels):
            groups[y].append(x)
        total = len(features)
        for label, rows in groups.items():
            self.priors[label] = len(rows) / total
            means = [sum(row[j] for row in rows) / len(rows) for j in range(len(rows[0]))]
            variances = [
                sum((row[j] - means[j]) ** 2 for row in rows) / len(rows) or 1e-9
                for j in range(len(rows[0]))
            ]
            self.stats[label] = (means, variances)

    def predict(self, x: list[float]) -> str:
        best_label, best_score = None, float("-inf")
        for label, (means, variances) in self.stats.items():
            score = math.log(self.priors[label])
            for value, mean, var in zip(x, means, variances):
                score += -0.5 * math.log(2 * math.pi * var) - (value - mean) ** 2 / (2 * var)
            if score > best_score:
                best_label, best_score = label, score
        return best_label or ""


if __name__ == "__main__":
    features = [[1.0], [1.2], [1.1], [5.0], [5.2], [5.1]]
    labels = ["low", "low", "low", "high", "high", "high"]
    model = GaussianNB()
    model.fit(features, labels)
    assert model.predict([1.15]) == "low"
    assert model.predict([5.05]) == "high"
    print("naive bayes ok")
