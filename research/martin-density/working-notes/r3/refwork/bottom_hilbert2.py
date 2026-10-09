"""Referee check (corrected): bottom-scale Hilbert capacity in Model N.
f': both types converted (centred, rho=0) at g adjacent scales lam = 1, 1/2, ..., r^(g-1); resources finer than the band
are destroyed as in E's scripts (rho -> rho -+ s/lam, s = 1+delta: deep peaks whose peak cost a0*s*|x|/tau does not decay
with depth); coarser resources matched.  All core errors carried (A = 0 at f'), no frozen error.  The ratio
P_f'(tau->0)/sup P_f is a LOWER bound for R in every EC scenario of R3 (EC cannot add two-sided O(scale)-error capacity)."""
import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); A=float(sys.argv[3]); B=float(sys.argv[4])
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
taus_f=np.exp(np.linspace(0,np.log(1/r),24,endpoint=False))
supf=max(solve(t,sg,lam,rho,np.zeros_like(lam),1.0,A,B,M,a0)[0] for t in taus_f for sg in (1,-1))
s=1+delta
out=[f"a0={a0} delta={delta} A={A} B={B}: supf={supf:.4f}"]
for g in (1,2,3,4,6,8):
    rho_p=rho.copy()
    for i in range(n1):
        if lam[i] < r**(g-1)-1e-12:
            rho_p[i]=rho[i]-s/lam[i]; rho_p[n1+i]=rho[n1+i]+s/lam[i]
        elif lam[i] <= 1+1e-12:
            rho_p[i]=0.0; rho_p[n1+i]=0.0
    vals=[max(solve(t,sg,lam,rho_p,np.zeros_like(lam),1.0,0.0,B,M,a0)[0] for sg in (1,-1)) for t in (r**10, r**14)]
    out.append(f"  g={g} (n_conv={2*g}): P_f'(2^-10)={vals[0]:.4f} P_f'(2^-14)={vals[1]:.4f} ratio={vals[1]/supf:.4f}")
print("\n".join(out))
