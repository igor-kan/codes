// Package math implements Brent's root-finding method (Numerical Recipes Ch. 9.3).
package math

import "math"

func BrentRoot(f func(float64) float64, a, b, tol float64, maxIter int) float64 {
	fa := f(a)
	fb := f(b)
	if fa*fb > 0 {
		panic("root not bracketed")
	}

	if math.Abs(fa) < math.Abs(fb) {
		a, b = b, a
		fa, fb = fb, fa
	}

	c := a
	fc := fa
	mflag := true
	var s, d float64

	for iter := 0; iter < maxIter; iter++ {
		if math.Abs(fb) < tol || math.Abs(b-a) < tol {
			return b
		}

		if fa != fc && fb != fc {
			s = (a*fb*fc)/((fa-fb)*(fa-fc)) +
				(b*fa*fc)/((fb-fa)*(fb-fc)) +
				(c*fa*fb)/((fc-fa)*(fc-fb))
		} else {
			s = b - fb*(b-a)/(fb-fa)
		}

		cond1 := (s-(3*a+b)/4)*(s-b) > 0
		cond2 := mflag && math.Abs(s-b) >= math.Abs(b-c)/2
		cond3 := !mflag && math.Abs(s-b) >= math.Abs(c-d)/2

		if cond1 || cond2 || cond3 {
			s = (a + b) / 2
			mflag = true
		} else {
			mflag = false
		}

		fs := f(s)
		d = c
		c = b
		fc = fb

		if fa*fs < 0 {
			b = s
			fb = fs
		} else {
			a = s
			fa = fs
		}

		if math.Abs(fa) < math.Abs(fb) {
			a, b = b, a
			fa, fb = fb, fa
		}
	}
	return b
}
