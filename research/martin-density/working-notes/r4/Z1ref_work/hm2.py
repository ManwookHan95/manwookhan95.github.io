# Toy check of the referee's "Hoffman matching" construction (Z1_ref part 5).
# K_* = free signature sets S_1..S_3 (truncated) + a few target coordinates outside them.
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(7)
L = 3; ns = 25
S = [list(range(l*ns, (l+1)*ns)) for l in range(L)]
extra = [L*ns, L*ns+1]                      # target coordinates outside signature sets (in K_*)
n = L*ns + len(extra)
eps_sig = np.array([1,1,-1])
z = np.zeros(n)
for l in range(L): z[S[l]] = eps_sig[l]
z[extra] = rng.choice([-1,1], size=len(extra))
delta = np.array([0.3,0.2,0.1])
U = np.zeros((L,n))                          # rows: u_l restricted to K_*
for l in range(L):
    U[l, S[l]] = delta[l]*2.0**(-np.arange(1,ns+1))
U[0, extra[0]] = 0.3                         # coarse free target outside signatures
U[1, S[0][2]] = 0.2;  U[1, extra[1]] = -0.1   # target of l=2 touches S_1 (slaving-closed)
U[2, S[0][4]] = -0.05; U[2, S[1][3]] = 0.07; U[2, extra[0]] = 0.02
w = np.array([1e-2,-2e-2,0.5e-2])
xs = np.array([2.0,1.0,0.0]); vs = U.T@xs
for j in range(n):
    if abs(vs[j])>0: z[j] = np.sign(vs[j]) if (j in extra or z[j]==0) else z[j]
A_ub = -(z[:,None]*U.T)
print('z*v(xi*) min =', (z*vs).min())                      # -z_j v_xi(j) <= 0
def project(x0):
    # min ||xi - x0||_1 s.t. xi in R_0 ; variables xi, s (s >= |xi - x0|)
    c = np.r_[np.zeros(L), np.ones(L)]
    Aub = np.r_[np.c_[A_ub, np.zeros((n,L))],
                np.c_[np.eye(L), -np.eye(L)], np.c_[-np.eye(L), -np.eye(L)]]
    bub = np.r_[np.zeros(n), x0, -x0]
    Aeq = np.r_[w, np.zeros(L)][None,:]
    r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=[0.0], bounds=[(None,None)]*L+[(0,None)]*L, method="highs")
    assert r.status == 0, r.message
    return r.x[:L]
# an exact d-neutral resonance xi* (nonzero): maximise sum eps_l xi_l subject to R_0 and |xi|<=1
r = linprog(-np.r_[eps_sig], A_ub=A_ub, b_ub=np.zeros(n), A_eq=w[None,:], b_eq=[0.0], bounds=[(-1,1)]*L, method="highs")
xistar = r.x; print("exact resonance xi* =", np.round(xistar,4))
for eps in [1e-2,1e-3,1e-4,1e-5]:
    worst = []
    for trial in range(30):
        xi0 = xistar + eps*rng.normal(size=L)              # actual switching -Delta c: near-resonant
        xi0 -= w*(w@xi0)/(w@w) ; xi0 += eps*rng.normal()*w/np.linalg.norm(w)  # d-neutral up to O(eps)
        sigma = U.T@xi0
        J = np.zeros(n); idx = rng.choice(n, 6, replace=False); J[idx] = eps*rng.normal(size=6)   # pinned-target junk
        total = z*(sigma + J)                              # z * DeltaB must be >= 0 up to wrong-signed mass
        pos = np.maximum(total,0); wrong = np.minimum(total,0)
        th = rng.uniform(0,1,n)
        Bp = z*(th*pos) + z*wrong                          # + side: z-signed except wrong mass
        Bm = -z*((1-th)*pos)                               # - side: -z-signed
        assert np.allclose(Bp - Bm, sigma + J)
        xit = project(xi0)
        vxi = U.T@xit
        Bp_clean = z*np.maximum(z*Bp,0)
        zP = np.maximum(0, z*(Bp_clean - vxi)); P = z*zP
        V = Bp_clean - P; W = V - vxi
        ok = (z*V >= -1e-12).all() and (z*W <= 1e-12).all() and (z@vxi*0==0)
        worst.append((np.abs(xit-xi0).sum()/eps, np.abs(P).sum()/eps, np.abs(Bp-V).sum()/eps, ok))
    a = np.array([x[:3] for x in worst]); oks = all(x[3] for x in worst)
    print(f"eps={eps:.0e}: max |xi_t-xi0|/eps={a[:,0].max():.2f}, max ||P||/eps={a[:,1].max():.2f}, max ||B+ - V||/eps={a[:,2].max():.2f}, signs ok={oks}")
