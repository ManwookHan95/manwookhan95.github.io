"""Sanity check of the kappa-reduction (U1 Lemma 1.3/1.4).

One block, finitely many carriers.  zeta in R^n (zeta(k) = lambda_k u_k(zhat)), weights Phi_k.
Norm |.|_Phi with unit ball B_l1 + D_Phi(B_l2); dual N(w) = ||w||_inf + ||Phi w||_2.
A := |zeta|_Phi, w := norming functional, M := ||w||_inf, C := ||Phi w||_2, theta := A M / C,
nu_k := |zeta(k)|/Phi_k^2, peaks P = {nu >= theta}, Q = complement.
Claims:
 (E1) sum_P Phi^2 (nu - theta) = A,   (E2) A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2
 (K)  data identity coefficient:  kappa_Omega := [A(A+theta) - sum_Omega nu^2 Phi^2]/theta
                                   = A + theta Phi_P^2 + (1/theta) sum_{Q\Omega} nu^2 Phi^2
 (D1) peak push |zeta(c)| += s:  d kappa/ds = 1 - X,  X := C sum_{Q\Omega} nu^2 Phi^2/(theta^2 Phi_P^2)
 (D2) push of a dropped strict non-peak d in Q\Omega: d kappa/ds = rho_d (2 + M X / C),  rho_d = nu_d/theta
 (I)  data identity: for omega^+-, Delta := d(omega^-) - d(omega^+), c_k := lambda_k[(omega^- - omega^+)(k) - Delta w(k)],
      Delta*M * kappa_Omega = sum_{Omega} u_k c_k   (u_k = zeta(k)/lambda_k), lambda_k = m Phi_k.
"""
import numpy as np

rng = np.random.default_rng(1)

def dual_norm(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi * w)

def norming(zeta, Phi, tol=1e-14):
    """Clamp formula: Phi_k w(k) = sgn(zeta_k) min(Phi_k M, C v_k), v_k = |zeta_k|/(Phi_k A).
    Solve for (A, C) by nested bisection: given A, C is the root of F(c) = sum min(Phi(1-c)/c, v)^2 = 1;
    A is then fixed by <w, zeta> = A."""
    def C_of_A(A):
        v = np.abs(zeta) / (Phi * A)
        F = lambda c: np.sum(np.minimum(Phi * (1 - c) / c, v) ** 2) - 1.0
        lo, hi = 1e-15, 1 - 1e-15
        # F decreasing in c
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if F(mid) > 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    def w_of(A):
        C = C_of_A(A)
        M = 1 - C
        v = np.abs(zeta) / (Phi * A)
        w = np.sign(zeta) * np.minimum(Phi * M, C * v) / Phi
        return w, M, C
    # A solves <w(A), zeta> = A; g(A) = <w(A),zeta> - A is decreasing
    lo, hi = 1e-12, np.sum(np.abs(zeta)) + 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        w, M, C = w_of(mid)
        if np.dot(w, zeta) - mid > 0:
            lo = mid
        else:
            hi = mid
    A = 0.5 * (lo + hi)
    w, M, C = w_of(A)
    return A, w, M, C

def block_data(zeta, Phi, Omega):
    A, w, M, C = norming(zeta, Phi)
    theta = A * M / C
    nu = np.abs(zeta) / Phi ** 2
    P = nu >= theta * (1 - 1e-12)
    Q = ~P
    PhiP2 = np.sum(Phi[P] ** 2)
    QmO = Q & ~Omega
    kappa1 = (A * (A + theta) - np.sum((nu[Omega] * Phi[Omega]) ** 2)) / theta
    kappa2 = A + theta * PhiP2 + np.sum((nu[QmO] * Phi[QmO]) ** 2) / theta
    X = C * np.sum((nu[QmO] * Phi[QmO]) ** 2) / (theta ** 2 * PhiP2)
    E1 = np.sum(Phi[P] ** 2 * (nu[P] - theta)) - A
    E2 = A ** 2 - theta ** 2 * PhiP2 - np.sum((nu[Q] * Phi[Q]) ** 2)
    return dict(A=A, w=w, M=M, C=C, theta=theta, nu=nu, P=P, Q=Q, PhiP2=PhiP2,
                kappa1=kappa1, kappa2=kappa2, X=X, E1=E1, E2=E2,
                dual=dual_norm(w, Phi), pair=np.dot(w, zeta))

