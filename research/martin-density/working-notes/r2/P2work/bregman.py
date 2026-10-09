import numpy as np
from scipy.optimize import brentq, minimize_scalar
rng=np.random.default_rng(0)
n=60; m=1
Phi=2.0**(-np.arange(1,n+1))*rng.uniform(0.3,1,n)
lam=m*Phi
def J(zeta):
    # maximize <w,zeta> s.t. ||w||_inf + ||Phi w||_2 <= 1
    def inner(M):
        C=1-M
        def wmu(mu): return np.clip(mu*zeta/Phi**2,-M,M)
        f=lambda mu: np.linalg.norm(Phi*wmu(mu))-C
        if f(1e12)<0: w=wmu(1e12)
        else: w=wmu(brentq(f,0,1e12,xtol=1e-14,rtol=1e-14,maxiter=500))
        return w
    r=minimize_scalar(lambda M:-inner(M)@zeta,bounds=(1e-9,1-1e-9),method='bounded',options={'xatol':1e-13})
    w=inner(r.x); return w
def normv(zeta,w): return w@zeta
# base point: u_k values, with some off-peak coordinates (small u)
u=rng.uniform(-1,1,n)
u[[2,5,9,14,20,30]]*=1e-3*np.array([1,2,1,3,1,1])*Phi[[2,5,9,14,20,30]]/Phi[[2,5,9,14,20,30]]
u[[2,5,9]]=Phi[[2,5,9]]*rng.uniform(-0.5,0.5,3)*50
zeta=lam*u
w=J(zeta); nz=w@zeta
print("M",np.abs(w).max(),"offpeaks",np.sum(np.abs(np.abs(w)-np.abs(w).max())>1e-9))
for A in [1e-2,3e-3,1e-3,3e-4,1e-4,3e-5]:
    vals=[]
    for rep in range(5):
        d=A*rng.uniform(-1,1,n)
        z2=lam*(u+d); w2=J(z2)
        e=1-(w@z2)/(w2@z2)
        vals.append(e/A)
    print(A, max(vals))
