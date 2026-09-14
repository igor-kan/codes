let rec merge l1 l2 =
  match (l1, l2) with
  | [], l | l, [] -> l
  | h1 :: t1, h2 :: t2 ->
      if h1 <= h2 then h1 :: merge t1 l2
      else h2 :: merge l1 t2

let rec split = function
  | [] -> ([], [])
  | [x] -> ([x], [])
  | x :: y :: rest ->
      let l1, l2 = split rest in
      (x :: l1, y :: l2)

let rec merge_sort = function
  | [] -> []
  | [x] -> [x]
  | lst ->
      let l1, l2 = split lst in
      merge (merge_sort l1) (merge_sort l2)
