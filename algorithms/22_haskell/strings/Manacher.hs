module Manacher (manacher) where

import Data.Array.ST (STArray, newListArray, readArray, writeArray, runSTArray)
import Control.Monad.ST (ST)

manacher :: String -> Int
manacher s = maximum (runSTArray $ do
  let t = '#' : concat [[c, '#'] | c <- s]
      n = length t
  arr <- newListArray (0, n - 1) t :: ST s (STArray s Int Char)
  p <- newListArray (0, n - 1) (replicate n 0) :: ST s (STArray s Int Int)
  let extend i = do
        pi' <- readArray p i
        if i + pi' + 1 < n && i - pi' - 1 >= 0 then do
          ca <- readArray arr (i + pi' + 1)
          cb <- readArray arr (i - pi' - 1)
          if ca == cb then writeArray p i (pi' + 1) >> extend i else return ()
        else return ()
      go i c r
        | i >= n = return ()
        | otherwise = do
            if i < r then do
              mir <- readArray p (2 * c - i)
              writeArray p i (min (r - i) mir)
            else return ()
            extend i
            pi'' <- readArray p i
            if i + pi'' > r then go (i + 1) i (i + pi'') else go (i + 1) c r
  go 0 0 0
  return p)

main :: IO ()
main = do
  if manacher "abba" == 4 && manacher "racecar" == 7
    then putStrLn "[Haskell Manacher] Longest palindromic substring verified"
    else error "Manacher verification failed"
