"""Finite Martin-type model used by the K2 referee scripts (one or two blocks, diagonal base).
Block norm: |zeta|_Phi with dual N(w) = ||w||_inf + ||Phi w||_2 (Martin Lemma A); computed by the threshold equation
(U1 Lemma 1.2): nu_k = |zeta_k|/Phi_k^2, P = {nu_k > theta}, A = sum_P Phi^2 (nu - theta), A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2,
w = sgn(zeta) M on P, w = C zeta/(Phi^2 A) off P, M = theta/(A + theta), C = A/(A + theta).
"""
import numpy as np
from scipy.optimize import brentq

def block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    hi = nu.max()
    def G(th):
        P = nu > th
        A = (Phi[P]**2 * (nu[P] - th)).sum()
        return A**2 - th**2 * (Phi[P]**2).sum() - (nu[~P]**2 * Phi[~P]**2).sum()
    th = brentq(G, 1e-15 * hi, hi * (1 - 1e-15), xtol=1e-18 * hi, rtol=1e-15, maxiter=2000)
    P = nu > th
    A = (Phi[P]**2 * (nu[P] - th)).sum()
    M = th / (A + th); C = A / (A + th)
    w = np.where(P, np.sign(zeta) * M, C * zeta / (Phi**2 * A))
    return dict(w=w, A=A, P=P, theta=th, M=M, C=C, nu=nu)

def kappa_of(zeta, Phi, Omega_mask):
    """U1 Lemma 1.3: kappa = A + theta Phi_P^2 + (1/theta) sum_{Q minus Omega} nu^2 Phi^2."""
    b = block(zeta, Phi)
    Q = ~b['P']
    S = (b['nu'][Q & ~Omega_mask]**2 * Phi[Q & ~Omega_mask]**2).sum()
    return b['A'] + b['theta'] * (Phi[b['P']]**2).sum() + S / b['theta'], b

def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)

def forced(A_un, z, mu, U, Phi, blocks):
    """Row with unnormalized base A_un and sign vector z.  U: carriers (rows), Phi: weights per carrier, blocks: block index per carrier."""
    a = A_un / qstar(A_un, mu)
    nu = np.linalg.norm(mu * a)
    e = mu * a / nu
    zhat = z + mu * e
    val = U @ zhat
    out = dict(a=a, nu=nu, e=e, zhat=zhat, val=val, z=z)
    W = np.zeros(len(val)); Ab = {}; Pk = np.zeros(len(val), bool); blk = {}
    for m in np.unique(blocks):
        idx = np.where(blocks == m)[0]
        b = block(Phi[idx] * val[idx], Phi[idx])
        W[idx] = b['w']; Ab[m] = b['A']; Pk[idx] = b['P']; blk[m] = b
    out.update(w=W, A=Ab, peak=Pk, blk=blk)
    return out
