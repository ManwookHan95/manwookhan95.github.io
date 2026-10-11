"""Finite one-block model of the Martin-type norm p = q + |R .|_Phi on R^n (sanity checks only).

Dual description:  p*(h) = min max(q*(A), N(W))  over  h = A + R^T W,
   q*(A) = ||A||_1 + ||mu * A||_2,        N(W) = ||W||_inf + ||Phi * W||_2,
   (R^T W) = sum_k lam_k W_k u_k,  lam_k = Phi_k (block index m = 1).
Forced data of the row f[a, z]:  nu = ||mu a||, e = mu a/nu, zhat = z + mu e (diagonal base U k_j = mu_j e_j),
   x = R zhat (x_k = lam_k u_k(zhat)),  w = argmax{<w, x> : N(w) <= 1},  sigma = <w, x>,  q0 = 1/(1 + sigma),
   xi = q0 zhat,  f = a + R^T w.
"""
import numpy as np
import cvxpy as cp

SOLVER = dict(solver=cp.CLARABEL)


def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)


def Nnorm(W, Phi):
    return np.abs(W).max() + np.linalg.norm(Phi * W)


class Row:
    def __init__(self, a, z, U, Phi, mu):
        """U: K x n matrix of carrier vectors (rows), normalized q*(u_k) = 1 by the caller."""
        self.a, self.z, self.U, self.Phi, self.mu = map(np.asarray, (a, z, U, Phi, mu))
        n = len(a)
        K = U.shape[0]
        self.n, self.K = n, K
        self.lam = self.Phi.copy()
        q = qstar(self.a, self.mu)
        self.a = self.a / q
        self.nu = np.linalg.norm(self.mu * self.a)
        self.e = self.mu * self.a / self.nu
        self.zhat = self.z + self.mu * self.e
        self.x = self.lam * (self.U @ self.zhat)
        w = cp.Variable(K)
        prob = cp.Problem(cp.Maximize(self.x @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(self.Phi, w), 2) <= 1])
        prob.solve(**SOLVER)
        self.w = np.array(w.value)
        self.sigma = float(self.x @ self.w)
        self.q0 = 1.0 / (1.0 + self.sigma)
        self.xi = self.q0 * self.zhat
        self.f = self.a + self.RT(self.w)

    def RT(self, W):
        return (self.lam * W) @ self.U

    def pstar(self, h):
        A = cp.Variable(self.n)
        W = cp.Variable(self.K)
        s = cp.Variable()
        cons = [h == A + (cp.multiply(self.lam, W)) @ self.U,
                cp.norm(A, 1) + cp.norm(cp.multiply(self.mu, A), 2) <= s,
                cp.norm(W, 'inf') + cp.norm(cp.multiply(self.Phi, W), 2) <= s]
        prob = cp.Problem(cp.Minimize(s), cons)
        prob.solve(**SOLVER)
        return float(s.value)

    def peaks(self, tol=1e-7):
        M = np.abs(self.w).max()
        return [k for k in range(self.K) if abs(abs(self.w[k]) - M) < tol]

    def max_switch(self, t, k, sign=+1, extra=None):
        """max sign*gamma_k over g with g(xi)=0 and decompositions of f +- t g with norms <= s(t).
        gamma_k = lam_k (Theta_-(k) - Theta_+(k)),  Theta_+ = (W_+ - w)/t,  Theta_- = (w - W_-)/t."""
        n, K = self.n, self.K
        st = np.sqrt(1 + t * t)
        g = cp.Variable(n)
        Ap, Am = cp.Variable(n), cp.Variable(n)
        Wp, Wm = cp.Variable(K), cp.Variable(K)
        cons = [self.f + t * g == Ap + cp.multiply(self.lam, Wp) @ self.U,
                self.f - t * g == Am + cp.multiply(self.lam, Wm) @ self.U,
                self.xi @ g == 0]
        for A in (Ap, Am):
            cons.append(cp.norm(A, 1) + cp.norm(cp.multiply(self.mu, A), 2) <= st)
        for W in (Wp, Wm):
            cons.append(cp.norm(W, 'inf') + cp.norm(cp.multiply(self.Phi, W), 2) <= st)
        if extra is not None:
            cons += extra(g, Ap, Am, Wp, Wm)
        gam = self.lam[k] * ((self.w[k] - Wm[k]) / t - (Wp[k] - self.w[k]) / t)
        prob = cp.Problem(cp.Maximize(sign * gam), cons)
        prob.solve(**SOLVER)
        return float(prob.value), prob.status
