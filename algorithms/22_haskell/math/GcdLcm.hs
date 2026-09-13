module GcdLcm (gcd', lcm') where
import Prelude hiding (gcd, lcm)
gcd' :: Integral a => a -> a -> a
gcd' a 0 = a
gcd' a b = gcd' b (a `mod` b)
lcm' :: Integral a => a -> a -> a
lcm' a b = (a `div` gcd' a b) * b