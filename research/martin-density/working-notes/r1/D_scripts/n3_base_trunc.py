# N3: test of Lemma 11.5(a) inequality (11.5.1):
#   q*(a + s P_N b) <= q*(a + s b) - s * r(xi) + C2 s^2 eps_N,  r = (I-P_N) b, eps_N = |U* r|
# for q*(a) = ||a||_1 + ||G a||_2 (G = U*), a of full support, b supported in supp a, b(xi)=0,
# xi = sign(a) + G^T (G a/|G a|).  We record the worst value of
#   [q*(a+sP_N b) - q*(a+sb) + s r(xi)] / (s^2 * eps_N)   (should stay bounded),
# and test it also in regimes with sign flips (|s b_j| > |a_j|).
import numpy as np
rng = np.random.default_rng(7)
def qstar(G, a): return np.abs(a).sum() + np.linalg.norm(G @ a)
worst = 0.0; worst_plain = -np.inf
for trial in range(300):
    n = 40; h = 5
    G = rng.normal(size=(h, n)) / np.sqrt(n)
    a = rng.normal(size=n) * np.exp(-0.15*np.arange(n))     # decaying "tail"
    a /= qstar(G, a)
    z = np.sign(a); h0 = G @ a / np.linalg.norm(G @ a)
    xi = z + G.T @ h0
    b = rng.normal(size=n)
    b -= (b @ xi) / (a @ xi) * a                              # b(xi) = 0 (a(xi)=1)
    for N in [5, 10, 20, 30]:
        r = b.copy(); r[:N] = 0.0
        PNb = b - r
        eps = np.linalg.norm(G @ r)
        for s in np.concatenate([np.linspace(-0.5, 0.5, 41), [1e-3, -1e-3, 2.0, -2.0]]):
            if s == 0 or eps < 1e-14: continue
            lhs = qstar(G, a + s*PNb) - qstar(G, a + s*b) + s*(r @ xi)
            worst_plain = max(worst_plain, lhs)
            ratio = lhs / (s*s*eps)
            worst = max(worst, ratio)
print("max over trials of [q*(a+sP_Nb) - q*(a+sb) + s r(xi)] =", worst_plain)
print("max ratio to s^2 eps_N =", worst, "  (bounded => consistent with (11.5.1))")
