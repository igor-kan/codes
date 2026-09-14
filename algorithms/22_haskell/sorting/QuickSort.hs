module QuickSort (quickSort) where

quickSort :: Ord a => [a] -> [a]
quickSort [] = []
quickSort (p:xs) = quickSort [x | x <- xs, x < p] ++ [p] ++ quickSort [x | x <- xs, x >= p]

main :: IO ()
main = do
  let data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19] :: [Int]
      sorted = quickSort data
  if sorted == [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]
    then putStrLn ("[Haskell QuickSort] Functional quicksort verified: " ++ show sorted)
    else error "QuickSort failed verification"
