"""
N3-ref sanity check 2 (finite model; NOT a statement about Martin's space).
Corollary 2.4' (margin form) predicts: if no strict non-peak and no degenerate peak sees Z = S u {j_f} and the
margin-sparsity rate holds at Z (automatic in a finite model: finitely many carriers), then every mate is proportional
to psi' on Z, whatever the WEIGHT and the (positive) MARGIN of the peaks seeing Z.
We add one carrier k6 ~ e1 - (1 - delta) e2 (sees S = {1,2}); u6(xhat) = delta/q* sets its margin.  Small delta ->
small margin; below the threshold k6 becomes a strict non-peak.  Expect: Osc_max ~ grid level while k6 is a peak
(any margin above the grid resolution), Osc_max ~ sqrt(H6) once it is a strict non-peak.
Caveat: the fibre is discretized on |t| in [1e-5, 3.2]; a peak of margin mu has capacity ~ min(t/mu, lambda/t), so
margins below ~ 1e-4 are not resolved by the grid.
"""
import numpy as np
from floor_check import model, build_row, max_osc

for phi6 in [5e-4]:
    for delta in [0.3, 0.05, 0.01, 2e-3, 5e-4, 1e-4, 0.0]:
        raw6 = np.array([0.0, 1.0, -(1.0 - delta), 0, 0, 0, 0])
        u, Phi, lam, Rs = model(raw6, phi6)
        a, z, xh, w, f, psi, zeta = build_row(u, Phi, lam, Rs, 0.0)
        sig_hat = zeta @ w; M_ = np.max(np.abs(w)); C_ = np.linalg.norm(Phi * w)
        c = 1.0 / (1.0 + sig_hat)                              # c' = q(x'), x' = xhat/p(xhat)
        theta6 = abs(u[6] @ xh) * c                            # |x'(u6)|
        vartheta = (c * sig_hat) * M_ / C_                     # sigma' M / (m C), m = 1
        margin6 = theta6 - vartheta * Phi[6]
        peak6 = abs(abs(w[6]) - M_) < 1e-7
        o, st = max_osc(Phi, Rs, f, psi)
        H6 = lam[6] * (abs(u[6][1]) + abs(u[6][2]))
        print(f"phi6={phi6:.0e} delta={delta:7.1e}: k6 {'PEAK    ' if peak6 else 'NON-PEAK'} margin={margin6: .3e} "
              f"|w6|/M={abs(w[6])/M_:.4f}  Osc_max={o:10.3e}  Osc/sqrt(H6)={o/np.sqrt(H6):6.3f} [{st}]")
