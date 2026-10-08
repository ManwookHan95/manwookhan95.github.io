import numpy as np
rng = np.random.default_rng(1)

def Nnorm(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi*w)

def J_of_zeta(zeta, Phi, nM=400):
    # maximize <w,zeta> s.t. ||w||_inf + ||Phi w||_2 <= 1 ; parametrize by M, C=1-M
    best = (-np.inf, None, None)
    def solve_given_M(M):
        C = 1.0 - M
        # w(k) = clip(lam*zeta/Phi^2, -M, M), choose lam s.t. ||Phi w|| = C (if possible)
        def wl(lam):
            return np.clip(lam*zeta/Phi**2, -M, M)
        lo, hi = 0.0, 1.0
        while np.linalg.norm(Phi*wl(hi)) < C and hi < 1e12:
            hi *= 2
        if np.linalg.norm(Phi*wl(hi)) < C:
            w = wl(hi)  # saturated everywhere
            return w
        for _ in range(200):
            mid = 0.5*(lo+hi)
            if np.linalg.norm(Phi*wl(mid)) < C: lo = mid
            else: hi = mid
        return wl(hi)
    Ms = np.linspace(1e-4, 1-1e-4, nM)
    vals = []
    for M in Ms:
        w = solve_given_M(M)
        vals.append(w @ zeta)
    i = int(np.argmax(vals))
    # refine by golden section around Ms[i]
    a = Ms[max(i-1,0)]; b = Ms[min(i+1,nM-1)]
    g = (np.sqrt(5)-1)/2
    c1 = b - g*(b-a); c2 = a + g*(b-a)
    f1 = solve_given_M(c1) @ zeta; f2 = solve_given_M(c2) @ zeta
    for _ in range(100):
        if f1 > f2:
            b, c2, f2 = c2, c1, f1
            c1 = b - g*(b-a); f1 = solve_given_M(c1) @ zeta
        else:
            a, c1, f1 = c1, c2, f2
            c2 = a + g*(b-a); f2 = solve_given_M(c2) @ zeta
    M = 0.5*(a+b)
    w = solve_given_M(M)
    return w, w @ zeta, M

n = 14
Phi = 2.0**(-np.arange(1, n+1)) * (0.5 + rng.random(n))
zeta = rng.standard_normal(n) * 2.0**(-np.arange(1, n+1)) * 3
zeta[5] = 1e-6; zeta[9] = -2e-7  # make some small entries (likely off-peak)
w, znorm, M = J_of_zeta(zeta, Phi)
C = np.linalg.norm(Phi*w)
print("M, C, M+C:", M, C, M+C, " N(w)=", Nnorm(w,Phi))
P = np.abs(np.abs(w) - np.max(np.abs(w))) < 1e-7
thr = Phi**2 * M * znorm / C
print("peak set (numerical):", np.where(P)[0])
print("threshold rule     :", np.where(np.abs(zeta) >= thr*(1-1e-6))[0])
off = ~P
print("off-peak formula check max err:", np.max(np.abs(w[off] - C*zeta[off]/(Phi[off]**2*znorm))) if off.any() else None)

# single-coordinate certificate expansion check (Cor 5.2): omega = c' e_k at an off-peak k
ks = np.where(off)[0]
k = ks[0]
cprime = 3.0
omega = np.zeros(n); omega[k] = cprime
d = (Phi*w) @ (Phi*omega) / C
H = (np.linalg.norm(Phi*omega)**2 - d**2)/C
gap = M - abs(w[k])
kappa = 2*abs(d)*M/C
r = min(gap/(2*abs(cprime)), 1/(2*abs(d)) if d!=0 else np.inf, C/(2*abs(d)*M) if d!=0 else np.inf)
print("k, w(k), gap, d, H, radius:", k, w[k], gap, d, H, r)
for s in [r, r/2, r/10, r/100, -r, -r/3]:
    W = (1-d*s)*w + s*omega
    lhs = Nnorm(W, Phi)
    rhs = 1 + 0.5*s**2*H*(1+kappa*abs(s))
    print(f"s={s:+.3e}  N(W)-1={lhs-1:.6e}  bound-1={rhs-1:.6e}  ok={lhs<=rhs+1e-15}  ratio={(lhs-1)/(0.5*s**2*H):.6f}")
