# NOTE (referee): this adversarial sign iteration OSCILLATES (peak-coordinate signs of Psi flip); it produced no instance. Kept only as a record of the attempt; the unprepared obstruction rests on Q2-refa C.5 and K1-ref (ref_offset_nonlinear).
"""K2 referee, Part D': adversarial contact signs.  Starting from a singular square lever system (ref_dc_degenerate.py models), set
z_s := -sgn Psi_y(s) at every contact s of the carriers' supports, re-tune the singularity, iterate.  At the fixed point every bank at an
UNPREPARED contact moves y^T F in the same direction (Q2-refa C.5 / K1 2.2 obstruction: one sign of correction along y is impossible with
levers + nonnegative banks).  After preparation (banks of mass theta0 in the BASE row) the enlarged two-sided system is regular and the
nonlinear d-consistency system is solved for both signs, with banked masses staying positive."""
import numpy as np
from scipy.optimize import brentq, nnls
exec(open('ref_dc_degenerate.py').read().split("results = []")[0])

def setup(K, n, S, U, Phi, mu, Kom, nT, z_override, thick, t):
    th = thick.copy(); th[0] = t
    A0, z0 = base_row(K, n, S, U, Kom, nT, th, np.ones(n), np.zeros(n, bool))
    z0 = np.where(np.isnan(z_override), z0, z_override)
    st = forced(A0, z0, mu, U, Phi, np.zeros(K, int))
    Om = [k for k in range(Kom) if not st['peak'][k]]
    if len(Om) < Kom: return None
    sysd = Sys(A0, z0, mu, U, Phi, Om)
    levers = [(l, S[l][0]) for l in Om]
    C, kinds, F0, st0 = columns(sysd, sysd.a0, z0, levers)
    return np.linalg.det(C[:, :len(levers)]), sysd, levers, C, st0

def singular(K, n, S, U, Phi, mu, Kom, nT, zov, thick):
    grid = np.concatenate([-np.linspace(0.8, 0.01, 50), np.linspace(0.01, 0.8, 50)])
    vals = []
    for t in grid:
        r = setup(K, n, S, U, Phi, mu, Kom, nT, zov, thick, t); vals.append(None if r is None else r[0])
    for i in range(len(grid) - 1):
        if vals[i] is not None and vals[i + 1] is not None and vals[i] * vals[i + 1] < 0:
            t = brentq(lambda t: setup(K, n, S, U, Phi, mu, Kom, nT, zov, thick, t)[0], grid[i], grid[i + 1], xtol=1e-14)
            return setup(K, n, S, U, Phi, mu, Kom, nT, zov, thick, t)
    return None

shown = 0
for trial in range(300):
    if shown >= 4: break
    Kom, Kpk, ns, nT = 3, 2, 4, 3
    K, n, S, U, Phi, mu = build(Kom, Kpk, ns, nT)
    thick = rng.choice([-1, 1], Kom) * rng.uniform(0.05, 0.3, Kom)
    zov = np.full(n, np.nan)
    r = singular(K, n, S, U, Phi, mu, Kom, nT, zov, thick)
    if r is None: continue
    ok = False
    for it in range(8):
        det, sysd, levers, C, st0 = r
        nl = len(levers)
        y = np.linalg.svd(C[:, :nl].T)[2][-1]
        Psi = Psi_of(sysd, st0, y)
        if (mu * Psi) @ st0['e'] < 0: y, Psi = -y, -Psi
        Bc, where = bank_columns(sysd, sysd.a0, sysd.z0)
        acts = y @ Bc
        if len(where) and (np.all(acts < 0) or np.all(acts > 0)):
            ok = True; break
        for s in where:
            if abs(Psi[s]) > 1e-12: zov[s] = -np.sign(Psi[s])
        r = singular(K, n, S, U, Phi, mu, Kom, nT, zov, thick)
        if r is None: break
    if not ok: continue
    shown += 1
    gam = (mu * Psi) @ st0['e']
    print(f"--- adversarial model {shown}: s_min(square) = {np.linalg.svd(C[:, :nl], compute_uv=False)[-1]:.1e}, gamma = {gam:.3f}, "
          f"bank y-actions all {'negative' if acts.max() < 0 else 'positive'} (max |.| = {np.abs(acts).max():.2e}, n_banks = {len(where)})")
    for sgn in [+1, -1]:
        d = 1e-6 * sgn * y
        M = np.hstack([C[:, :nl], -C[:, :nl], Bc])
        x, res = nnls(M, -d)
        print(f"    UNPREPARED: correct F(0) = {sgn:+d}e-6 y with levers + nonnegative banks: NNLS residual {res:.2e}")
    for theta0 in [1e-3, 1e-5]:
        aP, zP = prepare(sysd, theta0)
        stP = forced(aP, zP, mu, U, Phi, np.zeros(K, int))
        OmP = [k for k in range(Kom) if not stP['peak'][k]]
        sysP = Sys(aP, zP, mu, U, Phi, OmP)
        CP, kindsP, F0P, _ = columns(sysP, sysP.a0, zP, levers)
        banked = [s for s in range(n) if sysd.a0[s] == 0 and aP[s] != 0]
        msg = []
        for sgn in [+1, -1]:
            d = 0.05 * theta0 * sgn * y
            Fun = lambda a_, z_: sysP.F(a_, z_)[0] - d
            a_c = aP.copy(); z_c = zP.copy()
            for it in range(15):
                Fc = Fun(a_c, z_c)
                if np.abs(Fc).max() < 1e-14: break
                Cc, kk, _, stc = columns(sysP, a_c, z_c, levers)
                step = -Cc.T @ np.linalg.solve(Cc @ Cc.T, Fc)
                for j, (kd, s) in enumerate(kk):
                    if kd == 'lev':
                        l = [l for l, p in levers if p == s][0]
                        a_c[s] += step[j] * lever_dm(sysP, stc, l, s)
                    elif kd == 'mass': a_c[s] += step[j]
                    else: z_c[s] += step[j]
            minbank = min(a_c[s] * zP[s] for s in banked)
            msg.append(f"sign {sgn:+d}: residual {np.abs(Fun(a_c, z_c)).max():.1e}, min banked mass {minbank:.2e}")
        print(f"    PREPARED theta0={theta0:.0e}: s_min(enlarged two-sided) = {np.linalg.svd(CP, compute_uv=False)[-1]:.3f}; solve F = 0.05 theta0 (+-y): " + "; ".join(msg))
