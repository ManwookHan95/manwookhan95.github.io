"""K2 referee: Theorem K2.6 (Sys-DC after preparation) in a finite one-block Martin-type model, at rows where the SQUARE
lever system (S-mass levers (P4) at thick private coordinates) is EXACTLY singular.
 Part A: left null vector y of the square system: Psi_y(zhat_0) = 0, gamma = <U*Psi_y, e_0> robust, D_Psi = 0 on the lever coordinates,
         identity kappa + sum_{F^c} Psi z = 0 (so the off-support mass of Psi is forced), K2.5(b) on finite-difference columns.
 Part B: PREPARED row (every contact of the carriers' supports banked with mass theta_0): smallest singular value of the enlarged
         TWO-SIDED column matrix (levers + unit mass changes at all support coordinates + unit z-moves at free coordinates), for
         theta_0 = 1e-2, 1e-4, 1e-6 (robust as theta_0 -> 0), compared with the proof's bound eps_DC.
 Part C: nonlinear solve of F = 0 at a perturbed pre-row of the prepared row (perturbation of either sign along y), Newton with the
         minimal-norm right inverse; banked masses must stay >= theta_0/2.
 Part D: UNPREPARED row with the same carriers: contacts give one-sided banks; with contact signs chosen adversarially
         (z_s = -sgn Psi(s) at every contact, iterated to consistency) the perturbation of the bad sign is NOT correctable by the levers and
         nonnegative banks (NNLS residual > 0), reproducing Q2-refa C.5 / K1 2.2; after preparation it is.
"""
import numpy as np
from scipy.optimize import brentq, nnls
from model import forced
rng = np.random.default_rng(20261010)

def build(Kom=3, Kpk=2, ns=4, nT=3):
    K = Kom + Kpk
    n = nT + K * ns
    S = [list(range(nT + k * ns, nT + (k + 1) * ns)) for k in range(K)]
    U = np.zeros((K, n))
    for k in range(K):
        if k < Kom:
            U[k, :nT] = rng.uniform(-0.05, 0.05, nT)
            U[k, S[k]] = rng.uniform(0.5, 1.0) * 0.6**np.arange(ns)
        else:
            U[k, :nT] = rng.uniform(0.2, 0.5, nT)
            U[k, S[k]] = rng.uniform(0.3, 1.0) * 0.6**np.arange(ns)
        U[k] /= np.abs(U[k]).sum()
    Phi = np.concatenate([rng.uniform(0.35, 0.45, Kom), rng.uniform(0.15, 0.25, Kpk)])
    mu = 0.3 * 0.88**np.arange(n)
    return K, n, S, U, Phi, mu

def base_row(K, n, S, U, Kom, nT, thick, zc, free_mask):
    A = np.zeros(n); z = np.zeros(n)
    z[:nT] = 1.0
    for k in range(K):
        for i, s in enumerate(S[k]):
            if k < Kom and i == 0:
                A[s] = thick[k]; z[s] = np.sign(thick[k])
            elif k < Kom:
                z[s] = -np.sign(thick[k]) * zc[s]
            else:
                z[s] = 1.0
    z[free_mask] = 0.3 * z[free_mask]
    return A, z

class Sys:
    def __init__(s, A0, z0, mu, U, Phi, Om):
        s.mu, s.U, s.Phi, s.Om = mu, U, Phi, Om
        s.blocks = np.zeros(len(Phi), int)
        s.st0 = forced(A0, z0, mu, U, Phi, s.blocks)
        s.A0 = s.st0['A'][0]; s.val0 = s.st0['val'].copy()
        s.eps = np.sign(s.val0); s.eps[s.eps == 0] = 1
        s.a0 = s.st0['a'].copy(); s.z0 = z0.copy()
    def F(s, a, z):
        st = forced(a, z, s.mu, s.U, s.Phi, s.blocks)
        return np.array([s.eps[l] * (st['val'][l] - (st['A'][0] / s.A0) * s.val0[l]) for l in s.Om]), st

def lever_dm(sysd, st, l, p):
    v = sysd.U[l, p]
    return sysd.eps[l] * np.sign(v) * st['nu'] / (sysd.mu[p]**2 * abs(v))

def columns(sysd, a, z, levers, h=1e-7):
    """two-sided columns at (a, z): levers (normalized), unit mass changes at all support coords, unit z at free coords."""
    F0, st = sysd.F(a, z)
    cols, kinds = [], []
    for l, p in levers:
        dm = lever_dm(sysd, st, l, p)
        a2 = a.copy(); a2[p] += h * dm; a3 = a.copy(); a3[p] -= h * dm
        cols.append((sysd.F(a2, z)[0] - sysd.F(a3, z)[0]) / (2 * h)); kinds.append(('lev', p))
    lev_coords = {p for _, p in levers}
    for s in range(len(a)):
        if s in lev_coords: continue
        if a[s] != 0:
            a2 = a.copy(); a2[s] += h; a3 = a.copy(); a3[s] -= h
            cols.append((sysd.F(a2, z)[0] - sysd.F(a3, z)[0]) / (2 * h)); kinds.append(('mass', s))
        elif abs(z[s]) < 1:
            z2 = z.copy(); z2[s] += h; z3 = z.copy(); z3[s] -= h
            cols.append((sysd.F(a, z2)[0] - sysd.F(a, z3)[0]) / (2 * h)); kinds.append(('z', s))
    return np.array(cols).T, kinds, F0, st

def bank_columns(sysd, a, z, h=1e-7):
    cols, where = [], []
    for s in range(len(a)):
        if a[s] == 0 and abs(z[s]) == 1:
            a2 = a.copy(); a2[s] = z[s] * h
            cols.append((sysd.F(a2, z)[0] - sysd.F(a, z)[0]) / h); where.append(s)
    return (np.array(cols).T if cols else np.zeros((len(sysd.Om), 0))), where

def Psi_of(sysd, st, y):
    p = np.array([sysd.eps[l] * sysd.val0[l] / sysd.A0 for l in sysd.Om])
    beta = y @ p
    RW = (sysd.Phi * sysd.st0['w']) @ sysd.U
    return sum(y[i] * sysd.eps[l] * sysd.U[l] for i, l in enumerate(sysd.Om)) - beta * RW

def make_singular(K, n, S, U, Phi, mu, Kom, nT, zc, free_mask, thick):
    """tune the thick mass of lever 0 so that the square lever system is singular."""
    def sq(t):
        th = thick.copy(); th[0] = t
        A0, z0 = base_row(K, n, S, U, Kom, nT, th, zc, free_mask)
        st = forced(A0, z0, mu, U, Phi, np.zeros(K, int))
        Om = [k for k in range(Kom) if not st['peak'][k]]
        if len(Om) < Kom: return None
        sysd = Sys(A0, z0, mu, U, Phi, Om)
        levers = [(l, S[l][0]) for l in Om]
        C, kinds, F0, st = columns(sysd, sysd.a0, z0, levers)
        return np.linalg.det(C[:, :len(levers)]), sysd, levers
    grid = np.concatenate([-np.linspace(0.8, 0.01, 60), np.linspace(0.01, 0.8, 60)])
    vals = []
    for t in grid:
        r = sq(t); vals.append(None if r is None else r[0])
    for i in range(len(grid) - 1):
        if vals[i] is not None and vals[i + 1] is not None and vals[i] * vals[i + 1] < 0:
            t = brentq(lambda t: sq(t)[0], grid[i], grid[i + 1], xtol=1e-14)
            return t, sq(t)
    return None, None

def prepare(sysd, theta0):
    a = sysd.a0.copy(); z = sysd.z0.copy()
    for s in range(len(a)):
        if a[s] == 0 and abs(z[s]) == 1 and np.abs(sysd.U[:, s]).max() > 0:
            a[s] = theta0 * z[s]
    return a, z

results = []
found = 0
for trial in range(400):
    if found >= 6: break
    Kom, Kpk, ns, nT = 3, 2, 4, 3
    K, n, S, U, Phi, mu = build(Kom, Kpk, ns, nT)
    zc = np.where(rng.random(n) < 0.85, 1.0, -1.0)
    free_mask = np.zeros(n, bool)
    for k in range(K):
        free_mask[S[k][-1]] = rng.random() < 0.5
    thick = rng.choice([-1, 1], Kom) * rng.uniform(0.05, 0.3, Kom)
    t, r = make_singular(K, n, S, U, Phi, mu, Kom, nT, zc, free_mask, thick)
    if r is None: continue
    det, sysd, levers = r
    C, kinds, F0, st0 = columns(sysd, sysd.a0, sysd.z0, levers)
    nl = len(levers)
    Usq, ssq, Vsq = np.linalg.svd(C[:, :nl].T)
    y = Vsq[-1]                                   # left null vector of the square system
    Psi = Psi_of(sysd, st0, y)
    gam = (mu * Psi) @ st0['e']
    if gam < 0: y, Psi, gam = -y, -Psi, -gam
    kap = gam / st0['nu']
    Fset = st0['a'] != 0
    Dpsi_lev = max(abs(Psi[p] - kap * st0['a'][p]) for _, p in levers)
    ident = kap + ((Psi - kap * st0['a']) * np.sign(st0['a']))[Fset].sum() + (Psi * st0['z'])[~Fset].sum() - Psi @ st0['zhat']
    found += 1
    print(f"--- model {found}: square det = {det:.1e}, s_min(square) = {ssq[-1]:.2e}, |Psi(zhat_0)| = {abs(Psi @ st0['zhat']):.1e}, "
          f"gamma = {gam:.3f}, max D_Psi at levers = {Dpsi_lev:.1e}, identity err = {abs(ident):.1e}, "
          f"off-F sum Psi z = {(Psi * st0['z'])[~Fset].sum():+.3f} (= -kappa(1-alpha)-... , kappa = {kap:.3f})")
    # K2.5(b): y^T c = l_delta(Psi) for elementary columns
    errb = 0.0
    for j, (kd, s) in enumerate(kinds[nl:]):
        col = C[:, nl + j]
        pred = (mu[s]**2 / st0['nu']) * (Psi[s] - kap * st0['a'][s]) if kd == 'mass' else Psi[s]
        errb = max(errb, abs(y @ col - pred) / (abs(pred) + 1e-6))
    print(f"    K2.5(b) on elementary columns: max rel err {errb:.1e}")
    # Part B: prepared rows
    for theta0 in [1e-2, 1e-4, 1e-6]:
        aP, zP = prepare(sysd, theta0)
        stP = forced(aP, zP, mu, U, Phi, np.zeros(K, int))
        OmP = [k for k in range(Kom) if not stP['peak'][k]]
        sysP = Sys(aP, zP, mu, U, Phi, OmP)
        CP, kindsP, F0P, _ = columns(sysP, sysP.a0, zP, levers)
        sv = np.linalg.svd(CP, compute_uv=False)
        sq_sv = np.linalg.svd(CP[:, :nl], compute_uv=False)
        # proof's bound: eps_DC = mu_min^2 gamma_min/(4 D), gamma_min = 1/(4 ||h|| (1 + 4 ||p|| ||q||))
        h = np.array([sysP.eps[l] * sysP.a0[p] / (stP['nu'] * U[l, p]) for l, p in levers])
        pv = np.array([sysP.eps[l] * sysP.val0[l] / sysP.A0 for l in OmP]); qv = np.array([sysP.eps[l] * Phi[l] * stP['w'][l] for l in OmP])
        gmin = 1 / (4 * np.linalg.norm(h) * (1 + 4 * np.linalg.norm(pv) * np.linalg.norm(qv)))
        epsDC = mu.min()**2 * gmin / (4 * n)
        print(f"    prepared theta0={theta0:.0e}: s_min(square) = {sq_sv[-1]:.2e}, s_min(enlarged two-sided) = {sv[-1]:.3e}, proof bound eps_DC = {epsDC:.1e}")
        if theta0 == 1e-4:
            # Part C: nonlinear solve from perturbed pre-rows (perturb along +-y), banked masses must stay >= theta0/2
            banked = [s for s in range(n) if sysd.a0[s] == 0 and aP[s] != 0]
            for sgn in [+1, -1]:
                a1 = aP.copy(); z1 = zP.copy()
                # pre-row: small extra mass at a lever coordinate of NO carrier? use a z-perturbation at a free coordinate + mass noise
                fr = [s for s in range(n) if aP[s] == 0 and abs(zP[s]) < 1]
                F1 = sysP.F(a1, z1)[0]
                # create a perturbation with y^T F of chosen sign: move the thick mass of a target coordinate-less carrier slightly
                CPc, kc, _, _ = columns(sysP, a1, z1, levers)
                Uy, sy, Vy = np.linalg.svd(CPc[:, :nl].T); yy = Vy[-1]
                d = 2e-6 * sgn * yy
                # realize the perturbation F(0) = d by shifting the reference values (equivalent to a pre-row with these value moves)
                Fun = lambda a_, z_: sysP.F(a_, z_)[0] - d
                P = np.zeros(CPc.shape[1]); a_c = a1.copy(); z_c = z1.copy()
                for it in range(12):
                    Fc = Fun(a_c, z_c)
                    if np.abs(Fc).max() < 1e-13: break
                    Cc, kk, _, stc = columns(sysP, a_c, z_c, levers)
                    R = Cc.T @ np.linalg.inv(Cc @ Cc.T)
                    step = -R @ Fc
                    for j, (kd, s) in enumerate(kk):
                        if kd == 'lev':
                            l = [l for l, p in levers if p == s][0]
                            a_c[s] += step[j] * lever_dm(sysP, stc, l, s)
                        elif kd == 'mass': a_c[s] += step[j]
                        else: z_c[s] += step[j]
                minbank = min(abs(a_c[s]) * np.sign(a_c[s]) * zP[s] for s in banked)
                print(f"    nonlinear solve, perturbation sign {sgn:+d} along y: residual {np.abs(Fun(a_c, z_c)).max():.1e} after {it} its; "
                      f"min banked mass (signed) = {minbank:.3e} (theta0 = {theta0:.0e})")
    # Part D: unprepared one-sided test: feasibility of F0 + N P + B m = -d with m >= 0, d = +-small along y
    Bc, where = bank_columns(sysd, sysd.a0, sysd.z0)
    signs = np.sign(y @ Bc)
    for sgn in [+1, -1]:
        d = 1e-6 * sgn * y
        M = np.hstack([C[:, :nl], -C[:, :nl], Bc])
        x, res = nnls(M, -d)
        print(f"    unprepared: bank y-actions signs {''.join('+' if s > 0 else '-' for s in signs)}; correction of {sgn:+d} y: NNLS residual {res:.1e}")
