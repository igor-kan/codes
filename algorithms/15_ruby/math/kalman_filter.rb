# 1D Kalman Filter in Ruby (Numerical Recipes 3rd Ed. Chapter 15)

class KalmanFilter1D
  attr_accessor :x, :p, :q, :r
  def initialize(x, p, q, r)
    @x = x; @p = p; @q = q; @r = r
  end

  def predict
    @p += @q
  end

  def update(z)
    k = @p / (@p + @r)
    @x += k * (z - @x)
    @p = (1.0 - k) * @p
    @x
  end
end

kf = KalmanFilter1D.new(0.0, 1.0, 0.01, 0.1)
[0.9, 1.1, 0.95, 1.05].each do |z|
  kf.predict
  kf.update(z)
end
raise "Failed" if (kf.x - 1.0).abs > 0.2
puts "Ruby Kalman Filter verified."
