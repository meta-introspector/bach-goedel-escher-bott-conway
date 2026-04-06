import Mathlib.NumberTheory.ModularForms.Basic

open UpperHalfPlane

/-- A modular form of weight `k` and level `Γ` is a holomorphic function 
on the upper half-plane that is invariant under the weight `k` slash action 
of `Γ` and is bounded at the cusps. -/
structure ModularForm (Γ : Subgroup (GL (Fin 2) ℝ)) (k : ℤ) extends SlashInvariantForm Γ k : Type where
  holo' : MDiff ⇑toSlashInvariantForm
  bdd_at_cusps' {c : OnePoint ℝ} (hc : IsCusp c Γ) : c.IsBoundedAt toFun k
