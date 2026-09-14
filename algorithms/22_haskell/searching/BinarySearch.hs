module BinarySearch (binarySearch) where

import Data.Array (Array, listArray, bounds, (!))

binarySearch :: Array Int Int -> Int -> Int
binarySearch arr target = go lo hi
  where
    (lo, hi) = bounds arr
    go l h
      | l > h = -1
      | arr ! m == target = m
      | arr ! m < target = go (m + 1) h
      | otherwise = go l (m - 1)
      where
        m = (l + h) `div` 2

main :: IO ()
main = do
  let arr = listArray (0, 6) [1, 3, 5, 7, 9, 11, 13]
  if binarySearch arr 7 == 3 && binarySearch arr 8 == -1 && binarySearch arr 1 == 0
    then putStrLn "[Haskell BinarySearch] Binary search verified"
    else error "BinarySearch verification failed"
