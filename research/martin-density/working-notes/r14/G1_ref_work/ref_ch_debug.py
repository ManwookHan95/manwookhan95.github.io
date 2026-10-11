import numpy as np, itertools
import ref_ch_check as R
R.rng = np.random.default_rng(7)
u = 1e-3; cnt = 0; tries = 0
while cnt < 600 and tries < 200000:
    tries += 1
    n = int(R.rng.integers(3, 6))
    A, E, Is, Ic = R.instance(n, u)
    p = A.shape[0]
    if p > 7: continue
    mins_all = R.all_minors(A, list(range(p)))
    tiny = [d for d in mins_all if d < u]
    mu = max(tiny) if tiny else 0.0
    if mu > 1e-6: continue
    strictm = R.all_minors(A, E + Is)
    if any(1e-12 < d < u for d in strictm): continue
    mu = max(mu, 1e-300)
    K = np.linalg.svd(A[E])[2][len(E):].T
    y = K @ R.rng.normal(size=K.shape[1])
    x = R.unit(y) + 10 ** R.rng.uniform(-9, -3) * R.unit(R.rng.normal(size=n))
    xp, V, rho, Nk, kB = R.construct(A, E, Is, Ic, x, u)
    if V == 0: continue
    cnt += 1
    eta = 2 ** (n / 2) * mu / u
    val = np.min(A[Ic] @ xp + eta * np.linalg.norm(xp))
    if val < -1e-9:
        np.set_printoptions(precision=4, linewidth=150)
        print("FAIL n=%d p=%d E=%s Is=%s Ic=%s mu=%.3g eta=%.3g val=%.3g V=%.3g kB=%d Nk=%s" % (n, p, E, Is, Ic, mu, eta, val, V, kB, Nk))
        print("A=\n", A); print("x=", x); print("xp=", xp); print("A@x=", A @ x); print("A@xp=", A @ xp)
        print("norms", np.linalg.norm(A, axis=1))
        print("any nan:", np.isnan(A).any())
