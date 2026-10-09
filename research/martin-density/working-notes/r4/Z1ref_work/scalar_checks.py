import numpy as np
rng = np.random.default_rng(1)
s = lambda t: np.sqrt(1+t*t)
# (1) P2A Lemma 1.4 slack inequality (Z1 1.4): worst case over grids
worst = -1e9
for rho in np.linspace(0.01,0.999,60):
    for T0 in np.linspace(0.01,1,40):
        eps = (1-rho**2)*T0**2/6; eta = (1-rho**2)*T0/6
        tau = np.concatenate([np.linspace(T0,1,200), np.linspace(1,1e3,400)])
        v = s(rho*tau)+eps+tau*eta - s(tau)
        worst = max(worst, v.max())
        delta = T0**2/3
        tau2 = np.linspace(0,T0,200)
        v2 = 1+tau2**2/2*(1-delta) - s(tau2)
        worst = max(worst, v2.max())
print("1.4 slack: max violation", worst)
# (2) flip lemma pointwise inequalities (Z1 4.1)
viol=0
for _ in range(200000):
    a = rng.normal()*rng.random(); t = 10**rng.uniform(-3,0)
    Bp, Bm = rng.normal(scale=3*abs(a)/t+1e-9,size=2)
    sg = np.sign(a) if a!=0 else 1.0
    fm = max(sg*Bm - abs(a)/t,0); fp = max(-sg*Bp-abs(a)/t,0); e = max(sg*Bp-2*abs(a)/t,0)
    viol = max(viol, e - (abs(Bp-Bm)+fm))
    bcl = np.sign(Bp)*min(abs(Bp),2*abs(a)/t)
    viol = max(viol, abs(Bp-bcl) - (e+fp))
print("flip lemma pointwise: max violation", viol)
# (3) ray lemma algebra: (1 - tau b0)(1 + tau0 X) = 1 + tau*(X - b0), tau0 = tau/(1 - tau b0)
m=0
for _ in range(10000):
    tau, b0, X = rng.uniform(0,0.1), rng.normal(), rng.normal()
    tau0 = tau/(1-tau*b0)
    m = max(m, abs((1-tau*b0)*(1+tau0*X) - (1+tau*(X-b0))))
print("ray algebra identity err", m)
# (4) convexity bound for peak terms: phi(tau)=||w+tau*Om||_inf - sigma_k (w+tau*Om)(k), k peak
m=-1
for _ in range(20000):
    n=8; w = rng.uniform(-1,1,n); M = np.abs(w).max(); k = np.argmax(np.abs(w)); sk=np.sign(w[k])
    Om = rng.normal(size=n); t = rng.uniform(0.01,1); tau = rng.uniform(0,t)
    phi = lambda u: np.abs(w+u*Om).max() - sk*(w+u*Om)[k]
    m = max(m, phi(tau) - tau/t*phi(t))
print("peak convexity bound max violation", m)
# (5) Z1 2.4(b): rho*tau*D1 + rho^2 tau^2 G/2 <= s(tau)-1 on [c_rho D1, t/2]
worst=-1
for _ in range(20000):
    rho = rng.uniform(0.05,0.999); G = rng.uniform(0,1/rho**2*0.999); t = 10**rng.uniform(-4,-0.5)
    D1 = rng.uniform(0,t/2); c = 4*rho/(1-rho**2*G)
    lo = c*D1; hi=t/2
    if lo>=hi: continue
    tau = np.linspace(lo,hi,50)
    v = 1+rho*tau*D1+rho**2*tau**2*G/2 - s(tau)
    worst=max(worst,v.max())
print("2.4(b) interval inequality max violation", worst)
