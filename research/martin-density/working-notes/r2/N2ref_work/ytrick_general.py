# General Lemma R: S := {k : |2w'(k) - w(k)| <= M' + (M'-M)_+ + eps}; y = w' + (w'-w)1_S.
# Claim: N(y) <= 1 + (C'-C)_+ + eps + (||D(w'-w)||^2 + ||D Y||^2 + 2|R1|)/(2(C + 2(C'-C))).
import numpy as np
exec(open("ytrick_exact.py").read().split("N = lambda")[0])     # wM, J
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(13); worst = -1; cnt = 0; lost_in_S = 0
for trial in range(300):
    K = 16; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.2, 1.0, K)
    Q0 = rng.choice(np.arange(1, 10), size=rng.integers(1, 4), replace=False); zeta[Q0] *= 1e-3
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    t = 10**rng.uniform(-3.5, -1.5)
    zeta2 = zeta + t*Phi*rng.normal(size=K)*rng.uniform(0, 30)
    flip = rng.choice(np.arange(9, K), size=rng.integers(0, 4), replace=False); zeta2[flip] *= rng.uniform(-1.5, 0.5, len(flip))
    w2 = J(zeta2, Phi); M2 = np.abs(w2).max(); C2 = np.linalg.norm(Phi*w2)
    eps = rng.choice([0.0, 1e-3])
    S = np.abs(2*w2 - w) <= M2 + max(M2 - M, 0) + eps
    pk, pk2 = np.abs(np.abs(w)-M) < 1e-10, np.abs(np.abs(w2)-M2) < 1e-10
    lost_in_S += int((S & pk & ~pk2).sum())
    Y = (w2 - w)*S; y = w2 + Y; gam = C2 - C
    Delta = Phi*(w2 - w); R1 = (Phi*w2) @ (Phi*(w2-w)*(~S))
    bound = 1 + max(gam, 0) + eps + (Delta@Delta + (Phi*Y)@(Phi*Y) + 2*abs(R1))/(2*(C+2*gam))
    worst = max(worst, N(y, Phi) - bound); cnt += 1
print('cases', cnt, 'max violation', worst, '; lost peaks placed in S:', lost_in_S)
# (appended) the single violation above has C + 2 gamma < 0, outside the lemma's hypothesis; see ytrick_diag.py
