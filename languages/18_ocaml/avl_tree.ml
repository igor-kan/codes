(* Functional Self-Balancing AVL Tree in OCaml *)

type 'a tree =
  | Empty
  | Node of 'a * int * 'a tree * 'a tree

let height = function
  | Empty -> 0
  | Node (_, h, _, _) -> h

let make_node v l r =
  Node (v, 1 + max (height l) (height r), l, r)

let balance_factor = function
  | Empty -> 0
  | Node (_, _, l, r) -> height l - height r

let rotate_right = function
  | Node (y, _, Node (x, _, a, b), c) -> make_node x a (make_node y b c)
  | t -> t

let rotate_left = function
  | Node (x, _, a, Node (y, _, b, c)) -> make_node y (make_node x a b) c
  | t -> t

let balance = function
  | Node (v, _, l, r) as t ->
      let bf = balance_factor t in
      if bf > 1 then
        if balance_factor l >= 0 then
          rotate_right t
        else
          rotate_right (make_node v (rotate_left l) r)
      else if bf < -1 then
        if balance_factor r <= 0 then
          rotate_left t
        else
          rotate_left (make_node v l (rotate_right r))
      else
        make_node v l r
  | Empty -> Empty

let rec insert x = function
  | Empty -> Node (x, 1, Empty, Empty)
  | Node (v, _, l, r) as t ->
      if x < v then balance (make_node v (insert x l) r)
      else if x > v then balance (make_node v l (insert x r))
      else t

let rec mem x = function
  | Empty -> false
  | Node (v, _, l, r) ->
      if x = v then true
      else if x < v then mem x l
      else mem x r
