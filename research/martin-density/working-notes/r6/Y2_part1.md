# Y2 part 1: plan and the key new idea (tuning companions instead of steering)

Setting: note paper/martin_density_note.tex (Sections 1, 7, 8), F finite, I = {1..N}, SLD-type designs (SLD, SLD_G made
N-free, D''', explosive): only (T-a)-(T-d), (P1)-(P3) and allowedness (a),(b) are used.

## 1. Diagnosis of the steering gap (Z4 referee Observation 9.1)
Theorem thm:engineered uses, for |tau| <= s_1, the averaged ("theta") data, for BOTH signs of tau.  Any data used at
|tau| <= s_1 must have the same block amplitudes on every carrier with an infinite signature tail (otherwise the truncation
beyond N'' costs first order |tau| V_{>N''}), so at a used degenerate peak k the theta-type datum omega^c(k) is forced
(up to O(Kt)/lambda_k) and is outward for one sign of tau unless omega^c(k) = 0.  Re-decomposing g' at f' cannot remove
the k-component (moving it to the base creates a first-order level mismatch of size |tau| lambda_k u_k(xhat'), i.e. O(|tau|),
because q_k = Phi M/(mC) > 0).  Hence at an engineered approximant f' of f itself the used degenerate peaks must be strict
non-peaks with gap' >= 2 rho s_1 |omega^c(k)| (quantitative steering), and steering channels at f' are limited (first-order
cost on every coordinate carrying base switching; e-channels need a Gordan condition on the Gram form
G(v,w) = <P^perp U* v, P^perp U* w>, which can fail for special U).  HEURISTIC/PROVED mixture; not used below.

## 2. The way out: steer at a COMPANION, not at the approximant
Z3 Theorem E (PROVED, refereed) accepts exact d-neutral two-piece window data at nearby first rows f_j (same base support)
with p*(f_j - f) = o((bottom window scale)^2), and then applies Corollary cor:D1 AT f_j (fixed data, no gap lower bound).
New ingredient (Y2, PROVED in part 2): the THRESHOLD of a block, theta(zeta) = |zeta| M/C, is characterized by
   |zeta| = sum_k (|zeta(k)| - theta Phi_k^2)_+ ,   |zeta|^2 = sum_k Phi_k^2 min(theta, |zeta(k)|/Phi_k^2)^2,
so theta is the unique root of an explicit strictly monotone equation, and it STRICTLY INCREASES when |zeta(k')| is
increased at a peak k' or decreased (from a nonzero value) at a strict non-peak k'; at a degenerate peak ANY change raises it.
A companion f_j := first row with data (a, z + delta), delta supported on far coordinates of a "donor" signature set
(disjoint from every support used by the window data), raises the thresholds of the relevant blocks without changing any
value u_l(zhat) of a used carrier.  Consequences: every used degenerate swallowing-type peak becomes a strict non-peak of f_j
(tiny gap), the switching stays EXACTLY d-neutral at f_j (d-coefficients of used carriers are multiplied by a common factor
per block), b^+-(xi_j) = 0, and the data are exact two-piece data at f_j with inward-only (third-kind) coordinates.
Theorem E (with the inward-only extension of Lemma U) then recovers (f, rho g).  The size of the gap at f_j is irrelevant.

## 3. Items
(1)/(2) = degenerate swallowing-type peaks (rigid or not) : Theorem P (part 3), hypothesis (TD) = threshold donors,
          automatically satisfied under (H2'') in blocks with non-rigid degenerate peaks except an explicit corner case.
(3) mixed blocks / Conjecture G : part 4+.
(4) failure of (H2'') : part 5+.
