"""Referee check: Model N with the real-norm coupling peak cost ~ margin: a0*(1+delta) = cpk*delta (R3 4.7: alpha = delta Phi^2 M/C).
One absolute shift V (one type converted in a band of ratio (2+delta)/delta) or one shift per type (both types).
Bottom value P_f'(tau->0) = B S^2 / n_band (equal split, rooms unbounded as tau->0); compare with sup P_f."""
import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5; B=0.5
cpk=float(sys.argv[1]); Afac=float(sys.argv[2])
for delta in (1.0,0.3,0.1,0.03):
    a0=cpk*delta/(1+delta); A=Afac*cpk*delta
    lam,rho=f_config(r,-24,30,delta); n1=len(lam)//2
    taus=np.exp(np.linspace(0,np.log(1/r),12,endpoint=False))
    supf=max(solve(t,sg,lam,rho,np.zeros_like(lam),1.0,A,B,M,a0)[0] for t in taus for sg in (1,-1))
    best=None
    for sc in np.linspace(0.6,1.6,11):
        S=sc*(1+delta); rho_p=rho-S/lam
        band=np.where(np.abs(rho_p)<1)[0]
        # bottom: only band carriers usable; equal split weighted by availability (all available as tau->0)
        bottom=min(max(solve(t,sg,lam,rho_p,np.zeros_like(lam),1.0,0.0,B,M,a0)[0] for sg in (1,-1)) for t in [r**16])
        if best is None or bottom<best[0]: best=(bottom,len(band),round(sc,2))
    print(f"cpk={cpk} A={A:.4f} a0={a0:.4f} delta={delta}: supf={supf:.4f}; one shift: best bottom={best[0]:.4f} (n_band={best[1]}, shift={best[2]}) ratio={best[0]/supf:.3f}; two shifts ~ ratio/2={best[0]/supf/2:.3f}")
