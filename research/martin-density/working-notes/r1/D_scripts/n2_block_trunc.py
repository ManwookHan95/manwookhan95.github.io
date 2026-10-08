# N2: block norm |z| on R^n with unit ball B_{l1} + D(B_{l2}); dual N(w)=||w||_inf+||Dw||_2.
# Check that phi(z) = |z| - |P_K z| is NOT convex (so within-block coordinate truncation
# does not give p = q_eta + s_eta with s_eta a seminorm).
import numpy as np
rng = np.random.default_rng(0)
Phi = np.array([0.5, 0.25, 0.125])
def N(w): return np.max(np.abs(w)) + np.linalg.norm(Phi * w)
def norm_primal(z, iters=20000):
    # |z| = max_{w != 0} <w,z>/N(w); random search + local refinement on the sphere
    n = len(z); best = 0.0; bw = None
    W = rng.normal(size=(4000, n))
    vals = (W @ z) / np.array([N(w) for w in W])
    i = np.argmax(vals); best = vals[i]; bw = W[i]
    step = 0.5
    for _ in range(iters):
        c = bw + step * rng.normal(size=n)
        v = (c @ z) / N(c)
        if v > best: best, bw = v, c
        else: step *= 0.999
        if step < 1e-13: break
    return best
def phi(z, K=1):
    zz = z.copy(); zz[K:] = 0.0
    return norm_primal(z) - norm_primal(zz)
y = np.array([0.0, 1.0, 0.0])
for R in [1.0, 3.0, 10.0, 30.0]:
    zp = np.array([R, 1.0, 0.0]); zm = np.array([-R, 1.0, 0.0])
    lhs = phi(y); rhs = 0.5 * (phi(zp) + phi(zm))
    print("R=%5.1f  phi(y)=%.6f   avg phi(+-R e1 + y)=%.6f   convexity violated: %s" % (R, lhs, rhs, lhs > rhs + 1e-6))
# sanity: |e_k| = 1/(1+Phi_k)?  (B contains e_k + D-part)
for k in range(3):
    e = np.zeros(3); e[k] = 1
    print("|e_%d| = %.6f   (lower bound 1/(1+Phi)= %.6f)" % (k+1, norm_primal(e), 1/(1+Phi[k])))
