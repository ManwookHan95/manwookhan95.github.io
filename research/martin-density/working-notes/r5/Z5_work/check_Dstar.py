# Lemma 4.6(c): largest switching amplitude compatible with the cushion inequalities for a fast-swallowed carrier
import numpy as np
q0 = 0.5
J = np.arange(1, 400)
def Phi(D, t, beta):
    v = 2.0 ** (-J); aj = 2.0 ** (-(1 + beta) * J)
    return np.maximum(D * v - 2 * aj / t, 0).sum()
def Dstar(t, beta):
    lo, hi = 0.0, 1e12
    for _ in range(200):
        mid = np.sqrt(lo * hi) if lo > 0 else hi / 2 ** 20
        if Phi(mid, t, beta) <= t / (2 * q0): lo = mid
        else: hi = mid
        if hi / max(lo, 1e-300) < 1 + 1e-12: break
    return lo
for beta in [0.5, 1.0, 2.0, 3.0]:
    ts = np.logspace(-12, -3, 10)
    Ds = np.array([Dstar(t, beta) for t in ts])
    slope = np.polyfit(np.log(ts), np.log(Ds), 1)[0]
    print(f"beta={beta}: fitted exponent of D*(t) = {slope:.3f}, predicted (beta-1)/(beta+1) = {(beta-1)/(beta+1):.3f};  D*/t at t=1e-12: {Ds[0]/ts[0]:.3e}")
