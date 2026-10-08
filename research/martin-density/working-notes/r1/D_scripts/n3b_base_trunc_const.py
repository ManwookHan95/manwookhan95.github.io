# N3b: per-instance check of the explicit constant in (11.5.1) on the range |s| <= |U*a|/(2|U*b|):
#   l1 part:  ||a+sP_Nb||_1 - ||a+sb||_1 + s*sum_{j>N} z_j r_j <= 0          (exact)
#   U  part:  ||U*(a+sP_Nb)|| - ||U*(a+sb)|| + s<h0,U*r>  <= C2 s^2 eps,   C2 = 2|U*b|/|U*a| + eps/|U*a|
import numpy as np
rng = np.random.default_rng(11)
viol_l1 = 0; viol_U = 0; tot = 0; maxratio = 0.0
for trial in range(2000):
    n = rng.integers(10, 60); h = rng.integers(1, 8)
    G = rng.normal(size=(h, n)) / np.sqrt(n)
    a = rng.normal(size=n) * np.exp(-rng.uniform(0.02, 0.4)*np.arange(n))
    a /= (np.abs(a).sum() + np.linalg.norm(G @ a))
    z = np.sign(a); h0 = G @ a / np.linalg.norm(G @ a); xi = z + G.T @ h0
    b = rng.normal(size=n) * rng.uniform(0.1, 5)
    b -= (b @ xi) / (a @ xi) * a
    N = rng.integers(1, n)
    r = b.copy(); r[:N] = 0.0; PNb = b - r
    eps = np.linalg.norm(G @ r); Ua = np.linalg.norm(G @ a); Ub = np.linalg.norm(G @ b)
    C2 = 2*Ub/Ua + eps/Ua
    smax = Ua / (2*Ub)
    for s in np.linspace(-smax, smax, 31):
        if abs(s) < 1e-12: continue
        tot += 1
        l1 = np.abs(a + s*PNb).sum() - np.abs(a + s*b).sum() + s*(z[N:] @ r[N:])
        Up = np.linalg.norm(G @ (a + s*PNb)) - np.linalg.norm(G @ (a + s*b)) + s*(h0 @ (G @ r))
        if l1 > 1e-12: viol_l1 += 1
        if Up > C2*s*s*eps + 1e-12: viol_U += 1
        if eps > 1e-12: maxratio = max(maxratio, Up/(s*s*eps*C2))
print("tests:", tot, " l1 violations:", viol_l1, " U-part violations:", viol_U, " max(Up/(C2 s^2 eps)) =", round(maxratio, 4))
