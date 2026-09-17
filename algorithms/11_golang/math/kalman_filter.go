// Package math implements 1D Kalman Filter (Numerical Recipes Ch. 15).
package math

type KalmanFilter1D struct {
	X float64 // state estimate
	P float64 // error covariance
	Q float64 // process noise
	R float64 // measurement noise
}

func NewKalmanFilter(x, p, q, r float64) *KalmanFilter1D {
	return &KalmanFilter1D{X: x, P: p, Q: q, R: r}
}

func (kf *KalmanFilter1D) Predict() {
	kf.P += kf.Q
}

func (kf *KalmanFilter1D) Update(z float64) float64 {
	k := kf.P / (kf.P + kf.R)
	kf.X += k * (z - kf.X)
	kf.P = (1.0 - k) * kf.P
	return kf.X
}
