"""Finite toy model of Martin's norm p (one or more blocks) for sanity checks.

X = R^n with base dual norm q*(A) = ||A||_1 + ||U^T A||_2, blocks m with carriers u_{k,m} (vectors in R^n),
weights lam_{k,m} = m*Phi_{k,m}, block dual norm N_m(W) = ||W||_inf + ||D_m W||_2, L^*W = sum lam W(k) u_k.
p*(h) = min s : q*(A) <= s, N_m(W_m) <= s, A + L^*W = h.
Finite models are degenerate (everything attains its norm); they only test signs/algebra and scale profiles.
"""
import numpy as np
import cvxpy as cp

SOLVER = cp.CLARABEL


class Model:
    def __init__(self, U, blocks):
        # U: n x r ; blocks: list of dicts with 'u' (K x n), 'Phi' (K,), 'm' (int)
        self.U = U
        self.n = U.shape[0]
        self.blocks = blocks
        for b in blocks:
            b['lam'] = b['m'] * b['Phi']

    def Lstar(self, Ws):
        return sum(b['u'].T @ (b['lam'] * W) for b, W in zip(self.blocks, Ws))

    def qstar(self, A):
        return np.abs(A).sum() + np.linalg.norm(self.U.T @ A)

    def Nm(self, b, W):
        return np.abs(W).max() + np.linalg.norm(b['Phi'] * W)

    def pstar(self, h, return_dec=False):
        A = cp.Variable(self.n)
        Ws = [cp.Variable(len(b['Phi'])) for b in self.blocks]
        s = cp.Variable()
        cons = [cp.norm1(A) + cp.norm(self.U.T @ A) <= s]
        for b, W in zip(self.blocks, Ws):
            cons.append(cp.norm_inf(W) + cp.norm(cp.multiply(b['Phi'], W)) <= s)
        Ls = sum(b['u'].T @ cp.multiply(b['lam'], W) for b, W in zip(self.blocks, Ws))
        cons.append(A + Ls == h)
        pr = cp.Problem(cp.Minimize(s), cons)
        pr.solve(solver=SOLVER)
        if return_dec:
            return s.value, A.value, [W.value for W in Ws]
        return s.value

    def block_primal(self, b, zeta):
        """|zeta|_m = min max(||alpha||_1, ||beta||_2) s.t. zeta = alpha + D beta."""
        al = cp.Variable(len(zeta)); be = cp.Variable(len(zeta)); s = cp.Variable()
        pr = cp.Problem(cp.Minimize(s), [cp.norm1(al) <= s, cp.norm(be) <= s,
                                          al + cp.multiply(b['Phi'], be) == zeta])
        pr.solve(solver=SOLVER)
        return s.value

    def norming(self, b, zeta):
        """w = argmax <w,zeta> s.t. N(w) <= 1 (unique by strict convexity)."""
        w = cp.Variable(len(zeta))
        pr = cp.Problem(cp.Maximize(zeta @ w), [cp.norm_inf(w) + cp.norm(cp.multiply(b['Phi'], w)) <= 1])
        pr.solve(solver=SOLVER)
        return w.value, pr.value

    def first_row(self, a, z):
        """Forced data from (a,z): returns dict with f, xi, zhat, q0, w (list), zeta (list), sigma, M, C."""
        e = self.U.T @ a; nu = np.linalg.norm(e); e = e / nu
        zhat = z + self.U @ e
        assert abs(a @ zhat - 1) < 1e-8, a @ zhat
        zetas_hat = [b['lam'] * (b['u'] @ zhat) for b in self.blocks]
        norms = [self.block_primal(b, zh) for b, zh in zip(self.blocks, zetas_hat)]
        q0 = 1.0 / (1.0 + sum(norms))
        xi = q0 * zhat
        ws, zetas, sig, Ms, Cs = [], [], [], [], []
        for b, zh in zip(self.blocks, zetas_hat):
            zeta = q0 * zh
            w, val = self.norming(b, zeta)
            ws.append(w); zetas.append(zeta); sig.append(val)
            Ms.append(np.abs(w).max()); Cs.append(np.linalg.norm(b['Phi'] * w))
        f = a + self.Lstar(ws)
        return dict(f=f, xi=xi, zhat=zhat, q0=q0, w=ws, zeta=zetas, sigma=sig, M=Ms, C=Cs, e=e, nu=nu, a=a, z=z)


def s_of(t):
    return np.sqrt(1 + t * t)
