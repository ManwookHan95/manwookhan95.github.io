# V1-ref part 1 — reading log and first-pass issue list (referee's working file)

Read: V1_head, V1_part0..5 (V1_notes.md = head + part1..5, byte-identical by size), Y1..Y4 referee reports, BRIEFING(_R2).

First-pass candidate issues (to be checked against the note and Round-5/6 sources):
 (i1) l_f must also satisfy s_max(l_f) >= max F (so that s_m, pulls j_{l''}, banks j'_{l''} avoid F, and "z^2 = eps on S_{l''} \ [1,s_max]"
      holds); s_max(l) -> infinity because the allowed targets are dense in S_{q*} ∩ c_00 and each is used. Trivial precision.
 (i2) Part 2 Remark (2): in a one-signed block every component has rate <= b theta_m/m, not <= b; tiny only after l >= l_f
      (b theta/m < u since u/b is huge). Trivial precision.
 (i3) Lemma S: needs exact form of eq:peakshift (sign, e_k >= 0, e_k <= t/(sigma |alpha|)) and lem:switchbudget (phi-sum <= t/q_0).
 (i4) Lemma DR / ST: Lemma T2(b) hypotheses (outward push s, other perturbations E <= A s/(8(A+theta+1))).
 (i5) Prop TR Step 4: lem:split with z^(2); exact statement of lem:split needed (what is chi; the e_+- bounds).
 (i6) Prop TR Step 5: kind [3] inward condition, shift trick, A_2 = 22.
 (i7) Theorem E'': Lemma U with pulled support — no-flip at pulls needs |r| <= c_flat t; Cor D1 at f_j with tiny pull masses.
 (i8) Lemma TU: exponents of Design in c_T, C_T; fixed point; positivity of bank masses.
 (i9) Lemma ST: the threshold may DROP by C_f T_lo^4 in blocks outside I_D(w): check every kept carrier there has rho robustly < 1.
 (i10) Survival claim (d) of Theorem 1' is a meta-claim; check the new exponent omega+20 and rate objects (R5)-(R7) do not break
      any window proof (they only enlarge Q).
