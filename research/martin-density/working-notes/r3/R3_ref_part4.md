# R3 referee, part 4: closure route (3.2), residual class O3* (5.1), chain and coarsest guards (5.2), numerics of 4.7

## 4.1 Peak-cost formula, numerical check. CONFIRMED (refwork/peakcost.py).
Finite block, n = 12, Phi geometric, peaks at +-M with M + C = 1, alpha(k) = sigma delta Phi^2 M/C, inward Omega = omega e_k - d w:
excess N(w+t Omega) - 1 - t<Omega, zeta/|zeta|> = 1.3795e-6 vs predicted 1.3772e-6 (t = 1e-3) and 1.37747e-7 vs 1.37724e-7
(t = 1e-4) — agreement up to O(t^2), three random trials.

## 4.2 Closure route (3.2). (a) CORRECT (definitional consequence of Prop Z); (b) HEURISTIC, fairly labelled;
(c) arithmetic CORRECT given (b): under "converted coordinates have total depth sum lambda_k <= C eps", carrying kappa t
at scale t needs sum M lambda_k/t >= kappa t, i.e. t <= sqrt(M C eps/kappa), the slack scale; so an implant inequality can
only constrain O(1) components. (d) HEURISTIC. One addition: by part 3, a valid K(f) could also encode the room/Hilbert
capacity of two-sided carriers below the destruction boundary (an O(1)-component quantity, so not excluded by (c)).

## 4.3 Residual class O3* (5.1). OPEN, HEURISTIC formulation; INCOMPLETE as a description of what remains.
(R1)-(R5) are a reasonable description of what defeats EC for the ERROR part (escaping, late-scheduled, guarded errors).
Check of (R1): the profile split r_lambda = r_inf + (escaping part) along a boundary sequence is legitimate; r_inf is a
property of f (fixed) and can be targeted by EC before lambda_b is chosen; the escaping part tends to 0 coordinatewise and
cannot be targeted before lambda_b. OK.
MISSING (R6): even with all errors compact and carried, the converted carriers available near and below the boundary must
supply the room of the destroyed carriers (~ 4 M lambda_b/t at scale t) and carry the O(1) switching component below the band
with block coefficient <= Q (part 3.2). This is a rho-independent but nonzero conversion requirement; Model N shows it is NOT
met by one carrier of one type in general (R = 1.09 to 2.07 at nearby parameters, independent of tau_gen) and is met by
converting both types (R = 1.000 in the coupled test). A complete description of the residual adversarial requirements must
include "conversion capacity below the Hilbert/room requirement at every boundary".

## 4.4 Chain guards (5.2(b)). Arithmetic CORRECT in the linear status model, with one caveat. (refwork/chain.py, J = 32)
Bottom-up Delta_{i+1} = (T_i - Delta_i)/c, Delta_{i_b+1} = 0; top-down Delta_i = T_i - c Delta_{i+1}.
 c = 1.5: bottom-up max|move| 0.72 T (random one-type targets in [T/2, T]); c = 3: 0.33 T. Bounded uniformly in J. OK.
 c < 1, top-down: max|move| <= T/(1-c) (observed 1.0, 1.1, 1.66 for c = 0.3, 0.7, 0.9). OK. Bottom-up for c < 1 explodes
 (c^{-J}), as R3 says.
 c = 1 (CAVEAT): bottom-up is a random walk when the targets vary (Delta_{i+2} = Delta_i + T_{i+1} - T_i): max|move| = 3.6 T
 over random targets; bounded only for constant (or adaptively equalised) targets, which the approximant may choose since
 conversion targets form an interval. R3's "for c >= 1 bounded by T" should say "with constant targets".
 Alternating types, c = 1: moves grow like J T (observed 32 T). OK as stated. (For c > 1 alternating is bounded: 2T at c = 1.5.)
R3_part5.md 5.2(b) contains a garbled earlier version ("O(J max|T|)", "c^{-J}" bottom-up for c < 1 without the top-down fix);
the notes version is the correct one.

## 4.5 Coarsest guard (5.2(a)). HEURISTIC (not SKETCH): the existence of c_max(p) is fine (finitely many carriers above any
depth carry critical masses at a given p; each fixed carrier's far masses tend to 0), and "p is a private handle of c_max(p)
when the boundary lies just above c_max(p)" is fine in the status model. But: (i) the approximant needs J handles at ADJACENT
scales for ONE boundary, and the coarsest-guard observation produces handles at the boundaries it chooses, one per position;
the step from this to "blocking needs shared positions" is a heuristic dichotomy, not exhaustive (masses ~ lambda^alpha,
mixtures of chain and detector couplings, positions shared by both types with opposite signs); (ii) a shared position with
masses proportional to depth that extends to coarse scales cannot be used at all (moving it converts coarse carriers at cost
~ lambda_top, not o(1)); R3's "converts all members below the top member" needs the top member's depth -> 0, which holds for
escaping positions (fixed carriers have vanishing far masses) — fine, but should be said. (iii) Nothing is proved for the
real norm (R3 5.2(c) says so). Label HEURISTIC/SKETCH-in-toy-model is acceptable.

## 4.6 Statements in R3 section 0 / 5.4 that need correction.
 * "E's Model N agrees: R -> 1 even with a single converted carrier of one type": parameter-specific (B S^2 = 0.5 < sup P_f =
   0.5225); false at A = 0.5 (R = 1.46) or B = 0.6 (R = 1.086), maximum at the bottom scale, independent of tau_gen.
 * "the bounded-conversion-capacity obstruction ... disappears for compact error directions": only its error-driven part;
   a rho-independent Hilbert/room requirement remains (part 3.2).
 * "The conversion-capacity bound of E 8.3 (about three parameters at a group transition) is irrelevant" / "Far rigidity does
   not matter": irrelevant to EC itself, but relevant to the Hilbert/room requirement (both types must usually be converted,
   which E 4.4 says a group transition provides).
 * "at any prescribed depth" (task summary of Thm EC): only "at least as fine as" a prescribed depth.
