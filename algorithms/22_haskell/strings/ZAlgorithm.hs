module ZAlgorithm (zAlgorithm) where

import Data.Array.ST (STArray, newListArray, readArray, writeArray, runSTArray)
import Control.Monad.ST (ST)

zAlgorithm :: String -> [Int]
zAlgorithm s = runSTArray $ do
  let n = length s
  arr <- newListArray (0, n - 1) s :: ST s (STArray s Int Char)
  z <- newListArray (0, n - 1) (replicate n 0) :: ST s (STArray s Int Int)
  if n > 0 then writeArray z 0 n else return ()
  let extend i = do
        zi <- readArray z i
        if i + zi < n then do
          ca <- readArray arr zi
          cb <- readArray arr (i + zi)
          if ca == cb then writeArray z i (zi + 1) >> extend i else return ()
        else return ()
      go i l r
        | i >= n = return ()
        | otherwise = do
            if i <= r then do
              zl <- readArray z (i - l)
              writeArray z i (min (r - i + 1) zl)
            else return ()
            extend i
            zi <- readArray z i
            if i + zi - 1 > r
              then go (i + 1) i (i + zi - 1)
              else go (i + 1) l r
  go 1 0 0
  return z

main :: IO ()
main = do
  if zAlgorithm "abacaba" == [7, 0, 1, 0, 3, 0, 1]
    then putStrLn "[Haskell ZAlgorithm] Z-algorithm verified"
    else error "ZAlgorithm verification failed"
