import numpy as np, warnings
warnings.filterwarnings('ignore')
import importlib.util
spec = importlib.util.spec_from_file_location("chk", "ch_lemma_check.py"); chk = importlib.util.module_from_spec(spec); spec.loader.exec_module(chk)
rng = np.random.default_rng(7)
unit = chk.unit
u = 1e-4
out = []
for trial in range(4000):
    mu = 10 ** rng.uniform(-10, -8); sgn = rng.choice([-1, 1])
    a1, a2, a3, a4 = (0.5 * unit(rng.normal(size=4)) for _ in range(4))
    Q, _ = np.linalg.qr(np.stack([a1, a2]).T)
    q = rng.normal(size=4); q = unit(q - Q @ (Q.T @ q))
    c1 = 0.3 * a1 - 0.4 * a2 + sgn * mu * q
    A = np.stack([a1, a2, a3, c1, a4]); E, Is, Ic = [0, 1], [2], [3, 4]
    md, se = chk.check_MD_SE(A, mu, u, E + Is)
    if not (md and se): continue
    K = np.linalg.svd(A[E])[2][2:].T
    y = K @ rng.normal(size=2)
    if not (a3 @ y > 0.05 * np.linalg.norm(y) and a4 @ y > 0.05 * np.linalg.norm(y)): continue
    x0 = unit(y); V0 = 10 ** rng.uniform(-15, -13)
    x = x0 + V0 * unit(rng.normal(size=4))
    xp, V = chk.construct(A, E, Is, Ic, x, u)
    dC = chk.dist_exact_cone(A, E, Is + Ic, x)
    s = sgn * (q @ x0)
    out.append((s, mu, V, dC, np.linalg.norm(xp - x), (A[3] @ xp)))
    if len(out) >= 60: break
out = np.array(out)
right = out[:, 0] > 0
print("n =", len(out), " right-signed:", right.sum(), " wrong-signed:", (~right).sum())
print("right-signed: max dist to exact cone = %.3g, max |x'-x| = %.3g" % (out[right, 3].max(), out[right, 4].max()))
print("wrong-signed: min dist to exact cone = %.3g (data |x|=1), max |x'-x| = %.3g, min c1.x' = %.3g, max mu = %.3g"
      % (out[~right, 3].min(), out[~right, 4].max(), out[~right, 5].min(), out[~right, 1].max()))
