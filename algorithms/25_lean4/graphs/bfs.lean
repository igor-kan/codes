-- Breadth-first search on adjacency list in Lean 4
-- Termination is proven by decreasing fuel parameter.

def bfsAux (graph : Nat -> List Nat) (fuel : Nat) (queue : List Nat)
    (visited : Nat -> Bool) (order : List Nat) : List Nat :=
  match fuel with
  | 0 => order.reverse
  | n + 1 =>
    match queue with
    | [] => order.reverse
    | u :: rest =>
      if visited u then
        bfsAux graph n rest visited order
      else
        let neighbors := graph u
        bfsAux graph n (rest ++ neighbors)
          (fun n' => if n' = u then true else visited n') (u :: order)
termination_by fuel

def bfs (graph : Nat -> List Nat) (start : Nat) (maxNodes : Nat) : List Nat :=
  bfsAux graph maxNodes [start] (fun _ => false) []

def exampleGraph : Nat -> List Nat
  | 1 => [2, 3]
  | 2 => [1, 4]
  | 3 => [1, 5]
  | 4 => [2]
  | 5 => [3]
  | _ => []

#eval bfs exampleGraph 1 10