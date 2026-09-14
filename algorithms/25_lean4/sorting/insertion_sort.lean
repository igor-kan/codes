-- Insertion sort in Lean 4 with termination proof

def insertSorted (x : Nat) (xs : List Nat) : List Nat :=
  match xs with
  | [] => [x]
  | h :: t =>
    if x <= h then x :: h :: t
    else h :: insertSorted x t
termination_by xs

def insertionSort (xs : List Nat) : List Nat :=
  match xs with
  | [] => []
  | h :: t => insertSorted h (insertionSort t)
termination_by xs

#eval insertionSort [3, 1, 4, 1, 5, 9, 2, 6]
#eval insertionSort [1, 2, 3, 4, 5]
#eval insertionSort [5, 4, 3, 2, 1]
#eval insertionSort ([] : List Nat)