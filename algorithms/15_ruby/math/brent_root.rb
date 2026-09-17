# Brent's Root Finding in Ruby (Numerical Recipes 3rd Ed. Chapter 9.3)

def brent_root(f, a, b, tol = 1e-10, max_iter = 100)
  fa = f.call(a)
  fb = f.call(b)
  raise "Root not bracketed" if fa * fb > 0

  a, b, fa, fb = b, a, fb, fa if fa.abs < fb.abs
  c, fc, d, s = a, fa, 0.0, b
  mflag = true

  max_iter.times do
    return b if fb.abs < tol || (b - a).abs < tol

    if fa != fc && fb != fc
      s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
          (b * fa * fc) / ((fb - fa) * (fb - fc)) +
          (c * fa * fb) / ((fc - fa) * (fc - fb))
    else
      s = b - fb * (b - a) / (fb - fa)
    end

    c1 = (s - (3 * a + b) / 4.0) * (s - b) > 0
    c2 = mflag && (s - b).abs >= (b - c).abs / 2.0
    c3 = !mflag && (s - b).abs >= (c - d).abs / 2.0

    if c1 || c2 || c3
      s = (a + b) / 2.0
      mflag = true
    else
      mflag = false
    end

    fs = f.call(s)
    d, c, fc = c, b, fb
    if fa * fs < 0
      b, fb = s, fs
    else
      a, fa = s, fs
    end

    a, b, fa, fb = b, a, fb, fa if fa.abs < fb.abs
  end
  b
end

r = brent_root(->(x) { x**2 - 2.0 }, 0.0, 2.0)
raise "Failed" if (r - Math.sqrt(2.0)).abs > 1e-6
puts "Ruby Brent Root Finding verified."
