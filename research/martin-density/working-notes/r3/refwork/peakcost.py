import numpy as np
rng=np.random.default_rng(1)
n=12; Phi=0.5**np.arange(2,2+n)
# block value w: peaks at +-M on a set P, off-peak elsewhere; normalise so that M + C = 1
for trial in range(3):
    w=rng.uniform(-0.6,0.6,n); P=[0,3,5,8]; sg=np.array([1,-1,1,1])
    w[P]=sg
    M=1.0; C=np.linalg.norm(Phi*w); s=M+C; w=w/s; M=M/s; C=np.linalg.norm(Phi*w)
    assert abs(M+C-1)<1e-12
    k=3; sigma=np.sign(w[k]); delta=0.37
    alpha=np.zeros(n); alpha[k]=sigma*delta*Phi[k]**2*M/C
    rest=[p for p in P if p!=k]; alpha[rest]=np.sign(w[rest])*(1-abs(alpha[k]))/len(rest)  # ||alpha||_1 = 1
    zeta=alpha+Phi**2*w/C                                     # zeta/|zeta| (Fact C form)
    N=lambda W: np.max(np.abs(W))+np.linalg.norm(Phi*W)
    assert abs(N(w)-1)<1e-12 and abs(w@zeta-1)<1e-12        # w norms zeta: <w,zeta> = M + C = 1
    om=-sigma*1.0                                             # inward direction for t>0
    d=Phi[k]**2*w[k]*om/C
    Om=-d*w; Om[k]+=om
    for t in (1e-3,1e-4):
        exc=N(w+t*Om)-1-t*(Om@zeta)
        print(f"trial {trial} t={t}: excess={exc:.6e}  predicted |t om| delta Phi^2 M/C={abs(t*om)*delta*Phi[k]**2*M/C:.6e}")
