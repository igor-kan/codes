-- Euclidean GCD in Lean 4
def gcd (a b : Nat) : Nat :=
  match b with
  | 0 => a
  | Nat.succ _ =>
    have : a % b < b := Nat.mod_lt a (Nat.zero_lt_succ _)
    gcd b (a % b)
termination_by b
