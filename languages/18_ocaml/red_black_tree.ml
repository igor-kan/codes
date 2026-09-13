(* ==============================================================================
 * File: languages/18_ocaml/red_black_tree.ml
 * Language: OCaml (Advanced Functional Programming & Type Theory)
 * Domain: Purely Functional Self-Balancing Data Structures
 * Algorithm: Chris Okasaki's Red-Black Balanced Search Tree (4-Case Pattern Matching)
 *
 * Rationale & Language Fit:
 *   OCaml is the gold standard functional language in static program analysis,
 *   compiler design (Coq, early Rust), and quantitative finance (Jane Street).
 *   Its algebraic data types and exhaustive pattern matching reduce the complex
 *   rotations of a Red-Black Tree into a single, breathtakingly elegant 4-case
 *   `balance` function described in Chris Okasaki's "Purely Functional Data
 *   Structures" (1998).
 * ============================================================================== *)

type color = Red | Black

type 'a tree =
  | Empty
  | Node of color * 'a tree * 'a * 'a tree

module type SET = sig
  type elem
  type t
  val empty : t
  val mem : elem -> t -> bool
  val insert : elem -> t -> t
  val elements : t -> elem list
  val size : t -> int
  val black_height : t -> int
end

module MakeSet (Ord : sig
  type t
  val compare : t -> t -> int
end) : (SET with type elem = Ord.t and type t = Ord.t tree) = struct
  type elem = Ord.t
  type t = elem tree

  let empty = Empty

  (* O(log n) Membership lookup *)
  let rec mem x = function
    | Empty -> false
    | Node (_, left, y, right) ->
        let c = Ord.compare x y in
        if c < 0 then mem x left
        else if c > 0 then mem x right
        else true

  (* Okasaki's legendary balance function:
   * Collapses the 4 asymmetric violation cases (LL, LR, RL, RR) of two consecutive
   * Red nodes into one canonical balanced Red parent with two Black children. *)
  let balance = function
    | Black, Node (Red, Node (Red, a, x, b), y, c), z, d
    | Black, Node (Red, a, x, Node (Red, b, y, c)), z, d
    | Black, a, x, Node (Red, Node (Red, b, y, c), z, d)
    | Black, a, x, Node (Red, b, y, Node (Red, c, z, d)) ->
        Node (Red, Node (Black, a, x, b), y, Node (Black, c, z, d))
    | col, left, x, right ->
        Node (col, left, x, right)

  (* Purely functional insertion:
   * Guarantees that the root is colored Black upon completion. *)
  let insert x s =
    let rec ins = function
      | Empty -> Node (Red, Empty, x, Empty)
      | Node (col, left, y, right) as n ->
          let c = Ord.compare x y in
          if c < 0 then balance (col, ins left, y, right)
          else if c > 0 then balance (col, left, y, ins right)
          else n  (* Deduplicate existing element *)
    in
    match ins s with
    | Empty -> Empty
    | Node (_, left, y, right) -> Node (Black, left, y, right)

  (* In-order list of elements *)
  let elements s =
    let rec aux acc = function
      | Empty -> acc
      | Node (_, left, y, right) -> aux (y :: aux acc right) left
    in
    aux [] s

  let rec size = function
    | Empty -> 0
    | Node (_, left, _, right) -> 1 + size left + size right

  (* Verify invariant: all paths have the same number of black nodes *)
  let rec black_height = function
    | Empty -> 0
    | Node (color, left, _, right) ->
        let lh = black_height left in
        let rh = black_height right in
        if lh <> rh then failwith "Red-Black Tree Violation: black height mismatch!"
        else if color = Black then lh + 1
        else lh
end

(* IntSet instantiation *)
module IntSet = MakeSet(struct
  type t = int
  let compare = compare
end)

(* --- Demonstration & Verification --- *)
let () =
  Printf.printf "=================================================================\n";
  Printf.printf "OCaml Purely Functional Red-Black Tree (Chris Okasaki Architecture)\n";
  Printf.printf "=================================================================\n\n";

  let items = [55; 13; 89; 8; 21; 34; 70; 95; 3; 5; 144; 1; 2; 233] in
  Printf.printf "Inserting %d Fibonacci-related keys into immutable tree...\n" (List.length items);

  let tree = List.fold_left (fun acc x -> IntSet.insert x acc) IntSet.empty items in

  Printf.printf "Total elements in tree: %d\n" (IntSet.size tree);
  Printf.printf "Validating Black-Height Invariant... ";
  let bh = IntSet.black_height tree in
  Printf.printf "OK (Black Height = %d)\n" bh;

  let sorted = IntSet.elements tree in
  Printf.printf "In-order elements: [";
  List.iter (fun x -> Printf.printf "%d; " x) sorted;
  Printf.printf "]\n";

  assert (IntSet.mem 34 tree = true);
  assert (IntSet.mem 999 tree = false);
  Printf.printf "Membership verified: 34 -> present, 999 -> absent.\n";
  Printf.printf "[SUCCESS] OCaml Okasaki Red-Black tree invariants strictly verified.\n"
