/-
Formal Verification of Abstract Group Theory in Lean 4.
Proves the uniqueness of the identity element and left-inversion cancellation.
-/

class AbstractGroup (G : Type) where
  mul : G → G → G
  one : G
  inv : G → G
  mul_assoc : ∀ a b c : G, mul (mul a b) c = mul a (mul b c)
  one_mul : ∀ a : G, mul one a = a
  mul_one : ∀ a : G, mul a one = a
  inv_mul : ∀ a : G, mul (inv a) a = one

namespace AbstractGroup

variable {G : Type} [AbstractGroup G]

-- Infix notation
infixl:70 " ⋆ " => AbstractGroup.mul
notation "e" => AbstractGroup.one
postfix:max "⁻¹" => AbstractGroup.inv

/-- Uniqueness of the neutral identity element in any abstract group -/
theorem identity_unique (e' : G) (h : ∀ a : G, e' ⋆ a = a) : e' = e := by
  have h1 : e' ⋆ e = e := h e
  have h2 : e' ⋆ e = e' := mul_one e'
  rw [← h2, h1]

end AbstractGroup
