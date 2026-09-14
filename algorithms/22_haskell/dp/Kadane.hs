module Kadane (kadane) where

kadane :: [Int] -> Int
kadane [] = error "kadane: empty list"
kadane (x:xs) = maximum (scanl (\cur y -> max y (cur + y)) x xs)

main :: IO ()
main = do
  if kadane [-2, 1, -3, 4, -1, 2, 1, -5, 4] == 6 && kadane [-5, -2, -3] == -2
    then putStrLn "[Haskell Kadane] Maximum subarray sum verified"
    else error "Kadane verification failed"
