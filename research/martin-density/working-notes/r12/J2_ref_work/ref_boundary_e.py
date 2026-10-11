"""J2-ref: Lemma J2.1(e) at the boundary of its hypotheses: b = Phi_Pf^2/(6 Phi_W^2) (or the a-constraint active),
all weak peaks at rho = 1 + b (extreme), heavy weak-peak mass, light robust mass; double precision bisection solvers."""
import numpy as np
rng = np.random.default_rng(3)

def true_th(z, P):
    nu = z/P**2
    f = lambda th: np.sum(np.maximum(z - th*P**2, 0))**2 - np.sum(P**2*np.minimum(th, nu)**2)
    lo, hi = 1e-14, nu.max()*2
    for _ in range(200):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    th = (lo+hi)/2
    return th, np.sum(np.maximum(z - th*P**2, 0))

def froz(z, P, Pf):
    nu = z/P**2
    Q = ~Pf
    Af = lambda th: np.sum(z[Pf] - th*P[Pf]**2)
    f = lambda th: Af(th)**2 - (th**2*np.sum(P[Pf]**2) + np.sum(nu[Q]**2*P[Q]**2))
    lo, hi = 1e-14, np.sum(z[Pf])/np.sum(P[Pf]**2)
    if f(lo) <= 0: return None
    for _ in range(200):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    th = (lo+hi)/2
    return th, Af(th)

worst = [0, 0, 0, 0]; tested = 0; viol = 0
for trial in range(20000):
    nr, nw, nn = rng.integers(1, 3), rng.integers(1, 6), rng.integers(0, 6)
    n = nr + nw + nn
    P = np.concatenate([rng.uniform(0.01, 0.08, nr), rng.uniform(0.1, 0.4, nw), rng.uniform(0.01, 0.4, nn)])
    PhiPf2 = np.sum(P[:nr]**2); PhiW2 = np.sum(P[nr:nr+nw]**2)
    b = min(PhiPf2/(6*PhiW2), 0.5) * rng.uniform(0.9, 1.0)
    rho = np.concatenate([[0.0], rng.uniform(1.2, 30.0, nr-1), np.full(nw, 1 + b*rng.uniform(0.98, 1.0)), rng.uniform(0, 1, nn)])
    Pm = np.zeros(n, bool); Pm[:nr+nw] = True
    a = np.sqrt(np.sum(P[Pm]**2) + np.sum(rho[~Pm]**2*P[~Pm]**2))
    rest = np.sum((rho[1:nr+nw]-1)*P[1:nr+nw]**2)
    rho[0] = 1 + (a - rest)/P[0]**2
    if rho[0] <= 1.05: continue
    z = rho*P**2   # theta = 1
    th, A = true_th(z, P)
    if abs(th - 1) > 1e-9: continue
    if not (6*b*PhiW2 <= PhiPf2 + 1e-15 and 2*b*PhiW2 <= A/th): continue
    Pf = np.zeros(n, bool); Pf[:nr] = True
    out = froz(z, P, Pf)
    tested += 1
    if out is None: viol += 1; continue
    thf, Af = out
    x = b*PhiW2/PhiPf2
    r1 = (th - thf)/(3*th*x); r2 = abs(Af - A)/(4*th*x); r3 = (thf - th)
    worst[0] = max(worst[0], r1); worst[1] = max(worst[1], r2); worst[2] = max(worst[2], r3)
    if r1 > 1 or r2 > 1 or r3 > 1e-12: viol += 1
print('tested', tested, 'violations', viol)
print('max (theta-theta_f)/(3 b theta x) = %.4f, max |A_f-A|/(4 b theta x) = %.4f, max theta_f - theta = %.2e' % tuple(worst[:3]))
