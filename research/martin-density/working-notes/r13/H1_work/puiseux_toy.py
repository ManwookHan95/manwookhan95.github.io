"""Sanity check of Proposition J1.11 (first-order Puiseux margin) on toys with SINGULAR zero sets Z.
mu(h) = 1 - max_{r in Y_1} G_h(r), G_h(r) = inf{F(r'') : r'' in Z, |r''-r| < h}.
Computed via D(m) := max_{r in Y_1} dist(r, Z ∩ {F <= 1-m}); mu(h) = sup{m : D(m) < h}.
psi_d(r) = m |r_d| K(sigma, m^2 R^2) with Lemma K's closed form (one block, block index m=1).
"""
import numpy as np
from scipy.spatial import cKDTree

def K(sig, x):
    return (sig + np.sqrt(sig**2 * x + sig * (1 - x))) / (1 - x)

def psi(r, d, sig=0.4):
    R2 = np.sum(r**2, axis=1)
    return np.abs(r[:, d]) * K(sig, R2)

def mu_curve(P, Fv, ms):
    """P: sample points of Z (n x dim); Fv: F at samples; ms: margins. Returns D(m) for each m."""
    Y1 = Fv <= 1.0
    out = []
    for m in ms:
        good = Fv <= 1.0 - m
        if not np.any(good):
            out.append(np.inf); continue
        tree = cKDTree(P[good])
        q = Y1 & ~good
        if not np.any(q):
            out.append(0.0); continue
        dist, _ = tree.query(P[q])
        out.append(dist.max())
    return np.array(out)

def report(name, P, Fv, ms):
    D = mu_curve(P, Fv, ms)
    print(f"--- {name}: {len(P)} samples, min F on Z = {Fv.min():.6f}")
    # mu(h) >= m iff D(m) < h.  Print pairs (m, D(m)) and the ratio m/D(m) (a lower bound for mu(h)/h at h = D(m)+).
    for m, dm in zip(ms, D):
        print(f"   m = {m:.2e}   D(m) = {dm:.3e}   m/D(m) = {m/dm if dm>0 else np.inf:.4f}")
    # fitted exponent: log m vs log D
    ok = np.isfinite(D) & (D > 0)
    if ok.sum() >= 3:
        sl = np.polyfit(np.log(D[ok]), np.log(np.array(ms)[ok]), 1)[0]
        print(f"   fitted exponent beta (mu ~ h^beta): {sl:.3f}")

rng = np.random.default_rng(1)

# ---------- Toy A: cone with vertex c in R^3, N_T = {0, 1}, Lambda passing near the vertex ----------
c = np.array([0.20, 0.15, 0.05])
ns, nt = 500, 2000
s = np.linspace(0, 0.12, ns)
th = np.linspace(0, 2*np.pi, nt, endpoint=False)
S, TH = np.meshgrid(s, th, indexing='ij')
pts = []
for sgn in (+1, -1):
    pts.append(np.stack([c[0] + S*np.cos(TH), c[1] + S*np.sin(TH), c[2] + sgn*S], axis=-1).reshape(-1, 3))
PA = np.concatenate(pts)
pc = np.array([psi(c[None], 0)[0], psi(c[None], 1)[0]])
ms = np.geomspace(2e-4, 2e-2, 9)
for label, Phi in [("generic weights (vertex F = 1 - 3e-3)", pc / (1 - 3e-3) * np.array([1.0, 1.0 + 2.1e-3])),
                   ("coincidence weights (vertex on Lambda, both active)", pc.copy())]:
    Fv = np.maximum(psi(PA, 0) / Phi[0], psi(PA, 1) / Phi[1])
    report("Toy A cone, " + label, PA, Fv, ms)

# ---------- Toy B: rotated cusp in R^2 with tangent orthogonal to grad psi_0 at the tip ----------
c = np.array([0.20, 0.15])
eps_h = 1e-6
g = np.array([(psi((c + [eps_h, 0])[None], 0) - psi((c - [eps_h, 0])[None], 0))[0],
              (psi((c + [0, eps_h])[None], 0) - psi((c - [0, eps_h])[None], 0))[0]]) / (2 * eps_h)
t = np.array([-g[1], g[0]]); t /= np.linalg.norm(t)   # tangent of the cusp at the tip, orthogonal to grad psi_0
n = g / np.linalg.norm(g)
sv = np.concatenate([np.linspace(0, 0.35, 400000)])
PB = np.concatenate([c + np.outer(sv**2, t) + np.outer(sgn * sv**3, n) for sgn in (+1, -1)])
psi_tip = psi(c[None], 0)[0]
for label, Phi0 in [("coincidence (tip on Lambda, critical)", psi_tip),
                    ("generic (Phi * (1 + 1e-3))", psi_tip * (1 + 1e-3)),
                    ("generic (Phi * (1 - 1e-3))", psi_tip * (1 - 1e-3))]:
    Fv = psi(PB, 0) / Phi0
    report("Toy B cusp, " + label, PB, Fv, np.geomspace(1e-5, 1e-2, 7))
