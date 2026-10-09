"""Referee check: ec_modelN.py (one group scalar converting BOTH types at one scale) with variable A, B.
Reports supf, the bottom value P_f'(tau -> 0) and R with EC (resource errors carried to tau_gen, frozen to tau_gen^2)."""
import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); gen_oct=float(sys.argv[3]); A=float(sys.argv[4]); B=float(sys.argv[5])
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
taus_f=np.exp(np.linspace(0,np.log(1/r),24,endpoint=False))
supf=max(solve(t,sg,lam,rho,np.zeros_like(lam),1.0,A,B,M,a0)[0] for t in taus_f for sg in (1,-1))
S=(1+delta)
rho_p=rho.copy(); lam1=lam[:n1]
rho_p[:n1]=rho[:n1]-S/lam1; rho_p[n1:]=rho[n1:]+S/lam1
band=np.where(np.abs(rho_p)<1)[0]
room=M*(1-np.abs(rho_p[band]))*lam[band]; xfr=room/room.sum()
eta=np.zeros_like(lam); eta[band]=lam[band]*xfr
tau_gen=r**(-gen_oct); tau_F=tau_gen**2
best=0; arg=None
taus2=np.exp(np.linspace(np.log(r**8),np.log(max(r**-16,4*tau_F)),241))
for t in taus2:
    for sg in (1,-1):
        if t<=tau_gen: v=solve(t,sg,lam,rho_p,eta,1.0,0.0,B,M,a0)[0]
        elif t<=tau_F: v=solve(t,sg,lam,rho_p,np.zeros_like(eta),1.0,A,B,M,a0)[0]
        else: v=solve(t,sg,lam,rho_p,eta,1.0,A,B,M,a0)[0]
        if v>best: best=v; arg=(round(t,4),sg)
print(f"A={A} B={B} a0={a0} delta={delta} nband={len(band)} supf={supf:.4f} EC(gen={gen_oct}) R={best/supf:.4f} at {arg}")
