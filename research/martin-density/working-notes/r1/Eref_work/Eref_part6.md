# E referee — part 6: numerical checks and final verdict list

## Numerical checks (scripts in Eref_work/scripts/, numpy only)
* block_check.py: finite block (n = 14, random Phi, zeta): computed J(zeta) by direct maximization of <w,zeta> over
  N(w) <= 1. Peak set equals the threshold rule |zeta(k)| >= Phi(k)^2 M |zeta|/C (Fact C; used in E 2.4 bands);
  off-peak formula w = C zeta/(Phi^2 |zeta|) holds to 2e-5 (optimizer precision). Single-coordinate certificate of
  Cor 5.2 (omega = c' e_k at an off-peak k): N(W(s)) - 1 <= (s^2/2) H (1 + kappa|s|) on |s| <= r, ratio -> 1 as s -> 0,
  with H = (||D omega||^2 - d^2)/C. OK.
* thm51_check.py: worst-case bookkeeping of Thm 5.1 (each averaged component saturating its bound) over 300 random
  (rho, K_0, kappa_0), t in [1e-6, 1e4], with E's exact choices of e1, J, t_*, s_J: no violation; worst normalized
  excess -6e-4. Note: the proof's case split matters — using the P4.5 bound for coarse components at |t| > t_*
  (which the proof does NOT do) produces violations; E's Step 2 correctly switches to the transfer bound there.

## Final verdicts
N1 correct | Thm 5.1 correct | Cor 5.2 correct (g_0 != 0: hypothesis to be made explicit) | box tails correct w/ gaps |
skeleton correct | rigidity correct (scope: linear decompositions) | critical cross candidate correct w/ gaps |
T1 unclear (Delta d != 0) | conversion bands correct | NC mate correct w/ gaps | T4 correct w/ gaps |
L6.1/C6.2 correct | L6.3 correct | L6.4 correct | P8.2 correct | Gordan correct w/ gaps (infinite families).
