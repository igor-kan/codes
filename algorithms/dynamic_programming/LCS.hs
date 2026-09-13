module Main where

import Data.Array

lcs :: String -> String -> Int
lcs xs ys = table ! (m, n)
  where
    m = length xs
    n = length ys
    xArr = listArray (1, m) xs
    yArr = listArray (1, n) ys

    table :: Array (Int, Int) Int
    table = array ((0, 0), (m, n)) [((i, j), entry i j) | i <- [0..m], j <- [0..n]]

    entry 0 _ = 0
    entry _ 0 = 0
    entry i j
      | xArr ! i == yArr ! j = table ! (i - 1, j - 1) + 1
      | otherwise             = max (table ! (i - 1, j)) (table ! (i, j - 1))

main :: IO ()
main = do
  let res = lcs "AGGTAB" "GXTXAYB"
  putStrLn $ "[Haskell LCS] LCS length: " ++ show res
