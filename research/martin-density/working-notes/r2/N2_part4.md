# N2 part 4: approximate resonances, conversion capacity, and the rigid design versus Lemma B

## 4.1 Exact versus approximate resonances (what parts 2-3 do and do not use)
An exact resonance (part 1) is a SCALE-FREE transfer v = L*(Delta omega - Delta d w) supported on F cup K and z-signed on K. Engineering
(Theorems 1-3) uses: masses on finitely many window contacts (two-sided base usage at small scales), the contacts beyond the window
with their own signs (one-sided usage at intermediate scales), far negative masses (free pulls), and a scalar tuning. NO block coordinate
of f has to change status, and NO conversion of one-sided block carriers is needed: the carrier set Q_{m_0} is finite and robust.
An approximate resonance is a family of scale-dependent transfers: at scale t the two sides use DIFFERENT one-sided carriers of depth
Phi ~ t (weak peaks, near-threshold strict non-peaks used beyond their gap, near-contacts, near-flip base coordinates), which represent
the same component of g up to O(t) (A §7.2, P1 3.4-3.6). Known intrinsic results: near-threshold strict non-peak carriers with
sum of gaps = infinity give mates in cl Cert(f) (P1 4.4); single-family carriers with gaps bounded below are certificates + O(t)
(A Cor 6.10(c)). Open intrinsically: summable gaps, weak-peak carriers, near-contact carriers with rooms -> 0 in a summable way.

## 4.2 Proposition (cross-block near-duplicates). PROVED.
(a) (P1 4.2, sign rule) If u_{n,m} and u_{n,m'} differ by o(Phi) in the xi-direction, they serve the same side; they cannot switch.
(b) Exact duplicates u_{n,m} = u_{n,m'} ((n,m) != (n,m')) do not exist (T injective; A Fact F, E Lemma 6.3).
(c) If the difference of two (possibly cross-block) carriers is, up to the d-terms, a contact vector, i.e.
    c(u_{n,m}/... ) relation  v := c u_{n,m} - c' u_{n',m'} - Delta d_m R_m* w_m + Delta d_{m'} R_{m'}* w_{m'} supported on F cup K and z-signed,
    with (n,m), (n',m') strict non-peaks, then the two-piece mates built on this transfer (P1 2.3 construction) are EXACT two-piece mates
    with two active blocks; they are recovered by Theorem 1 + Remark 2.6 when Delta d_m = Delta d_{m'} = 0 and ell_m|_J != 0 (rank condition:
    ell_m|_J = -ell_{m'}|_J since v vanishes on J), and fall under part 3 otherwise (multi-block versions of Thms 2-3: SKETCH).
(d) Martin's built-in near-duplicates (same w'_n in every block) are approximate in general: their differences are the unknown
    perturbations of [16, Prop 2.8], not contact vectors; they create switching only if the perturbations are >~ Phi in the xi-direction
    with opposite signs at every scale (P1 4.2), i.e. an approximate resonance treated below.
*Proof.* (a),(b) quoted. (c): the representation is exact two-piece by construction (Def 1.1), with I_act = {m, m'}; the rank condition is
as stated. QED.

## 4.3 Theorem 4 (recovery through converted or implanted carriers at the approximant; conditional). PROVED.
Let f in S_{p*}, g in C(f), rho in (0,1), T_0 in (0, sqrt((1-rho^2)/2)]. Let f' in NA cap S_{p*}, gbar, h_1, ..., h_J in X*, Q, kappa >= 0 and
scales s_j := s_1 2^{j-1} (s_J <= T_0) satisfy
 (HC) p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j      (two-sided structure at f' down to scale s_j: CONVERTED or implanted carriers),
 (HT) p*(f' + t gbar) <= 1 + Q t^2/2 for s_1 <= |t| <= T_0   (the structure of f transferred to f' above the boundary scale s_1),
 (HE) p*(h_j - gbar) <= kappa s_j                          (frozen error of the order of its own scale),
with Q <= 1 - 3(1-rho^2)/8 and J >= 16 kappa/(1-rho^2). Put g' := (1/J) sum_j h_j (so p*(g' - gbar) <= 2 kappa s_J/J). Then
p*(f' + t g') <= s(t) for |t| <= T_0. If moreover eps := p*(f' - f) <= (1-rho^2) T_0^2/6 and eta := p*(g' - rho g) <= (1-rho^2) T_0/6, then
g' is in C(f') and (f', g') is in NA. Consequently: if for every rho < 1 there is T_0 > 0 such that data as above exist with eps, eta -> 0,
then g is in Ls(f), i.e. (f, rho g) is in cl NA for all rho < 1.
*Proof (the skeleton of E notes 2.1, re-derived).* By convexity, p*(f' + t g') <= (1/J) sum_j p*(f' + t h_j). For j with s_j >= |t| use (HC);
for s_j < |t| (so |t| >= s_1) use p*(f' + t h_j) <= p*(f' + t gbar) + |t| kappa s_j and (HT). Since sum_{s_j < |t|} s_j <= 2|t|, for |t| <= T_0:
p*(f' + t g') <= 1 + Q t^2/2 + 2 kappa t^2/J <= 1 + t^2 [1/2 - 3(1-rho^2)/16 + (1-rho^2)/8] = 1 + t^2 [1/2 - (1-rho^2)/16] <= s(t)
(s(t) >= 1 + t^2/2 - t^4/8 and t^2 <= (1-rho^2)/2). For |t| >= T_0: p*(f' + t g') <= p*(f + t rho g) + eps + |t| eta <= s(rho t) +
(1-rho^2) min(t^2,|t|)/3 <= s(t) (A Lemma 4.7, as in Theorem 1 Step 7). N_part1 Lemma 1.2(a) gives (f', g') in NA; the last
statement follows from N_part1 Thm 1. QED.
Comment. The theorem isolates exactly what engineering must provide for an approximate resonance: (HT) (transport of the one-sided
structure above a boundary scale; the carriers used at scales >= s_1 must keep their statuses at f' and the destroyed finer carriers must
contribute only O(t) at scale t >= s_1 — the bookkeeping of E 2.1 (H-transfer), HEURISTIC in general) and (HC)+(HE) at J(rho) ~ 16 kappa/(1-rho^2)
ADJACENT DYADIC SCALES just below the boundary. Note that J(rho) is finite for each rho: one does not need infinitely many conversions
for a given rho, but J(rho) -> infinity as rho -> 1 (E's Model M/N: R(J) -> 1 only as J -> infinity).

## 4.4 Conversion capacity (definition, sources, limits)
Definition. At f, for a family of one-sided carriers (k_i) of a switching mate, the CONVERSION CAPACITY is
  CC(f) := sup{ J : for every eps > 0 there is an NA f' with p*(f' - f) <= eps at which J carriers of adjacent dyadic depths just below the
            boundary scale of f' are strict non-peaks with gaps bounded below (two-sided) and the coarser carriers keep their status }.
Sources (all with the refereed estimates):
 (S1) window moves and Delta a act on the carriers u_k = (v + K lambda_k sigma_k + far_k)/n_k only through ONE absolute scalar V = v(x' - xhat)
      up to o(lambda_k) (E Prop 8.2, PROVED); one scalar converts one carrier TYPE in one band of scale ratio (2+delta)/delta (E 2.4, re-derived
      by E_referee 2.7);
 (S2) far tails: carrier k can be shifted by any s with |s| < tau_k (free tail mass relative to the guards, E Lemma 6.1/Cor 6.2, PROVED,
      room factor 2-4 by E_referee 2.10) without disturbing the guards; conversion needs |s| ~ theta Phi_k; so each carrier with
      tau_k >~ Phi_k is individually convertible;
 (S3) detector-group scalars (E Lemma 6.4): one per group of carriers whose far parts are proportional to one detector psi_n.
So CC(f) = infinity whenever infinitely many carriers near every scale have free tail mass >~ Phi_k relative to the coarser guards
("quantitative tail independence at scale"). The adversarial alternative is FAR RIGIDITY: tau_k << Phi_k for all carriers, with far parts
collinear inside long groups (E (A2), far half). Then CC(f) <= (number of independent group scalars at a transition) + 1 <= 3 (E 8.3).

## 4.5 Proposition (far rigidity is compatible with Lemma B). SKETCH (adaptation of the PROVED construction P1 2.1).
For every prescribed family of "carrier" vectors y_i in c_00 (with prescribed scales) and every sequence eps_i -> 0 there is an admissible T
(Lemma B's conclusion: norm one, injective, Ran T cap c_00 = {0}, each block's normalized vectors dense in S_{q*}) whose block vectors include
u_i = (y_i + delta_i (psi_{n(i)} + eps_i h_i))/norm, where the detectors psi_n have pairwise disjoint supports G_n, the signatures h_i have pairwise
disjoint supports S_i disjoint from all G_n and from all supp y, and delta_i, eps_i are as small as we wish. In particular the free tail mass of
u_i relative to the other members of its group is <= delta_i eps_i ||h_i|| << Phi_i: far rigidity (E (A2), far half) holds.
*Sketch.* Copy P1 2.1: targets y^{(l)} dense in S_{q*} with "allowedness" (a target index is used at position l only if its support avoids all
signature sets S_{l'} at which it could compete with the signature coefficient c_{l'} delta_{l'} eps_{l'}); signature tails delta_l eps_l h_l on S_l;
detector parts delta_l psi_{n(l)} supported on G_{n(l)}, disjoint from all S. Injectivity and Ran T cap c_00 = {0}: for Z = sum x_l c_l u_l in c_00 and
s in S_{l'} far out, Z(s) = x_{l'} c_{l'} delta_{l'} eps_{l'} 2^{-s}/n_{l'} + (target contributions, bounded by allowedness), exactly P1's estimate
with delta_{l'} replaced by delta_{l'} eps_{l'}; detectors do not meet S_{l'}. Density: delta_l -> 0 along each block. Norm one: c_1 = 1 as in P1.
The only change is bookkeeping of the constants. (Not written out in full: SKETCH.)
Consequence. Lemma B does NOT force unbounded conversion capacity through source (S2). The E_referee objection "the NC design constraint
contradicts density" concerns a different constraint ("every coordinate with j-mass carries errors >= eps_0 (j-mass)"), which indeed
contradicts density (density requires approximants of e_j*/q*(e_j*) with arbitrarily small error); its RATE version (good approximants of the
core directions occur only at scales lambda_k <= psi(error), psi decaying as fast as one likes) is compatible with Lemma B by the same
construction (the target sequence may be visited arbitrarily late in each block).

## 4.6 What is NOT settled by 4.5 (why the rigid design is not an obstruction)
 (i) A switching mate through one-sided carriers needs a non-NA f whose block statuses are tuned (near-threshold peaks of both signs at all
     scales, E (A1)) — a fixed-point problem between T and f; P1 2.1/2.2 show such fixed points can be engineered for finitely many
     prescribed statuses with robust margins; near-threshold statuses at ALL scales are not constructed anywhere (OPEN, plausible).
 (ii) Even with CC(f) bounded, Theorem 4 can use OTHER two-sided carriers for (HC): implanted fine coordinates (A Lemma 8.2: a fine k with
     u_k close to a target plus a far handle can be set off-peak with w'(k) = 0 at f'), converted generic coordinates of FINE detector groups
     whose scalars are free (E 7.5 (C1)), coarse one-sided carriers of the core directions (C2), combinations (C3). Their usefulness depends on
     approximation RATES of the dense generic family: a carrier at depth lambda used at its own scale must have error O(lambda) ("implant scale
     gap", C Round 1). Lemma B allows arbitrarily slow rates, but slow rates for a FIXED target only push good approximants to fixed (eventually
     coarse) scales, where they are matched rather than convertible (E 7.5). Whether an adversary can block (C1)-(C3) simultaneously with (A1)-(A5)
     is OPEN; no consistent complete design is known (E 7.5, E_referee 4).
 (iii) Model N's positive excess R(J) - 1 (1.2%-19% for J <= 4) is NUMERICAL in a cost model that optimizes only over frozen + transfer
     representations; it is not a lower bound for p* over all decompositions at all approximants.

## 4.7 Answer to task item 2 (precise limit of engineering)
 * For EXACT resonances the decisive quantities are not conversion capacities: Delta d = 0 needs nothing beyond Lemma B (Theorem 1);
   Delta d > 0 needs the scalar Bregman condition (BR) (automatic under two-sided mass tuning, Thm 2); Delta d < 0 needs the pinning condition
   (PC) on the NEAR FREE coordinates (Thm 3), which in the generic case (infinitely many strict non-peaks in the carrier block) is a quantitative
   tail-independence statement at the scale of the window masses (3.7c). Conversely (3.4) the convexity mechanism provably cannot replace (PC).
 * For APPROXIMATE resonances the decisive quantity is the conversion capacity at the destruction boundary, or more generally the supply of
   two-sided carriers with frozen errors O(scale) at J(rho) ~ 16 kappa/(1-rho^2) adjacent scales below the boundary (Theorem 4). Sufficiency:
   PROVED conditionally (Thm 4) given the transport hypothesis (HT) (itself HEURISTIC in general). Necessity: OPEN — and I see no way to prove it,
   because (HC) can be met by carriers that are not conversions of the original ones (4.6(ii)); a necessary-and-sufficient property of T is
   therefore NOT identified. What IS established: (a) unbounded conversion capacity through far tails is not implied by Lemma B (4.5); (b) the
   only rigorous link between T and recovery for one-sided block carriers is through free tail masses (Cor 6.2) and the absolute scalar V (Prop 8.2).
 * Can an admissible T violate the sufficient conditions at some f? For approximate resonances: far rigidity (violating (S2)) is consistent with
   Lemma B (4.5, SKETCH); whether this can be combined with a non-NA f carrying a switching mate and with blocking of (C1)-(C3) is OPEN. For exact
   resonances with Delta d < 0: a P1-type T with Delta d < 0 exists (3.8, SKETCH), and there (PC) holds up to a far-tail comparison (3.7(a),(b)):
   no violation known.
