# cert1 (Round 11): independent toy for Lemma NLM / Lemma QC with the ACTUAL structure of X1:
#   effective columns c_l(r_l) = u_l - r_l tau on E_c (Lemma EC) => 2x2 minor det[c_1(r_1), c_2(r_2)] is AFFINE in (r_1, r_2);
#   psi_d(r) = m |r_d| K(sigma_rob, R_a^2), F_Phi = max_d psi_d / Phi_d on Z = {minor = 0} cap K_kappa (W-fix region).
# (A) coincidence weights (min_Z F = 1 at a local min) give mu(h) = 0; generic weights give mu(h) > 0, mu ~ c h^beta.
# (B) a cusp-shaped Z (zero set of y^2 - x^3 type minor) to see a Puiseux exponent beta > 1 for generic weights at a boundary point.
# (C) sampling: P(|min_Z F - 1| < eps) ~ eps (coincidence set has codimension 1 in Phi-space).
import numpy as np
rng = np.random.default_rng(11)

def K(s, x):
    return (s + np.sqrt(s * s * x + s * (1 - x))) / (1 - x)

m = 1
srob = 0.02
xmax = 1 - srob / 4          # W-fix region R_a^2 <= 1 - sigma_rob/4
u1 = np.array([0.3, -0.2]); u2 = np.array([0.1, 0.3]); tau = np.array([0.5, 0.3])
# minor(r1, r2) = det[u1 - r1 tau, u2 - r2 tau] = det(u1,u2) - r1 det(tau,u2) - r2 det(u1,tau)
d12 = u1[0]*u2[1]-u1[1]*u2[0]; dtu2 = tau[0]*u2[1]-tau[1]*u2[0]; du1t = u1[0]*tau[1]-u1[1]*tau[0]
# Z: d12 - r1*dtu2 - r2*du1t = 0  -> line; parametrize by arclength t
p0 = np.array([d12 / dtu2, 0.0]); dirv = np.array([-du1t, dtu2]); dirv /= np.linalg.norm(dirv)
# shift p0 to the point of the line closest to origin
p0 = p0 - np.dot(p0, dirv) * dirv
T = np.linspace(-1.2, 1.2, 240001)
pts = p0[None, :] + T[:, None] * dirv[None, :]
R2 = m * m * (pts ** 2).sum(1)
inside = R2 <= xmax
T = T[inside]; pts = pts[inside]; R2 = R2[inside]
dt = T[1] - T[0]
psi = m * np.abs(pts) * K(srob, R2)[:, None]       # psi_1, psi_2 along Z

def Fvals(Phi):
    return np.max(psi / Phi[None, :], axis=1)

def mu_of_h(F, h):
    w = max(1, int(round(h / dt)))
    # G_h(t) = min over |t''-t| <= h of F(t'') (sliding window min)
    from numpy.lib.stride_tricks import sliding_window_view
    Fp = np.concatenate([np.full(w, np.inf), F, np.full(w, np.inf)])
    G = sliding_window_view(Fp, 2 * w + 1).min(axis=1)
    Y1 = F <= 1
    if not Y1.any():
        return None
    return 1 - G[Y1].max()

out = []
# (A) generic weights
Phi = np.array([0.30, 0.25])
F = Fvals(Phi)
out.append('Z: line (Lemma EC: 2x2 minor affine in r); |Z cap K| = %.3f; min F = %.6f' % (T[-1]-T[0], F.min()))
# scale weights so that min F < 1 but Y_1 is a proper subset
Phi = Phi * (F.min() * 1.05)
F = Fvals(Phi)
hs = [1e-2, 3e-3, 1e-3, 3e-4]
mus = [mu_of_h(F, h) for h in hs]
out.append('(A) generic weights Phi=%s: min F=%.6f; mu(h) for h=%s: %s' % (np.round(Phi, 6), F.min(), hs, ['%.3e' % x for x in mus]))
bet = np.polyfit(np.log(hs), np.log(mus), 1)[0]
out.append('    fitted exponent beta ~ %.3f (expected 1: boundary points of Y_1 are regular)' % bet)
# coincidence: scale Phi so that min F = 1 exactly
Phic = Phi * F.min()
Fc = Fvals(Phic)
imin = Fc.argmin()
out.append('(A) coincidence Phi=%s: min F = %.12f at t=%.4f, psi1/Phi1=%.6f psi2/Phi2=%.6f' % (np.round(Phic, 8), Fc.min(), T[imin], psi[imin,0]/Phic[0], psi[imin,1]/Phic[1]))
musc = [mu_of_h(Fc, h) for h in hs]
out.append('    mu(h) at coincidence: %s  (should be ~0)' % ['%.2e' % x for x in musc])
for eps in [1e-3, 1e-2]:
    Fe = Fvals(Phic * (1 + eps))
    out.append('    weights x(1+%g): mu(h=1e-3) = %.3e' % (eps, mu_of_h(Fe, 1e-3)))
# critical-point property at coincidence: slopes of the two branches along Z have opposite signs
g1 = np.gradient(psi[:, 0] / Phic[0], dt)[imin]; g2 = np.gradient(psi[:, 1] / Phic[1], dt)[imin]
out.append('    tangential slopes at the minimizer: %.4f, %.4f (opposite signs => critical for Psi_D, D={1,2})' % (g1, g2))

# (C) sampling the codimension: fraction of random Phi with |min F - 1| < eps
N = 20000
ph = rng.uniform(0.06, 0.10, size=(N, 2))
mins = np.array([np.max(psi / p[None, :], axis=1).min() for p in ph[:6000]])
for eps in [1e-1, 1e-2, 1e-3]:
    out.append('(C) P(|min_Z F - 1| < %g) = %.4f' % (eps, np.mean(np.abs(mins - 1) < eps)))

# (B) cusp-shaped Z: Z = {(x0 + s^2, y0 + s^3)} (zero set of (y-y0)^2 - (x-x0)^3), one carrier d with psi = |r_1| K(srob, R^2)
s = np.linspace(-0.5, 0.5, 400001)
x0, y0 = 0.30, 0.20
P = np.stack([x0 + s ** 2, y0 + s ** 3], 1)
R2c = (P ** 2).sum(1)
psic = np.abs(P[:, 0]) * K(srob, R2c)  # status of carrier 1 depends on r_1 and R^2
# choose Phi so that F = psic/Phi equals 1 at the cusp tip s = 0 => cusp tip is a local MIN of F (s^2 increases r_1) -> coincidence
Phi_tip = psic[200000]
arc = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(P, axis=0), axis=1))])
def mu_curve(Fv, h):
    # G_h via euclidean ball in r-space restricted to Z (use arclength upper bound: points within euclidean h)
    Y1 = np.where(Fv <= 1)[0]
    if len(Y1) == 0: return None
    best = -np.inf
    for i in Y1[:: max(1, len(Y1)//400)]:
        dist = np.linalg.norm(P - P[i], axis=1)
        best = max(best, Fv[dist < h].min())
    return 1 - best
for fac in [1.0, 1.001, 1.01]:
    Fv = psic / (Phi_tip * fac)
    r = [mu_curve(Fv, h) for h in [1e-2, 3e-3, 1e-3]]
    out.append('(B) cusp, weight x%.3f: min F=%.6f, mu(h=1e-2,3e-3,1e-3) = %s' % (fac, Fv.min(), ['%.3e' % x for x in r]))
open('nlm_qc_toy.out', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
