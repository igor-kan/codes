package main

import (
	"fmt"
	"math"
)

func verlet(acceleration func(float64) float64, x0, v0, dt float64, steps int) (float64, float64) {
	x, v := x0, v0
	for i := 0; i < steps; i++ {
		a := acceleration(x)
		xNew := x + v*dt + 0.5*a*dt*dt
		aNew := acceleration(xNew)
		v = v + 0.5*(a+aNew)*dt
		x = xNew
	}
	return x, v
}

func main() {
	position, velocity := verlet(func(x float64) float64 { return -x }, 1, 0, 0.001, 10000)
	energy := 0.5 * (velocity*velocity + position*position)
	if math.Abs(energy-0.5) > 1e-3 || math.Abs(position-math.Cos(10)) > 1e-2 {
		panic("verlet failed")
	}
	fmt.Println("verlet ok")
}
