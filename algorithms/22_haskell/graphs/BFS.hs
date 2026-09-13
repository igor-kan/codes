module BFS (bfs) where
import qualified Data.Map as M
import qualified Data.Set as S
import Data.Maybe (fromMaybe)
bfs :: Ord a => M.Map a [a] -> a -> [a]
bfs graph start = go [start] (S.singleton start) []
  where go [] _ acc = reverse acc
        go (x:xs) visited acc =
          let neighbors = filter (`S.notMember` visited) (fromMaybe [] (M.lookup x graph))
              visited' = foldr S.insert visited neighbors
          in go (xs ++ neighbors) visited' (x:acc)