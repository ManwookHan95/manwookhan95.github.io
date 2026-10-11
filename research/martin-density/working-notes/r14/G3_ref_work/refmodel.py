"""Independent finite multi-block model of the Martin-type norm (referee check of G3, Round 14).

Base:   q*(A) = ||A||_1 + ||mu * A||_2               (diagonal base U, h = U e has h_s = mu_s^2 a_s / nu)
Block m: N_m(W) = ||W||_inf + ||Phi_m * W||_2,  R_m^T W = sum_k lam_{m,k} W_k u_{m,k},  lam_{m,k} = m * Phi_m(k)
p*(h) = min max(q*(A), max_m N_m(W_m))  over  h = A + sum_m R_m^T W_m.
Forced data of the row given (a, z):  a normalized (q*(a) = 1), zhat = z + mu^2 a / nu, x_m = lam_m * (U_m zhat),
w_m = argmax{<w, x_m> : N_m(w) <= 1}, |x_m|_m = <w_m, x_m>, q0 = 1/(1 + sum_m |x_m|_m), sigma_m = q0 |x_m|_m,
zeta_m = q0 x_m, xi = q0 zhat, f = a + sum_m R_m^T w_m.
"""
import numpy as np
import cvxpy as cp

SOLVER = dict(solver=cp.CLARABEL)


def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)


def Nnorm(W, Phi):
    return np.abs(W).max() + np.linalg.norm(Phi * W)


class MRow:
    def __init__(self, a, z, Us, Phis, mu, lam_scale=None):
        self.mu = np.asarray(mu, float)
        a = np.asarray(a, float)
        self.a = a / qstar(a, self.mu)
        self.z = np.asarray(z, float)
        self.n = len(a)
        self.Us = [np.asarray(U, float) for U in Us]
        self.Phis = [np.asarray(P, float) for P in Phis]
        self.B = len(Us)
        self.lams = [(m + 1 if lam_scale is None else lam_scale[m]) * self.Phis[m] for m in range(self.B)]
        self.F = np.abs(self.a) > 0
        self.nu = np.linalg.norm(self.mu * self.a)
        self.h = self.mu ** 2 * self.a / self.nu
        self.zhat = self.z + self.h
        self.ws, self.xs, self.normx = [], [], []
        for m in range(self.B):
            x = self.lams[m] * (self.Us[m] @ self.zhat)
            K = len(x)
            w = cp.Variable(K)
            pr = cp.Problem(cp.Maximize(x @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(self.Phis[m], w), 2) <= 1])
            pr.solve(**SOLVER)
            self.ws.append(np.array(w.value))
            self.xs.append(x)
            self.normx.append(float(x @ w.value))
        self.q0 = 1.0 / (1.0 + sum(self.normx))
        self.sigmas = [self.q0 * v for v in self.normx]
        self.zetas = [self.q0 * x for x in self.xs]
        self.xi = self.q0 * self.zhat
        self.f = self.a + sum(self.RT(m, self.ws[m]) for m in range(self.B))

    def RT(self, m, W):
        return (self.lams[m] * W) @ self.Us[m]

    def RT_cp(self, m, W):
        return cp.multiply(self.lams[m], W) @ self.Us[m]

    def pstar(self, hvec):
        A = cp.Variable(self.n)
        Ws = [cp.Variable(len(self.Phis[m])) for m in range(self.B)]
        s = cp.Variable()
        cons = [hvec == A + sum(self.RT_cp(m, Ws[m]) for m in range(self.B)),
                cp.norm(A, 1) + cp.norm(cp.multiply(self.mu, A), 2) <= s]
        for m in range(self.B):
            cons.append(cp.norm(Ws[m], 'inf') + cp.norm(cp.multiply(self.Phis[m], Ws[m]), 2) <= s)
        cp.Problem(cp.Minimize(s), cons).solve(**SOLVER)
        return float(s.value)

    def decomp(self, t, objective_fn, extra=None):
        """Feasible (g, A_+, A_-, W_+, W_-) maximizing objective_fn(vars) subject to the two-sided budget at scale t."""
        st = np.sqrt(1 + t * t)
        g = cp.Variable(self.n)
        Ap, Am = cp.Variable(self.n), cp.Variable(self.n)
        Wp = [cp.Variable(len(self.Phis[m])) for m in range(self.B)]
        Wm = [cp.Variable(len(self.Phis[m])) for m in range(self.B)]
        cons = [self.f + t * g == Ap + sum(self.RT_cp(m, Wp[m]) for m in range(self.B)),
                self.f - t * g == Am + sum(self.RT_cp(m, Wm[m]) for m in range(self.B)),
                self.xi @ g == 0]
        for A in (Ap, Am):
            cons.append(cp.norm(A, 1) + cp.norm(cp.multiply(self.mu, A), 2) <= st)
        for m in range(self.B):
            for W in (Wp[m], Wm[m]):
                cons.append(cp.norm(W, 'inf') + cp.norm(cp.multiply(self.Phis[m], W), 2) <= st)
        V = dict(g=g, Ap=Ap, Am=Am, Wp=Wp, Wm=Wm)
        if extra is not None:
            cons += extra(V)
        pr = cp.Problem(cp.Maximize(objective_fn(V)), cons)
        pr.solve(**SOLVER)
        out = dict(status=pr.status, g=g.value, Ap=Ap.value, Am=Am.value,
                   Wp=[W.value for W in Wp], Wm=[W.value for W in Wm], val=pr.value)
        return out

    def derived(self, t, d):
        """Switching vector, amplitudes, coordinate excesses."""
        Bp = (d['Ap'] - self.a) / t
        Bm = (self.a - d['Am']) / t
        V = Bp - Bm
        Thp = [(d['Wp'][m] - self.ws[m]) / t for m in range(self.B)]
        Thm = [(self.ws[m] - d['Wm'][m]) / t for m in range(self.B)]
        gam = [self.lams[m] * (Thm[m] - Thp[m]) for m in range(self.B)]
        Vrec = sum(gam[m] @ self.Us[m] for m in range(self.B))
        ep = np.abs(d['Ap']) - self.z * d['Ap']
        em = np.abs(d['Am']) - self.z * d['Am']
        return dict(Bp=Bp, Bm=Bm, V=V, Thp=Thp, Thm=Thm, gam=gam, Vrec=Vrec, ep=ep, em=em)
