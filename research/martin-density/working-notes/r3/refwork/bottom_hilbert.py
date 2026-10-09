"""Referee check: Hilbert capacity at the bottom scale in Model N.
f: one-sided near-threshold peaks of both types at all scales (E's Model N).  f': n_conv converted resources
(both types at g adjacent scales, n_conv = 2g) and EVERYTHING else ideal: all core errors carried (A=0 at f'),
no frozen error (eta = 0), matched resources above the band unchanged, finer ones destroyed (deep peaks).
Reports sup P_f, P_f'(tau -> 0) and the ratio; the ratio is a LOWER bound for R in any EC scenario."""
import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); A=float(sys.argv[3]); B=float(sys.argv[4])
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
taus_f=np.exp(np.linspace(0,np.log(1/r),24,endpoint=False))
supf=max(solve(t,sg,lam,rho,np.zeros_like(lam),1.0,A,B,M,a0)[0] for t in taus_f for sg in (1,-1))
out=[f"a0={a0} delta={delta} A={A} B={B}: supf={supf:.4f}, B*S^2={B:.3f}"]
for g in (1,2,3,4,6):
    rho_p=rho.copy()
    # convert both types at g adjacent scales lam = 1, 1/2, ..., destroy finer (deep peaks), keep coarser matched
    i1=np.arange(n1)
    for i in i1:
        if lam[i] < r**(g-1) - 1e-12:   # finer than the band: deep peaks of the opposite... make them deep
            rho_p[i]=-50.0; rho_p[n1+i]=50.0
        elif lam[i] <= 1+1e-12:          # band: off-peak, centred
            rho_p[i]=0.0; rho_p[n1+i]=0.0
    tiny=min(max(solve(t,sg,lam,rho_p,np.zeros_like(lam),1.0,0.0,B,M,a0)[0] for sg in (1,-1)) for t in [r**12])
    out.append(f"  converted scales g={g} (n_conv={2*g}): P_f'(tau=2^-12)={tiny:.4f}  ratio={tiny/supf:.4f}  (B S^2/(n_conv supf)={B/(2*g*supf):.4f})")
print("\n".join(out))
