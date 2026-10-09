
# 6. The other P2 instance's results (P2_part2.md, P2_part3.md): summary and what I re-checked

**6.1 Theorem (d-neutral two-piece mates; P2_part2 2.1). PROVED there.** f with F finite, g in C(f) with d-neutral two-piece data (Delta d_m = 0 for all m),
rho^2 kappa < 1; if |I_0| >= 2 a steering span hypothesis (S) on free coordinates. Then (f, rho g) in cl NA. No condition on the contact split, on K,
on rates of T or on the number of non-peaks; no tuning cone condition.
Key step re-checked (steering without (TC)): P_{e-perp}U*v != 0 (v in Y \ {0} is not a multiple of a, U* injective), and since v lives on F u K with
z_j v_j = |v_j| on K, sum_{j in F} v_j <P_{e-perp}U*v, U*e_j*> + sum_{j in K} |v_j| <P_{e-perp}U*v, z_j U*e_j*> = ||P_{e-perp}U*v||^2 > 0, so there is a "raising"
coordinate j_+ (in F with either sign, or a contact with its own sign) whose mass increases v(xhat'); far flipped contacts with negative masses
("pulls", reservoir sum_{K > N}|v_j| > 0 because v is not in c_00) decrease it by 2 sum_Far |v_j|; the intermediate value theorem gives v(xhat') = 0
exactly. Order: N, s_1 (small w.r.t. the reservoir), Far, N'' (decompositions transfer exactly on (N, N''] \ Far, and are linear on Far thanks to the
negative masses), then the raising mass; beyond N the target uses the constant-split theta-tail. I checked the sign identity, the Far
compatibility (z'_j = -z_j = sign a'_j) and the tail estimate; I did not re-derive every constant.
Combined with Theorem 3.5 above: A_referee §5.4's general form (d-neutral, any split) is PROVED (one block: always; several blocks: under (S) or (TC));
Delta d_m >= 0: PROVED under (TC) (Thm 3.5); Delta d > 0 with pulls only: SKETCH (Bregman term needs a far-tail comparison, 4.2).
**6.2 (P2_part3 3.1-3.2).** The mixed term and the multi-piece consistency identity — agree with my 2.5-2.6 (their 3.2 identity
B'_t - B'_{t'} - rho(B_t - B_{t'}) = -rho sum_m[(Delta'_m - Delta_m)R_m*w'_m + Delta_m R_m*(w'_m - w_m)] is the multi-piece form of my Step 3 algebra).
**6.3 (P2_part3 3.4, SKETCH there).** Non-neutral two-piece data (any sign of Delta d) at block-tame active blocks with margin sparsity and a tuning
span: agrees with my 4.1(d) (pinning); both are SKETCH (uniform implicit-function / Lipschitz step for the global scalars not written in full).
For Delta d_m >= 0 my Theorem 3.5 removes all block-tameness and margin assumptions.

# 7. Answers to the specific questions of the task, and next steps

(a) **A_referee §5.4 (two-piece mates over infinite contact sets with non-constant split).** PROVED: Theorem 3.5 (several blocks, Delta d_m >= 0, (TC)) and
6.1 (d-neutral, other instance). The referee's "extra degree of freedom in the masses" is correct exactly when (TC) holds (P1's diagonal-U
objection is the failure of (TC)); otherwise pulls are needed (6.1). The referee's truncation of g is fine when N is chosen after s_1 (no pulls);
with pulls one needs the constant-split tail (P1's correction).
(b) **Switching mates.** Contacts on both sides: covered (Thm 3.5: side - contacts transfer exactly, side + contacts get masses). Off-peak carriers
pushed beyond their gap: covered when the carriers are fixed (Lemma 3.2(b): activation at fixed scales, zero-order errors -> 0); NOT covered when the
depth of the carrier grows as t -> 0 (Prop 5.4). Weak peaks: degenerate peaks (alpha = 0) SKETCH-covered by one tuning each (4.4(b)); non-degenerate weak
peaks are scale-dependent resources (usable only at scales t >~ alpha_k dev_k): residual (R3), except when intrinsic weighted averaging applies
(P1 4.3-4.4: non-summable gaps -> cl Cert(f)).
(c) **C's implant scale gap.** CONFIRMED in quantitative form (5.3: capacity t_cap costs >= 2|c| t_cap in f' - f, absent cancellations; the same
cost/capacity ratio for window masses and near-threshold conversions). It is not an obstruction to the three-regime scheme: the band
[t_cap, sqrt(t_cap)] is covered by exact transfer of robust structure (Thm 3.5). It IS an obstruction for scale-dependent carriers (5.4).
(d) **The mixed term delta t <P^perp U*e_j, P^perp U*B_t>/||U*a||.** Exact form 2.5. Not an obstruction: for one base part it is absorbed by the
a'-multiple; for finitely many pieces it is cancelled by finitely many scalar tunings (for two-piece data: the single condition Delta d'_m = Delta d_m,
whose residue is the Bregman excess, o(s_1)); for any bounded family of base parts it is cancelled up to eta by finitely many tunings (compactness of U*).
Cancellation needs tuning moves with positively spanning effects ((TC)) or pulls.
(e) **Exactly for which mates regime (i) can be supplied:** 5.5 — components carried at small scales by base contacts/near-contacts, fixed off-peak
carriers, (degenerate peaks); not for components carried at all small scales by scale-dependent block carriers.
**Next steps.** (1) Prove the pinning Lipschitz step (4.1(d)) to close Delta d < 0 at block-tame blocks. (2) "Finitely generated switching" (carriers in a
fixed finite set, base parts varying with t): write the per-piece convexity version (SKETCH in 5.5). (3) Decide (R3): either find an f with a
mate in (R3) and a uniform lower bound dist(rho g, C(f')) >= c for all NA f' near f (counterexample route — would need excluding cancellations in
f' - f, which none of the present arguments does), or a pinning scheme with ~log(1/s) conditions, i.e. a quantitative tail-independence property of T
(possibly arranged by choosing T, cf. P1 2.1). (4) Shifted two-piece data (P2_part2 2.4) to get f in R at P1's example.
