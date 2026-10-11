# Sanity check of the pure-block (PB) staircase example of N2 part 2 in a finite truncated model.
# One block (m=1). Coordinates 1..J (index 0..J-1). Carriers k=1..K.
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(0)
J = 400                      # base coordinates
mu = 2.0**(-np.arange(1, J+1)-10)   # diagonal U
def qstar(b): return np.abs(b).sum() + np.linalg.norm(mu*b)
abar = 1/(1+mu[0])
a = np.zeros(J); a[0] = abar
zhat = np.full(J, 0.5); zhat[0] = 1+mu[0]          # zhat = z + U e, e = e_1
h = np.zeros(J); h[1] = 1; h[2] = -1
e0 = np.zeros(J); e0[1] = 1; e0[2] = 1
K = 40; k0 = 12; theta = 0.2
Phi = np.zeros(K+1); U = np.zeros((K+1, J)); typ = {}
# signature sets: disjoint chunks of coordinates 4..J-1
sigpos = list(range(3, J)); chunk = 5
def sig(k):
    s = np.zeros(J); idx = sigpos[(k*chunk) % len(sigpos):(k*chunk) % len(sigpos)+chunk]
    for j in idx: s[j] = 2.0**(-(j+1))
    return s
for k in range(1, K+1):
    if k == 1:
        c = 1.0; Phi[k] = 2.0**(-1-k)*c
        v = np.zeros(J); v[0] = 1; v += 1e-12*sig(k)
    elif k >= k0 and k % 3 in (0, 1):
        c = 1.0; Phi[k] = 2.0**(-1-k)*c
        beta = -8*Phi[k] if k % 3 == 0 else 8*Phi[k]
        typ[k] = '+' if k % 3 == 0 else '-'
        v = h + beta*e0 + Phi[k]**2*2.0**(-k)*sig(k)
    else:   # generic: random sparse target, made a robust peak by an e_1 correction
        c = 2.0**(-k/4.0); Phi[k] = 2.0**(-1-k)*c
        y = np.zeros(J); sup = rng.choice(np.arange(1, 60), 3, replace=False); y[sup] = rng.normal(size=3)
        y /= qstar(y)
        val = y @ zhat
        s = 0.0 if abs(val) >= 4*Phi[k] else (8*Phi[k] if val >= 0 else -8*Phi[k])
        v = y + s*abar*np.eye(J)[0] + 1e-3*Phi[k]**2*sig(k)
    U[k] = v/qstar(v)
def J_map(zeta, Ph):
    vv = np.abs(zeta)/Ph**2
    A = lambda x: np.maximum(np.abs(zeta)-x*Ph**2, 0).sum()
    B = lambda x: (Ph**2*np.minimum(x, vv)**2).sum()
    Xi = lambda x: A(x)**2 - B(x)
    th = brentq(Xi, 1e-14, vv.max()*(1-1e-12))
    nz = A(th); M = th/(th+nz); C = nz/(th+nz)
    w = np.sign(zeta)*M*np.minimum(1, vv/th)
    return w, M, C, th, nz
def analyse(zh, label):
    zeta = Phi[1:]*(U[1:] @ zh)          # R zhat (lambda_k = Phi_k for m = 1)
    w, M, C, th, nz = J_map(zeta, Phi[1:])
    peaks = np.abs(np.abs(w)-M) < 1e-12
    print(label, 'M=%.4f C=%.4f thr(zhat units)=%.3f  #nonpeaks=%d' % (M, C, th*Phi[1]/Phi[1], (~peaks).sum()))
    vals = U[1:] @ zh
    st = [k for k in typ]
    rel = [abs(vals[k-1])/Phi[k] for k in st]
    print('  staircase |u(zhat)|/Phi in [%.3f, %.3f]; signs ok:' % (min(rel), max(rel)),
          all((vals[k-1] < 0) == (typ[k] == '+') for k in st), ' all staircase peaks:', all(peaks[k-1] for k in st))
    psi = (Phi[1:]*w) @ U[1:]
    worst = -1; info=(0,'',0,0,0,0,0)
    for t in np.geomspace(Phi[K]/theta*1.01, 1e-4, 60):
        for side in ('+', '-'):
            S = [k for k in st if typ[k] == side and Phi[k] <= theta*t]
            if not S: continue
            nu = 0.5
            gam = sum(Phi[k]*nu*M/t/qstar_n[k] for k in S)
            om = np.zeros(K); 
            for k in S: om[k-1] = nu*M/t
            sgn = 1 if side == '+' else -1          # side '+': t>0 ; side '-': t<0, write f - s g
            d = (Phi[1:]**2*w*om).sum()/C
            Wv = (1 - sgn*t*d)*w + sgn*t*om if side == '+' else (1 + t*d)*w - t*om
            if side == '+':
                Wv = (1 - t*d)*w + t*om
            Nn = np.abs(Wv).max() + np.linalg.norm(Phi[1:]*Wv)
            LTheta = ((Phi[1:]*om) @ U[1:]) - d*psi
            B = gam*h - LTheta
            Avec = a + t*B if side == '+' else a - t*B
            qn = qstar(Avec)
            exc = max(Nn, qn) - 1
            if exc/t**2 > worst:
                worst = exc/t**2; info = (t, side, nu, Nn-1, qn-1, d, len(S))
    print('  max (p*-bound - 1)/t^2 = %.4g at t=%.3g side=%s nu=%.3g N-1=%.3g q-1=%.3g d=%.3g |S|=%d' % ((worst,)+info))
qstar_n = {k: qstar(np.concatenate([[0], [0]])) for k in []}
# normalisation constants n_k of staircase vectors
qstar_n = {}
for k in typ:
    beta = -8*Phi[k] if typ[k] == '+' else 8*Phi[k]
    qstar_n[k] = qstar(h + beta*e0 + Phi[k]**2*2.0**(-k)*sig(k))
analyse(zhat, 'f (row with normer zhat):')
for N in (3, 10, 50):
    zN = zhat.copy(); zN[N:] = 0.0
    analyse(zN, 'f_N, N=%d (canonical truncation, NA):' % N)
