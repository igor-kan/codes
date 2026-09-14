module CountingSort (countingSort) where

import Data.Array (accumArray, (!))

countingSort :: [Int] -> [Int]
countingSort [] = []
countingSort xs =
  let mx = maximum xs
      count = accumArray (+) 0 (0, mx) [(x, 1) | x <- xs]
  in concat [replicate (count ! i) i | i <- [0 .. mx]]

main :: IO ()
main = do
  let data' = [4, 2, 2, 8, 3, 3, 1]
      sorted = countingSort data'
  if sorted == [1, 2, 2, 3, 3, 4, 8]
    then putStrLn ("[Haskell CountingSort] Counting sort verified: " ++ show sorted)
    else error "CountingSort verification failed"
