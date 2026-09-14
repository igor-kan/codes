-- Linear-time Tail-Recursive Fibonacci in Lean 4
def fibAux (n : Nat) (a b : Nat) : Nat :=
  match n with
  | 0 => a
  | n + 1 => fibAux n b (a + b)

def fib (n : Nat) : Nat :=
  fibAux n 0 1
