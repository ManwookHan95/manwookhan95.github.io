# E referee — part 7: a partial repair of T1 (referee SKETCH) and the T4 sign analysis

## 7.1 Block absorption of the d-mismatch when Delta d := d- - d+ >= 0 (referee SKETCH)
Setting: two-piece mate with one-sided linear decompositions Om+- = omega+- - d+- w (omega+- finitely supported,
off-peak), admissible on [0,tau_0] resp. [-tau_0,0]. At f'' use
   Om''+- := omega+- - d+-'' w'' + c+- (w'' - w),   with c+ <= 0 <= c-  (so t c+- <= 0 on the side where it is used).
(1) Mismatch: the side decompositions at f'' represent the same g'' with base parts EXACTLY equal to the transported
    b+- (window part) iff (c- - c+) = Delta d and d+''-d-'' = d+-d- (one scalar condition per block, enforced by a
    small window move as in A-referee 5.4). Feasible with the sign constraints iff Delta d >= 0. The side made
    two-sided by eta-masses (regime |t| <= eta) must have c = 0 (it is used for both signs of t); then the other c
    equals +-Delta d with the right sign iff Delta d >= 0.
(2) No first-order block cost: with h = omega - d'' w'' + c(w'' - w), tc <= 0, sup-norm derivative over peaks and
    near-peaks of w'' is -d'' M'' + c(M'' - M) (min of M'' - sigma'' w(k) is M'' - M at unchanged peaks, never smaller);
    D-part derivative d'' M'' + c(C'' - <Dw,Dw''>/C''). Sum: t c (C C'' - <Dw,Dw''>)/C'' <= 0 (Cauchy-Schwarz), i.e. a
    first-order GAIN of size |t c| O(||D(w''-w)||^2) — no condition C'' = C needed.
(3) Exact sup-norm bound: |W(k)| <= (1 - t d'' - |tc|)|w''(k)| + |tc||w(k)| <= (1 - t d'')M'' + |tc|(M - M'')_+ off supp omega,
    which is exactly the first-order term above: no hidden second-order excess. Hilbert part: c^2 ||D(w''-w)||^2 small.
Conclusion: T1 (eta-masses + far truncation, A-referee 5.4 / E 1.4(i)) extends from Delta d = 0 to Delta d >= 0.
For Delta d < 0 one would need t c > 0 (extrapolation away from w), and every new or flipped peak k of w'' (typical:
fine coordinates are scrambled by the eta-perturbation) produces first-order excess t c (M'' - sigma''_k w(k)) up to
2|t c| M. Replacing w by a coarse/fine hybrid leaves base mismatch |Delta d| sum_{scrambled} lambda_k |w''-w| ~ |Delta d| eta.
So Delta d < 0 two-piece mates remain OPEN; their existence is as plausible as for Delta d > 0 (same fixed-point
sign condition as A-referee 5.2 with omega of the opposite sign). The fix would need matching all coordinates with
Phi(k) >= eps eta after the eta-perturbation (quantitative tail independence).

## 7.2 T4: who pays for the head shift (CORRECTED: both sides pay)
Carrier-k decomposition with its own clean block part w'' + t(omega_k - d''_k w'') has base direction
B = B_a + L*(omega_{N*} - omega_k) + eps_k L*w'', eps_k = d''_k - d''_{N*}. B(xhat'') = 0 (the carrier difference
compensates eps_k (1-q_0'')/q_0''), so the cost is the KINK cost |t||eps_k| kappa_q''(+-L*w'') > 0 (z'' in c_0), on BOTH
sides. Moving eps into the block (delta = d''_{N*}) gives block first-order t eps_k and base first-order
-t eps_k (1-q_0'')/q_0'': again a cost on both sides. (A first draft claimed one side is free: that was wrong — the
rescaling f'' = a'' + L*w'' only redistributes the excess.) Head contacts shift n u_{N*}(x'') by +sum |Z_l| gamma_l,
so |eps_k| = rho c sum|Z_l| gamma_l/|zeta''| <= rho c c_gamma lambda_{N*} eps_0/|zeta''| for every matched carrier. A common window shift V
does not change eps_k (it shifts all v0-carriers equally). Freezing a P-type coordinate instead moves the cost to
t > 0. Hence single-N* T4 needs c_gamma eps_0 <= (1-rho^2) M |zeta|/(12 rho^2 c^2 n), while the mate condition only
gives c_gamma eps_0 <~ M/(4 c^2 n): for rho near 1 an adversary can violate it. Averaging J frozen representations
with heads at J dyadic scales (T2 / Thm 5.1 mechanism, using carriers other than the heads in each (b)-regime)
divides this boundary cost by J: plausible repair.
