# Counterexample to the literal "Reading" of N2 Lemma 1.4: a push on a ROBUST peak (no relevant carrier touched)
# still has a positive second-order block excess when strict non-peaks exist (Part I lem:localformula: d^2_S Lambda = C c_Q/(|zeta| F_2)).
import numpy as np
from scipy.optimize import brentq
def blocknorm(x, Ph):
    v = np.abs(x)/Ph**2
    A = lambda s: np.maximum(np.abs(x)-s*Ph**2, 0).sum()
    B = lambda s: (Ph**2*np.minimum(s, v)**2).sum()
    th = brentq(lambda s: A(s)**2 - B(s), 1e-300, v.max()*(1-1e-15))
    a = A(th); M = th/(th+a); C = a/(th+a)
    return a, np.sign(x)*M*np.minimum(1, v/th), M, C, th
Ph = np.array([0.25, 0.125, 0.0625, 0.03125])
zeta = np.array([0.25*1.0, 0.125*0.9, 0.0625*0.01, 0.03125*0.8])   # carrier 3 should be a strict non-peak
sig, w, M, C, th = blocknorm(zeta, Ph)
P = np.abs(np.abs(w)-M) < 1e-12
print('peaks:', P, ' w =', w, ' M,C =', M, C)
k = 0                                    # robust peak (dominant)
eta = np.zeros(4); eta[k] = Ph[k]        # push on the robust peak only
F2 = (Ph[P]**2).sum(); cQ = ((Ph*w)[~P]**2).sum()
pred = C*cQ/(sig*F2)*(np.sign(w[k])*eta[k])**2/2   # (1/2) d^2_S Lambda * (dS)^2
for t in [1e-2, 3e-3, 1e-3, 3e-4]:
    exc = blocknorm(zeta + t*eta, Ph)[0] - (w*(zeta + t*eta)).sum()
    print('t=%.0e  excess/t^2 = %.6e   lem:localformula prediction = %.6e' % (t, exc/t**2, pred))
