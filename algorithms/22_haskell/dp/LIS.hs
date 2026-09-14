module LIS (lis) where

import Data.Array (listArray, (!), elems)

lis :: [Int] -> Int
lis [] = 0
lis xs = maximum (elems dp)
  where
    n = length xs
    arr = listArray (0, n - 1) xs
    dp = listArray (0, n - 1)
           [ 1 + maximum (0 : [dp ! j | j <- [0 .. i - 1], arr ! j < arr ! i])
           | i <- [0 .. n - 1] ]

main :: IO ()
main = do
  if lis [10, 9, 2, 5, 3, 7, 101, 18] == 4 && lis [] == 0
    then putStrLn "[Haskell LIS] Longest increasing subsequence verified"
    else error "LIS verification failed"
