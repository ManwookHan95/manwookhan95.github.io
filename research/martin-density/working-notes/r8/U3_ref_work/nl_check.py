"""U3 Part 5 numerics: finite model of Theorem NL (failure of lower semicontinuity of the fibre map
at a self-aligned row along rows with one far anti-type flip).

Model (N = 1, one block, m = 1 so lambda_k = Phi_k):
  coordinates 0,1 = F = {p, p'} (base support, a > 0 there), others off F, all contacts (|z| = 1).
  carriers: c1 (target e_2, signature {3,4,5}, z=+1)    robust swallowing-type peak
            c2 (target e_6, signature {7,8},  z=-1)     robust swallowing-type peak
            lm (target y* = (e_0-e_1)/q*, signature {9,10}, z=+1)  tuned: val < 0 tiny -> anti-type strict non-peak (q<0)
            o  (target y*, signature {11,12}; z=-1 in f (aligned peak), z=+1 in f_n (anti-type peak))
  U diagonal: U^* e_j^* = s_j kappa_j.
Quantities: q*(A) = ||A||_1 + ||s*A||_2 ; N(W) = ||W||_inf + ||Phi*W||_2 ; R^* W = sum_k lambda_k W(k) u_k.
Mate set relaxed to a finite grid of t: C_grid(f) = {g : p*(f + t g) <= s(t), t in grid}.  We maximize g(x) for
x = e_{s1}/psi(s1) - e_{s2}/psi(s2) (s1, s2 in the signature set of c1), psi = R^* w.
Theory (Proposition S3 / Theorem NL): at f the maximum is positive (oscillating mates), at f_n it is ~0.
"""
import numpy as np, cvxpy as cp, sys

def build(flip, eta=2e-3, Phi=None, sdiag=None, delta=None, ratio=None):
    n = 13
    if sdiag is None:
        sdiag = np.array([0.6, 0.5] + [0.3*0.7**j for j in range(n-2)])
    if Phi is None:
        Phi = np.array([0.3, 0.1, 0.03, 0.01])
    if delta is None:
        delta = np.array([0.2, 0.2, 0.2, 0.02])
    sig = {0: [3,4,5], 1: [7,8], 2: [9,10], 3: [11,12]}
    tgt = {0: {2: 1.0}, 1: {6: 1.0}, 2: {0: 1.0, 1: -1.0}, 3: {0: 1.0, 1: -1.0}}
    def qstar(A):
        return np.abs(A).sum() + np.linalg.norm(sdiag*A)
    U = []  # carrier vectors u_k (normalized by q*)
    for k in range(4):
        y = np.zeros(n)
        for j, c in tgt[k].items(): y[j] = c
        y = y/qstar(y)
        h = np.zeros(n)
        for s in sig[k]: h[s] = 2.0**(-(s - sig[k][0]) - 1)
        v = y + delta[k]*h
        U.append(v/qstar(v))
    U = np.array(U)            # 4 x n
    lam = Phi.copy()           # m = 1
    z = np.zeros(n); z[0] = z[1] = 1.0
    z[[2,3,4,5]] = 1.0; z[6] = 1.0   # c1 target and signature +1; c2 target coordinate 6 +1
    z[[7,8]] = -1.0 if False else -1.0
    # c2: target e_6 with z_6=+1 would make val positive; make c2 aligned negative: z_6=-1, signature -1
    z[6] = -1.0
    z[[9,10]] = 1.0                  # lm signature +1 (anti-type, since val < 0)
    z[[11,12]] = (1.0 if flip else -1.0)
    # tune a = (a0, a1) so that n_lm val_lm = -eta (val computed with the normalized u)
    def forced(r):
        a = np.zeros(n); a[0] = r; a[1] = 1.0
        a = a/qstar(a)
        nu = np.linalg.norm(sdiag*a)
        zhat = z.copy(); zhat[0] += sdiag[0]**2*a[0]/nu; zhat[1] += sdiag[1]**2*a[1]/nu
        val = U @ zhat
        return a, zhat, val
    if ratio is None:
        lo, hi = 0.01, 100.0
        for _ in range(200):
            mid = np.sqrt(lo*hi)
            _, _, val = forced(mid)
            if val[2] + eta > 0: hi = mid
            else: lo = mid
        ratio = np.sqrt(lo*hi)
    a, zhat, val = forced(ratio)
    zeta = lam*val
    # norming functional w of zeta for N(W) = ||W||_inf + ||Phi W||_2
    w = cp.Variable(4)
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    prob.solve(solver='CLARABEL')
    w = w.value; normz = prob.value
    f = a + (lam*w) @ U
    return dict(n=n, U=U, lam=lam, Phi=Phi, s=sdiag, a=a, z=z, zhat=zhat, val=val, w=w, f=f, normz=normz, ratio=ratio)

def pstar(M, h):
    n = M['n']
    A = cp.Variable(n); W = cp.Variable(4); tau = cp.Variable()
    cons = [A + cp.multiply(M['lam'], W) @ M['U'] == h,
            cp.norm(A, 1) + cp.norm(cp.multiply(M['s'], A), 2) <= tau,
            cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= tau]
    p = cp.Problem(cp.Minimize(tau), cons); p.solve(solver='CLARABEL')
    return p.value

def max_mate(M, x, tgrid):
    n = M['n']
    g = cp.Variable(n)
    cons = []
    for t in tgrid:
        A = cp.Variable(n); W = cp.Variable(4)
        st = np.sqrt(1 + t*t)
        cons += [A + cp.multiply(M['lam'], W) @ M['U'] == M['f'] + t*g,
                 cp.norm(A, 1) + cp.norm(cp.multiply(M['s'], A), 2) <= st,
                 cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= st]
    p = cp.Problem(cp.Maximize(x @ g), cons)
    p.solve(solver='CLARABEL', tol_gap_abs=1e-11, tol_gap_rel=1e-11, tol_feas=1e-11, max_iter=500)
    return p.value, g.value

if __name__ == '__main__':
    M0 = build(flip=False)
    M1 = build(flip=True, ratio=M0['ratio'])
    for name, M in (('f', M0), ('f_n', M1)):
        psi = (M['lam']*M['w']) @ M['U']
        print(name, 'val =', np.round(M['val'], 5), ' w =', np.round(M['w'], 5), ' |zeta| =', round(M['normz'], 6))
        print('   p*(f) =', round(pstar(M, M['f']), 9), '  z*psi on signature coords:',
              np.round((M['z']*psi)[[3,4,5,7,8,9,10,11,12]], 6))
    print('p*(f_n - f) =', pstar(M0, M1['f'] - M0['f']))
    s1, s2 = 3, 4
    for kmin in (-15, -20, -25, -30, -35, -40):
        ks = np.arange(kmin, 11, 1)/10.0
        grid = np.concatenate([10**ks, -10**ks])
        out = []
        for M in (M0, M1):
            psi = cp.multiply(M['lam'], M['w']).value @ M['U'] if False else (M['lam']*M['w']) @ M['U']
            x = np.zeros(M['n']); x[s1] = 1/psi[s1]; x[s2] = -1/psi[s2]
            v, g = max_mate(M, x, grid)
            out.append(v)
        print('t_min = %.1e :  max pi(s1)-pi(s2) over C_grid(f) = %.6e ,  over C_grid(f_n) = %.6e' % (10**(kmin/10), out[0], out[1]))
        sys.stdout.flush()
