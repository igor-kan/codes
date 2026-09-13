def sieve(n)
  is_prime = Array.new(n+1, true); is_prime[0]=is_prime[1]=false
  (2..Math.sqrt(n)).each { |i| (i*i..n).step(i) { |j| is_prime[j]=false } if is_prime[i] }
  (2..n).select { |i| is_prime[i] }
end