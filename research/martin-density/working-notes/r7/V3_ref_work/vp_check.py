"""Referee check of V3 Lemma VP (value-preserving raises) for a diagonal base.

Value of a carrier u at zhat = z + U e, e = U*a/||U*a||:  u(zhat) = u(z) + <U*u, e> = u(z) + sum_s mu_s^2 u_s a_s / ||U*a||.
A raise D (supported on F, here: a deep raise Da plus a correction x on F0) changes only the second term.
Checks: (1) the derivative at x = 0 equals Lambda(xi)/nu with Lambda(x)_k = sum mu_s^2 x_s (u_k(s) - a_s gamma_k/nu^2);
(2) Newton solve for x on F0 with ||x||_1 <= C ||U* Da||; (3) a carrier vanishing on F has Lambda-row = 0 and its value is
automatically preserved (so (ND_{L_0}) as stated fails trivially there; the corrected condition (ND') ignores such rows).
"""
import numpy as np
rng = np.random.default_rng(3)
n = 40
mu = 2.0 ** (-(np.arange(n) / 4.0) ** 2 - 1)        # fast decay (scaled so that n = 40 is meaningful in double precision)
F = np.arange(30)                                     # support
a = np.zeros(n); a[F] = rng.choice([-1, 1], len(F)) * 0.7 ** F; a /= (np.abs(a).sum() + np.linalg.norm(mu * a))
L0 = [rng.standard_normal(n) for _ in range(3)]
L0.append(np.concatenate([np.zeros(30), rng.standard_normal(10)]))   # carrier vanishing on F
def val_shift(u, A):
    return (mu ** 2 * u * A).sum() / np.linalg.norm(mu * A) - (mu ** 2 * u * a).sum() / np.linalg.norm(mu * a)
nu = np.linalg.norm(mu * a)
gam = [(mu ** 2 * u * a).sum() for u in L0]
Lam = np.array([[mu[s] ** 2 * (u[s] - a[s] * g / nu ** 2) for s in F] for u, g in zip(L0, gam)])
print("Lambda row norms:", np.abs(Lam).sum(1))
# (1) derivative check
xi = np.zeros(n); xi[:5] = rng.standard_normal(5) * 1e-7
num = np.array([val_shift(u, a + xi) for u in L0]) / 1e-0
print("derivative check (num vs Lambda/nu):", num[:3], (Lam[:3, :5] @ xi[:5]) / nu)
# (2) Newton solve on F0 = {0..4} for the first three carriers (the fourth is automatically preserved)
F0 = np.arange(5)
for y in [1e-1, 1e-2, 1e-3]:
    Da = np.zeros(n); deep = np.arange(8, 16); Da[deep] = np.sign(a[deep]) * y * 0.5 ** (deep - 8)
    x = np.zeros(n)
    for it in range(30):
        A = a + Da + x
        G = np.array([val_shift(u, A) for u in L0[:3]])
        if np.abs(G).max() < 1e-17:
            break
        J = np.zeros((3, len(F0)))
        for c, s in enumerate(F0):
            d = np.zeros(n); d[s] = 1e-9
            J[:, c] = (np.array([val_shift(u, A + d) for u in L0[:3]]) - G) / 1e-9
        step = np.linalg.lstsq(J, -G, rcond=None)[0]
        x[F0] += step
    UD = np.linalg.norm(mu * Da)
    print(f"y={y:g}: ||U*Da||={UD:.3e}  ||x||_1={np.abs(x).sum():.3e}  ratio={np.abs(x).sum()/UD:.3f}  "
          f"max|x/a| on F0={np.max(np.abs(x[F0]/a[F0])):.2e}  residual={np.abs(G).max():.1e}  "
          f"4th carrier shift={val_shift(L0[3], a + Da + x):.1e}  sign kept={np.all(np.sign(a+Da+x)[F]==np.sign(a[F]))}")
