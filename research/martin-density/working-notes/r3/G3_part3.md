# G3 part 3: signature pinning of block coefficients (uses SLD and (SR))

Standing in this part: T is the SLD operator of 1.2; f in R_0 with constants gamma, vartheta (1.1); g in C(f); eta <= eta_* and t <= t_eta
(part 2); a two-sided decomposition (B_+-, Omega_+-) of g at scale t (2.1). Ladder indices l with m(l) > N play no role (their carriers are
absent from L); all sums over l below run over {l : m(l) <= N}. Put
  c^+-_l := lambda_l Omega_{+-, m(l)}(k(l))   (so L*Omega_+- = sum_l c^+-_l u_l, absolutely convergent in l_1),
  Delta c_l := c^+_l - c^-_l,   Delta B := B_+ - B_- = - sum_l Delta c_l u_l   (both pairs represent g).
For a window index l_* let Cset := {l <= l_*} (coarse) and Fset := {l > l_*} (fine). delta'_l := delta_l ||h_l 1_{S_l cap J_gamma}||_1 / n_l >=
vartheta^l delta°_l > 0 by (SR) and (P1).

## 3.1 Lemma (box bound). PROVED.  |c^+-_l| <= 3 lambda_l / t for every l.
*Proof.* 2.4(e): |t Omega_+-(k)| <= 3. QED.

## 3.2 Lemma (pinning inequality). PROVED.
For every l:  delta'_l |Delta c_l| <= E_l + sum_{l' > l} kappa_{l', l} |Delta c_{l'}|,  where E_l := ||Delta B 1_{S_l cap J_gamma}||_1 and
kappa_{l', l} := ||y_{l'} 1_{S_l}||_1 / n_{l'}. Moreover kappa_{l',l} <= 4/3 and sum_l kappa_{l',l} <= 4/3 for every l'.
*Proof.* Let s in S_l. By (P1): u_{l'}(s) = 0 for l' < l (their targets avoid S_l, their signatures live on S_{l'}); u_l(s) = delta_l 2^{-s}/n_l
(y_l avoids S_l); u_{l'}(s) = y_{l'}(s)/n_{l'} for l' > l. Hence for s in S_l,
  -Delta B(s) = Delta c_l delta_l 2^{-s}/n_l + sum_{l' > l} Delta c_{l'} y_{l'}(s)/n_{l'}.
Take the l_1-norm over s in S_l cap J_gamma and use the triangle inequality; the left side is <= E_l and the first term on the right has norm
|Delta c_l| delta'_l. kappa_{l',l} <= ||y_{l'}||_1/n_{l'} <= 4/3, and the S_l are disjoint. QED.

## 3.3 Lemma (solution of the triangular system). PROVED.
  sum_{l in Cset} |Delta c_l| <= Lambda_f(l_*) [ sum_{l in Cset} E_l + (4/3) sum_{l' in Fset} |Delta c_{l'}| ],
  Lambda_f(l_*) := prod_{l <= l_*} (1 + 2/delta'_l) <= vartheta^{-l_*^2} Lambda°(l_*).
*Proof.* For l in Cset put D_l := |Delta c_l|, X_l := E_l + sum_{l' in Fset} kappa_{l',l} D_{l'} and S_l := sum_{l' in Cset, l' >= l} D_{l'} (S := 0 past l_*).
By 3.2, D_l <= (X_l + (4/3) S_{l+1})/delta'_l, hence S_l <= X_l/delta'_l + (1 + 4/(3 delta'_l)) S_{l+1}. Unrolling from l_* downwards,
S_1 <= sum_{l in Cset} (X_l/delta'_l) prod_{l'' < l} (1 + 4/(3 delta'_{l''})) <= (sum_l X_l) prod_{l'' <= l_*} (1 + 2/delta'_{l''}),
and sum_{l in Cset} X_l <= sum E_l + (4/3) sum_{Fset} D_{l'} by 3.2. Finally 1 + 2/delta'_l <= 1 + 2 vartheta^{-l}/delta°_l <= vartheta^{-l}(1 + 2/delta°_l)
and sum_{l <= l_*} l <= l_*^2. QED.

## 3.4 Lemma (total coefficient defect in a window). PROVED.
If t in W(l_*) and t <= min(t_eta, 1), then
  sum_l |Delta c_l| <= K_1 Lambda_f(l_*) t,   K_1 := 1/(gamma q_0) + 14.
*Proof.* sum_l E_l <= sum_{j in J_gamma} (|B_+(j)| + |B_-(j)|) <= t/(gamma q_0) (2.3(b); the S_l are disjoint). By 3.1 and (P2),
sum_{Fset} |Delta c_{l'}| <= 6 sum_{l' > l_*} lambda_{l'}/t <= 6 c_{l_*+1}/t <= 6 T_lo(l_*)^3/t <= 6 t^2. With 3.3:
sum_l |Delta c_l| <= Lambda_f (t/(gamma q_0) + 8 t^2) + 6 t^2 <= Lambda_f t (1/(gamma q_0) + 14). QED.

## 3.5 Corollary (what pinning controls). PROVED. Same hypotheses as 3.4; K := K_1 Lambda_f(l_*).
 (a) ||Delta B||_1 = ||sum_l Delta c_l u_l||_1 <= sum_l |Delta c_l| <= K t   (||u_l||_1 <= q*(u_l) = 1).
 (b) Base mass off the support: ||B_+ 1_{F^c}||_1 + ||B_- 1_{F^c}||_1 <= K t + t/q_0   (2.3(b) and (a)).
     In particular the total mass that the two decompositions put on CONTACTS and NEAR-CONTACTS (one-sided base resources, possibly
     infinitely many) is O(K t): contact switching is pinned by the block signatures.
 (c) Uniform shifts: for every block m, |Delta d_m| := |d_{+,m} - d_{-,m}| <= (Phi^max_m/(m C_m)) sum_{l : m(l) = m} |Delta c_l| + 2t/(sigma_m M_m) <= K_d K t,
     K_d := max_m (1/(m C_m) + 2/(sigma_m M_m)) (Phi^max_m := max_k Phi_m(k) <= 1).
*Proof of (c).* Put Delta Omega := Omega_+ - Omega_- and Delta omega := omega_+ - omega_- = Delta Omega + Delta d w. By 2.4(d),
Delta d = d(Delta omega) + r with |r| <= 2t/sigma_m, and d(Delta omega) = <Dw, D Delta Omega>/C + Delta d C. Hence Delta d M = <Dw, D Delta Omega>/C + r.
Since lambda_k = m Phi_k, <Dw, D Delta Omega> = sum_k Phi_k^2 w(k) Delta Omega(k) = (1/m) sum_k Phi_k w(k) Delta c_k, of modulus <= (M Phi^max/m) sum_k |Delta c_k|.
Divide by M. QED.

## 3.6 Remark (why this is the heart of the matter).
3.2-3.5 hold for ANY two decompositions of g (two sides, or two scales). They say: on every f in R_0 the block content of a mate is
determined, carrier by carrier, by the mate itself up to the base mass that the decompositions put on the roomy part of the signature sets,
which costs first order and is therefore O(t). This is exactly what fails at P1's example (the signature set of the resonant carrier is a
contact set: the signature can be carried for free on one side, and the carrier coefficient is not pinned). The price of pinning is the
factor 1/delta' per level and the triangular amplification Lambda_f(l_*) (coarse-to-fine contamination of signature sets by finer
targets, which cannot be avoided because targets must approximate vectors supported on signature sets); the windows of the SLD design are
long enough to absorb it (part 5).
