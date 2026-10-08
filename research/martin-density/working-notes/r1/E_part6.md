# E notes, part 6: structural lemmas about destruction and conversion at NA approximants

Setting: f with normer xi, xhat = xi/q_0 = z + U e. An NA approximant is f' = grad p(x'), x' = z' + U e'
(F1). In this part a' = a (possible when a in c_00; otherwise add the truncation error, which only changes e' by a
norm-small amount) and z' = z on a window [1, W]. For a block coordinate k write
   Delta_k(z') := u_{k,m}(x') - u_{k,m}(xhat) = u_{k,m}((z' - z) 1_{(W,inf)}).
Status of k at f' vs f is governed by Delta_k relative to Phi_m(k) (block threshold, Preprint B).

## Lemma 6.1 (duality; PROVED)

Let E be a finite-dimensional subspace of l_1(W, inf) and y in l_1(W, inf). Then
   sup { y(eta) : eta in c_00(W, inf), ||eta||_inf <= 1, h(eta) = 0 for all h in E } = dist_{l_1}(y, E).
Proof. "<=": for h in E, y(eta) = (y - h)(eta) <= ||y - h||_1. ">=": the annihilator E_perp := {eta in c_0(W,inf) :
h(eta) = 0, h in E} is a closed subspace of c_0 and (E_perp)* = l_1/(E_perp)^perp = l_1/E (E is finite-dimensional, hence
weak*-closed, so (E_perp)^perp = E). Hence sup over the unit ball of E_perp of y(eta) is the quotient norm
dist(y, E). The unit ball of E_perp cap c_00 is norm dense in that of E_perp (truncate and correct on finitely many
coordinates using a finite set where E is "injective"; standard), so the sup over c_00 is the same. QED

## Corollary 6.2 (destroyed implies convertible; PROVED)

Let G be a finite set of block coordinates ("guards") and k notin G. Put
   tau_k := dist_{l_1}( u_{k,m}|_{(W,inf)},  span{ u_g|_{(W,inf)} : g in G } )    (the FREE TAIL MASS of k).
(a) If z' (beyond W) keeps the guards exactly matched, Delta_g(z') = 0 for g in G, then |Delta_k(z')| <= 2 tau_k.
(b) Conversely, for every s with |s| < tau_k there is eta in c_00(W,inf) with ||eta||_inf <= 1, Delta_g unchanged for
    all g in G, and Delta_k shifted by exactly s (replace z' by z' + eta / 2 when ||z'||_inf <= 1/2 far out).
So the amount by which k can be DESTROYED while the guards are kept is at most twice the amount by which the approximant
can SHIFT k (for instance back to off-peak) without touching the guards.
Proof. (a) (z' - z)1_{(W,inf)} annihilates E := span{u_g|_{(W,inf)}} and has sup norm <= 2; apply Lemma 6.1 to y = u_k|_{(W,inf)}
(by homogeneity). (b) Lemma 6.1 gives eta with value arbitrarily close to tau_k, then scale. QED
Remarks. (1) Matching the guards exactly is a finite set of linear conditions on z' beyond W; by tail independence
(A_notes Fact F(b): finitely many restrictions u_{k_i,m_i}|_{[N,inf)} are linearly independent, PROVED from Y cap c_00 = {0})
it is solvable; quantitatively the size of the correction depends on condition numbers. (2) tau_k > 0 always (same fact).

## Lemma 6.3 (no exact collinearity of tails; PROVED)

If k != k' are coordinates of the same or different blocks and there are W_0 and c in R with
u_{k,m}|_{(W_0,inf)} = c u_{k',m'}|_{(W_0,inf)}, then contradiction. Proof: u_{k,m} - c u_{k',m'} is in Y (Y linear)
and finitely supported, hence 0 (Y cap c_00 = {0}); so T(e_{k,m}/q*(T e_{k,m}) - c e_{k',m'}/q*(T e_{k',m'})) = 0,
contradicting injectivity of T. QED
Consequence: an adversary can only make tails APPROXIMATELY collinear; the deviations give individual conversion
capacity equal to their free tail mass (Cor 6.2(b)), which the adversary must keep below the conversion threshold.

## Lemma 6.4 (a single far detector can always be neutralized; PROVED for the first statement)

Let psi in l_1, W in N, psi_{>W} := psi 1_{(W,inf)}, and z in B_{l_inf}. Then
   { psi_{>W}(z') : z' in B_{c_0} } = ( -||psi_{>W}||_1 , ||psi_{>W}||_1 )   (plus an endpoint if psi_{>W} in c_00).
Hence if |psi_{>W}(z)| < ||psi_{>W}||_1 (true whenever |z| < 1 on a set carrying a positive part of |psi_{>W}|, e.g. on
near-contacts), there is z' in B_{c_0} with z' = z on [1,W] and psi((z' - z) 1_{(W,inf)}) = 0.
Proof: for z' finitely supported with |z'| <= 1, psi_{>W}(z') ranges over [-S_N, S_N], S_N = sum_{W<l<=N} |psi_l| (take
z'_l = c sign(psi_l)); S_N increases to ||psi_{>W}||_1; c_0 vectors give the open interval by approximation. QED
Consequence (HEURISTIC as a description of all adversarial designs): resources whose far parts are all proportional to
ONE detector psi can be matched simultaneously by a single scalar condition, so an adversary who wants destruction at
all fine scales at EVERY approximant needs infinitely many independent detectors ("groups"); the approximant can then
place the matched/destroyed boundary at a transition between two groups (two independent scalars), which is exactly
the configuration where Model N gives R ~ 1 when peak costs matter (part 4.4), but R(2) = 1.043 in the error-dominated
regime (part 7.4).
