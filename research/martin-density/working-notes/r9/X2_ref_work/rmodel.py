"""X2-referee independent finite model (several blocks, diagonal base), written from scratch.
Row data: base vector A (unnormalized), sign vector z (|z|<=1, z = sgn A on supp A).
Forced data: a = A/q*(A), nu = ||U^*a||, e = U^*a/nu, zhat = z + U e, values u_k(zhat), block vectors zeta_m(k) = lambda_k u_k(zhat).
Block norm N(W) = ||W||_inf + ||Phi W||_2; the norming functional w of zeta is computed by solving the threshold equation
for C by bisection on the clamp equation  sum_k min(Phi_k (1-c)/c, v_k)^2 = 1,  v_k = |zeta(k)|/(Phi_k |zeta|)  is circular in |zeta|,
so we instead solve for theta via (E1),(E2) with mpmath-free bisection and VERIFY with cvxpy on a few instances.
"""
import numpy as np

class Row:
    def __init__(self, mu, U, blk, Phi, F):
        self.mu = np.asarray(mu, float)            # diagonal base: U^* e_s^* = mu_s k_s, (U h)_s = mu_s h_s
        self.U = np.asarray(U, float)              # carriers x coordinates, each row normalized: q*(u) = 1
        self.blk = np.asarray(blk, int)            # block index m >= 1 of each carrier
        self.Phi = np.asarray(Phi, float)
        self.lam = self.blk*self.Phi               # lambda_k = m Phi_k
        self.F = list(F)
        self.N = self.blk.max()

    def qstar(self, A):
        return np.abs(A).sum() + np.linalg.norm(self.mu*A)

    @staticmethod
    def block_norming(zeta, Phi):
        """norming functional of zeta for the norm with dual N(W) = ||W||_inf + ||Phi W||_2.
        Uses (E1): A = sum_P Phi^2 (nu - th), (E2): A^2 = th^2 Phi_P^2 + sum_Q nu^2 Phi^2, nu = |zeta|/Phi^2."""
        nu = np.abs(zeta)/Phi**2
        def G(th):
            P = nu >= th
            A = (Phi[P]**2*(nu[P] - th)).sum()
            return A*A - th*th*(Phi[P]**2).sum() - (nu[~P]**2*Phi[~P]**2).sum()
        lo, hi = 0.0, nu.max()
        # G(hi) < 0 (A = 0 at th = max nu, unless degenerate), G(0+) > 0
        for _ in range(400):
            mid = 0.5*(lo + hi)
            if G(mid) > 0: lo = mid
            else: hi = mid
        th = 0.5*(lo + hi)
        P = nu >= th
        A = (Phi[P]**2*(nu[P] - th)).sum()
        M = th/(A + th); C = A/(A + th)
        w = np.where(P, np.sign(zeta)*M, C*zeta/(Phi**2*A))
        return dict(w=w, A=A, M=M, C=C, theta=th, P=P, nu=nu)

    def forced(self, A_un, z):
        a = A_un/self.qstar(A_un)
        nu = np.linalg.norm(self.mu*a)
        e = self.mu*a/nu
        zhat = z + self.mu*e
        val = self.U @ zhat
        out = dict(a=a, nu=nu, e=e, zhat=zhat, val=val, blocks={})
        Atot = 0.0
        for m in range(1, self.N + 1):
            idx = np.where(self.blk == m)[0]
            B = self.block_norming(self.lam[idx]*val[idx], self.Phi[idx])
            B['idx'] = idx
            out['blocks'][m] = B
            Atot += B['A']
        out['q0'] = 1.0/(1.0 + Atot)
        return out

    def nv(self, D, k):
        m = self.blk[k]; B = D['blocks'][m]
        return self.lam[k]*D['val'][k]/B['A']

    def d(self, D, m, om):
        """d_m(omega) = <D w, D omega>/C for omega (indexed by carriers of block m, vanishing on peaks)"""
        B = D['blocks'][m]; idx = B['idx']
        return (self.Phi[idx]**2*B['w']*om).sum()/B['C']

    def H(self, D, m, om):
        B = D['blocks'][m]; idx = B['idx']
        Dom = self.Phi[idx]*om
        return ((Dom**2).sum() - self.d(D, m, om)**2)/B['C']
