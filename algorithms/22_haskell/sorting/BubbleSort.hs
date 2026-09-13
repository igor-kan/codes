module BubbleSort (bubbleSort) where
bubbleSort :: Ord a => [a] -> [a]
bubbleSort [] = []
bubbleSort xs = let (xs', swapped) = pass xs
                in if swapped then bubbleSort xs' else xs'
  where
    pass [] = ([], False)
    pass [x] = ([x], False)
    pass (x:y:rest)
      | x > y = let (r,_) = pass (x:rest) in (y:r, True)
      | otherwise = let (r,s) = pass (y:rest) in (x:r, s)