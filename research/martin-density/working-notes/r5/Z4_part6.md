# Z4 part 6: what remains, precisely; route (2) verdict; the averaging lemma with scale-dependent c_flat

## 6.1 A bookkeeping lemma used in part 4
**Lemma 6.1 (windowed averaging with window-dependent c_flat).** PROVED. Theorem thm:windowed and Lemma lem:avgfunctionals remain true if
c_flat is allowed to depend on j (c_flat = c_{flat,j} in (0,1]), provided n_j >= 24 rho^2 K_j/(c_{flat,j}(1 - rho^2)) for every j.
*Proof.* In the proof of Theorem thm:windowed, j is fixed from the second sentence on; c_flat enters only through I_r := {i : c_flat t_i <
rho|r|}, the bound sum_{I_r} t_i < 2 rho|r|/c_flat and Q := 2 rho^2 K/(c_flat n) <= (1-rho^2)/12, all for that j. QED.
(Part 4, Step 8 uses this with c_{flat,j} = c_flat(l_j).)

## 6.2 The residual obstruction after Theorem 3.1 (F finite)
Theorem 3.1 (with Corollaries 4.1, 4.2, 5.4) reduces every remaining case of (O2) and (O3) with F finite to at least one of the following
**first-order inexact resources** on swallowed signature sets (for SLD_G; for the original SLD add the growth of H^Z_f):
 (E-a) swallowing-sign swallowed peaks that are degenerate ((H3) fails) or whose margins decay faster than the ladder (M_f large);
 (E-b) swallowed strict non-peaks with gaps decaying faster than the ladder (gamma_f small): near-threshold carriers;
 (E-c) free target coordinates (|z_j| < 1) with rooms decaying faster than the ladder (gamma_T small): near-contacts met by swallowed targets;
 (E-d) one-sided d-resources: (DR) fails (zero-cost cone has d-sums of one sign only in some block), so exact d-neutral data would have to
       drop genuine switching (Proposition 5.1 forbids Delta d != 0 at maximal contact);
 (E-e) good signature sets whose rooms r*_l(l_*) decay too fast or vanish once coarse swallowed targets are removed (Lambda* large) —
       this is approximate swallowing, (O1)(i).
In every case the window data at scale t are two-piece data up to a FIRST-ORDER defect of size O(t) (block excess |alpha(k)| |tau omega(k)|
at weak peaks, overshoot beyond the gap, room-weighted base mass, d-defect times wrong-signed R*w mass). HEURISTIC (but each step is a
one-line estimate): such defects cannot be averaged away, because the one-sided expansion (i) of Lemma lem:avgfunctionals must hold for
|r| <= c_flat t down to r -> 0, where a defect delta |r| with delta ~ K t is not <= eta r^2; and Theorem thm:engineered tolerates first-order
defects only of size o(s_1)|tau|, s_1 -> 0, whereas averaged data have a fixed defect ~ K t_top/n. So the common core of (O1), and of what is
left of (O2)/(O3), is:

**Problem 6.2 (exact data for inexact resources).** For the designed operator and F finite: given swallowed signature sets on which the
switching uses weak peaks, near-threshold strict non-peaks, near-contacts or one-sided d-resources, find, on long windows of scales, functionals
g_t with ||g - g_t|| <= K t and EXACT two-piece data, or an engineering theorem accepting data whose first-order defect is O(t) at window
scale t (a multi-scale version of Theorem thm:engineered, in which the engineering scale s_1 and the data scale are coupled).

## 6.3 Route (2) verdict (lower semicontinuity along far lowerings)
(a) PROVED (Prop. 1.2): p*(f^L - f) <= C_f eps_L <= C_f c_{L+1}/2.
(b) PROVED (Prop. 1.3): on all scales that f^L inherits from f through the rho-slack, the carriers made roomy are negligible (total switching
O(t)), and the coarse ones are swallowed exactly as at f. Therefore dist(rho g, C(f^L)) -> 0 requires on the band [A t_L, T] the same
exact matching of the finitely many coarse swallowed carriers that Theorem 3.1 performs at f itself; when the hypotheses of Theorem 3.1 hold,
f in R directly and no lowering is needed.
(c) HEURISTIC: when they fail because of (E-a)-(E-d) (f-dependent growth), far lowering cannot help: the band length (about
(1/2) log2(1/c_{L+1}) dyadic scales) is a DESIGN quantity, while the constants of the coarse matching at level L (1/margins, 1/gaps,
Hoffman constants of the d-rows) are f-quantities, and f is chosen after T. (A proof would need to construct, for any given design, a first row
whose level-L constants exceed any given function of L; not attempted.) Lowering by a factor, or on far points of coarse sets, is worse:
the created room pins only at scales t^2 <~ lambda_l room_l, which the slack of that lowering does not reach (Z1's transition band; part 1).
(d) The second open question of (O2), "are all finitely swallowed first rows in R?", is answered for those satisfying (H2'), (H3) and
(B_fin) by Corollary 4.2(b) — no (DR), no (H2), no resonance needed — and stays open only when (H3) or (H2') fails (a degenerate swallowing-sign
peak; or a block all of whose non-degenerate peaks are swallowed and which lacks a swallowing-sign non-degenerate swallowed peak or an
anti-sign swallowed peak). For finitely many swallowed carriers, margins, gaps, rooms of the finitely many target points and the Hoffman
constants of the finitely many cones are fixed positive (finite) numbers, so (E-a) with mu > 0, (E-b), (E-c), (E-d) are harmless there.

## 6.4 Proposal: the modified design SLD_G (summary for the note)
SLD_G = Definition def:SLD with (i) n^w_l and T_hi(l) inflated by the configuration Hoffman constant G*(l) (part 2.4), and (ii) the extra
clause c_l <= (delta_l ||h_l||_1)^2 (Lemma 5.3). All proved results of Section 8 survive verbatim (Proposition 2.4: only (T-a)-(T-d),
(P1)-(P3) and allowedness are used). New: Theorem 3.1 (S_Binf) and its corollaries hold for SLD_G with the f-dependent growth hypothesis
(W_inf) only; for the original SLD they hold under (W_inf^orig), which includes the f-dependent Hoffman constants H^Z_f.

## 6.5 Cross-reference (parallel Round-5 work, not refereed here)
Z3 (case (O1)) reports a "moved first row" version of the engineering (exact data at a nearby f_j with p*(f_j - f) = o(T_lo^2)) and a BAND
limit (carriers with room between T_lo^2 and 1/K can be neither pinned nor exactified). Part 8.2 above is the same limit for weak peaks
(margin in place of room); the obstruction (E-a)-(E-e) of 6.2 is thus the band phenomenon of (O1) appearing inside (O2)/(O3). Naming: the
theorem of part 3 is called S_Binf (infinitely many swallowed carriers, F finite); it is unrelated to the "Theorem S-inf" of Z5 (infinite F).
