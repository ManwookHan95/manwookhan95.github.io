"""X2 finite model (N = 1 block, m = 1 so lambda_k = Phi_k), diagonal base U^* e_j^* = s_j k_j.
Exact forced data via the threshold equation (no SOCP needed for the norming functional).
Coordinates: F = {0, 1} (support of a, a > 0, z = +1 there); carriers k = 0..K-1 with targets on F and disjoint
signature sets S_k (all contacts, z = sigma_k on S_k unless changed by levers).
"""
import numpy as np
from scipy.optimize import brentq

class Model:
    def __init__(self, K=4, nsig=6, Phi=None, delta=None, tg=None, sig=None, sdiag=None, abase=(1.0, 0.7)):
        self.K = K; self.nsig = nsig
        self.n = 2 + K*nsig
        self.Phi = np.array(Phi if Phi is not None else [0.2, 0.08, 0.05, 0.02][:K])
        self.lam = self.Phi.copy()
        self.delta = np.array(delta if delta is not None else [0.3]*K)
        self.s = np.array(sdiag if sdiag is not None else [0.6, 0.5] + [0.4*0.8**j for j in range(self.n-2)])
        self.S = [list(range(2 + k*nsig, 2 + (k+1)*nsig)) for k in range(K)]
        tg = tg if tg is not None else [(1.0, 0.2), (1.0, -1.0), (0.5, 1.0), (-1.0, 0.3)][:K]
        self.sig = np.array(sig if sig is not None else [1, -1, 1, -1][:K], dtype=float)
        U = []
        for k in range(K):
            y = np.zeros(self.n); y[0], y[1] = tg[k]; y = y/self.qstar(y)
            h = np.zeros(self.n)
            for i, j in enumerate(self.S[k]): h[j] = 2.0**(-i-1)
            v = y + self.delta[k]*h
            U.append(v/self.qstar(v))
        self.U = np.array(U)
        a = np.zeros(self.n); a[0], a[1] = abase
        self.a0 = a/self.qstar(a)
        z = np.zeros(self.n); z[0] = z[1] = 1.0
        for k in range(K): z[self.S[k]] = self.sig[k]
        self.z0 = z

    def qstar(self, A):
        return np.abs(A).sum() + np.linalg.norm(self.s*A)

    def block(self, zeta):
        """norming functional w of zeta for N(W) = ||W||_inf + ||Phi W||_2; returns w, A=|zeta|, M, C, theta, peaks."""
        Phi = self.Phi; nu = np.abs(zeta)/Phi**2
        def G(th):
            P = nu >= th
            A = (Phi[P]**2*(nu[P] - th)).sum()
            return A**2 - th**2*(Phi[P]**2).sum() - (nu[~P]**2*Phi[~P]**2).sum()
        hi = nu.max(); lo = 1e-300
        th = brentq(G, lo*0 + 1e-14*hi, hi*(1 - 1e-15), xtol=1e-16*hi, rtol=1e-15, maxiter=500)
        P = nu >= th
        A = (Phi[P]**2*(nu[P] - th)).sum()
        M = th/(A + th); C = A/(A + th)
        w = np.where(P, np.sign(zeta)*M, C*zeta/(Phi**2*A))
        return dict(w=w, A=A, M=M, C=C, theta=th, P=P, nuk=nu)

    def forced(self, A_un, z):
        """forced data of the row with base vector A_un (unnormalized, z = sgn A on supp A) and sign vector z."""
        a = A_un/self.qstar(A_un)
        nu = np.linalg.norm(self.s*a); e = self.s*a/nu
        zhat = z + self.s*e                      # (Ue)_j = s_j e_j with e as coefficient vector on k_j
        val = self.U @ zhat
        zeta = self.lam*val
        B = self.block(zeta)
        q0 = 1.0/(1.0 + B['A'])
        f = a + (self.lam*B['w']) @ self.U
        return dict(a=a, nu=nu, e=e, zhat=zhat, val=val, zeta=zeta, q0=q0, f=f, **B)

    def d(self, D, om):
        """d(omega) = <D w, D omega>/C for omega supported off the peaks"""
        return (self.Phi**2*D['w']*om).sum()/D['C']

    def H(self, D, om):
        Dom = self.Phi*om
        return ((Dom**2).sum() - self.d(D, om)**2)/D['C']

    def h(self, D, b):
        Ub = self.s*b
        e = D['e']
        perp = Ub - (Ub @ e)*e
        return (perp @ perp)/D['nu']
