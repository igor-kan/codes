module MergeSort (mergeSort) where
mergeSort :: Ord a => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right)
  where (left, right) = splitAt (length xs `div` 2) xs
        merge [] r = r
        merge l [] = l
        merge (x:xs) (y:ys) = if x<=y then x:merge xs (y:ys) else y:merge (x:xs) ys