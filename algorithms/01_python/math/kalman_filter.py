"""
1D Kalman Filter in Python (Numerical Recipes 3rd Ed. Chapter 15).
"""

class KalmanFilter1D:
    def __init__(self, x0, p0, q, r):
        self.x = x0
        self.p = p0
        self.q = q
        self.r = r

    def predict(self):
        self.p += self.q

    def update(self, z):
        k = self.p / (self.p + self.r)
        self.x += k * (z - self.x)
        self.p = (1.0 - k) * self.p
        return self.x

if __name__ == "__main__":
    kf = KalmanFilter1D(0.0, 1.0, 0.01, 0.1)
    for z in [0.9, 1.1, 0.95, 1.05]:
        kf.predict()
        kf.update(z)
    assert abs(kf.x - 1.0) < 0.2
    print("Python Kalman Filter verified.")
