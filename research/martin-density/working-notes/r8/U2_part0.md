# U2 part 0: orientation notes (working file, not final)

Reduction target: (LSC-trunc) [Y3 6(a)]: given Lemma Z at every F-finite row, (LSC-trunc) <=> Lemma Z at every row.
Y3 Thm 6.1 + Thm 2.1: (LSC-trunc) holds for (f,g) as soon as windowed EXACT two-piece data with cushion-compatible
side parts ((iv): (sb^+)_- , (sb^-)_+ <= C|a|/t + beta, beta cushion-sparse) exist (at f, or at a companion with
transfer error o(T_lo^2), V3 Thm 2.5). Truncation itself is free.

Where infinite F hurts: the exact (projected) switching X = sum_B eps_l tau'_l u_l is anti-signed on F beyond the
cushion on the deep set D_t = {j in F: s_j X_j < -4|a_j|/t}. Deep anti-signed mass is O(Kt) in l_1 always, but
fixed data with it flip at first order at all smaller scales (fatal unless cushion-sparse).
V3 remedy: raise deep coordinates (Hilbert footprint mu_j * level); fails for mu-thin a ((RR) fails).

NEW IDEA (E1, thin-support dichotomy): the anti-amplitude of the ACTUAL switching through a support-swallowed
carrier l' is pinned by every coordinate j of S_l' cap F which is "effectively a contact" at scale t
(|a_j| <= theta0 K t^2 v_j): sigma*DeltaTheta <= 2 theta0 K t + O(Kt)/v_j. So:
 - shallow coordinates j <= J: by PIGEONHOLE over sub-window positions inside the long design window, each shallow
   coordinate is either thick at all sub-window scales (never deep) or effectively-contact at the bottom scale
   (then it pins the anti-switching with constant ~2^J/delta: add its sign row to the cone; Hoffman ~ H_0 2^J);
   each shallow coordinate excludes only a band of O(n + log K) dyadic positions;
 - deep coordinates j > J: raise them (cost <= mu_J * K'' t^2) -- cheap if mu decays doubly-exponentially faster
   than the signature weights: mu_J <= 2^{-C K 2^J} holds for J ~ log log K when mu_s = 2^{-2^{2^s}}.
So (RR) can be removed by a DESIGN choice of the diagonal base + pigeonhole (no condition on the profile of a).
To check: pinning inequality with finer targets / other bad carriers; Hoffman constants with added sign rows;
circularity J <-> n <-> K; window length budget n^w >= J(n + log K) + n.

E5 idea: VP via PRIVATE far coordinates (diagonal base): one coordinate per carrier in S_l (in F: raise/lower a_s;
off F: pulls/banks as in V1) -> VP constant is a design constant per carrier (diagonal), no f-dependent
conditioning of a growing system. Issue: two-sided tuning on F needs |a_s| not tiny for lowering; else raise one
coordinate and lower via normalization or use a second coordinate.
