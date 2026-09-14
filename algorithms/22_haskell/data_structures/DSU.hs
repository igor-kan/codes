module DSU (DSU, make, find, union, connected) where

import qualified Data.IntMap.Strict as M

type DSU = M.IntMap Int

make :: Int -> DSU
make n = M.fromList [(i, i) | i <- [0 .. n - 1]]

find :: DSU -> Int -> (Int, DSU)
find m x =
  case M.lookup x m of
    Nothing -> (x, m)
    Just p
      | p == x -> (x, m)
      | otherwise ->
          let (root, m') = find m p
          in (root, M.insert x root m')

union :: DSU -> Int -> Int -> DSU
union m x y =
  let (rx, m1) = find m x
      (ry, m2) = find m1 y
  in if rx == ry then m2 else M.insert ry rx m2

connected :: DSU -> Int -> Int -> Bool
connected m x y =
  let (rx, _) = find m x
      (ry, _) = find m y
  in rx == ry

main :: IO ()
main = do
  let m0 = make 5
      m1 = union m0 0 1
      m2 = union m1 1 2
      m3 = union m2 3 4
  if connected m3 0 2 && not (connected m3 0 3)
    then putStrLn "[Haskell DSU] Disjoint set union verified"
    else error "DSU verification failed"
