module LCS (lcs) where
lcs :: Eq a => [a] -> [a] -> Int
lcs [] _ = 0
lcs _ [] = 0
lcs (x:xs) (y:ys)
  | x==y = 1 + lcs xs ys
  | otherwise = max (lcs xs (y:ys)) (lcs (x:xs) ys)