module SelectionSort (selectionSort) where

selectionSort :: Ord a => [a] -> [a]
selectionSort [] = []
selectionSort xs =
  let m = minimum xs
  in m : selectionSort (removeOne m xs)
  where
    removeOne _ [] = []
    removeOne y (z:zs)
      | y == z = zs
      | otherwise = z : removeOne y zs

main :: IO ()
main = do
  let data' = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19] :: [Int]
      sorted = selectionSort data'
  if sorted == [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]
    then putStrLn ("[Haskell SelectionSort] Selection sort verified: " ++ show sorted)
    else error "SelectionSort verification failed"
