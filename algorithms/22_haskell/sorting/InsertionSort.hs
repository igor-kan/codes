module InsertionSort (insertionSort) where

insertionSort :: Ord a => [a] -> [a]
insertionSort = foldl ins []
  where
    ins [] x = [x]
    ins ys@(y:ys') x
      | x <= y = x : ys
      | otherwise = y : ins ys' x

main :: IO ()
main = do
  let data' = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19] :: [Int]
      sorted = insertionSort data'
  if sorted == [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]
    then putStrLn ("[Haskell InsertionSort] Insertion sort verified: " ++ show sorted)
    else error "InsertionSort verification failed"
