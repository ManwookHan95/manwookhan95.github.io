import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5; B=0.5
for (A,a0,delta) in [(1.0,0.03,1.0),(0.5,0.03,1.0),(0.1,0.03,1.0),(0.1,0.01,1.0),(0.03,0.003,1.0),(0.01,0.001,1.0),(0.003,0.0003,1.0)]:
    lam,rho=f_config(r,-24,30,delta)
    taus=np.exp(np.linspace(0,np.log(1/r),12,endpoint=False))
    supf=max(solve(t,sg,lam,rho,np.zeros_like(lam),1.0,A,B,M,a0)[0] for t in taus for sg in (1,-1))
    print(f"A={A} a0={a0} delta={delta}: supf={supf:.4f}  needed n_conv >= B S^2/supf = {B/supf:.2f}")
