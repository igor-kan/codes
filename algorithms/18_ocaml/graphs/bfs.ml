module IntSet = Set.Make(Int)

let bfs graph start =
  let rec loop queue visited acc =
    match queue with
    | [] -> List.rev acc
    | u :: rest ->
        if IntSet.mem u visited then loop rest visited acc
        else
          let visited' = IntSet.add u visited in
          let neighbors = try List.assoc u graph with Not_found -> [] in
          loop (rest @ neighbors) visited' (u :: acc)
  in
  loop [start] IntSet.empty []
