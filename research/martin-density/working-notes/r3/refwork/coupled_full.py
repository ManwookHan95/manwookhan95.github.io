"""Referee check: full EC profile (R3's ec_onetype scheme) in Model N with peak cost tied to margin, a0(1+delta) = cpk*delta.
One absolute shift (one type converted). EC: core-error cost 0 for tau <= tau_gen, frozen error carried to tau_F = tau_gen^2."""
import numpy as np, sys
sys.path.insert(0, '../work')
from modelN import solve, f_config
r=0.5; M=0.5; B=0.5
cpk=float(sys.argv[1]); Afac=float(sys.argv[2]); delta=float(sys.argv[3]); g=float(sys.argv[4]); nshift=int(sys.argv[5])
a0=cpk*delta/(1+delta); A=Afac*cpk*delta
lam,rho=f_config(r,-22,26,delta); n1=len(lam)//2
def sp(lam,rho,taus,fun):
    best=0;arg=None
    for t in taus:
        for sg in (1,-1):
            eta,Aeff=fun(t)
            v=solve(t,sg,lam,rho,eta,1.0,Aeff,B,M,a0)[0]
            if v>best: best=v;arg=(round(t,4),sg)
    return best,arg
supf,_=sp(lam,rho,np.exp(np.linspace(0,np.log(2),16,endpoint=False)),lambda t:(np.zeros_like(lam),A))
res=[]
for sc in (0.7,1.0,1.3):
    S=sc*(1+delta)
    if nshift==1:
        rho_p=rho-S/lam
    else:  # both types shifted toward 0 (one group scalar with opposite coefficients)
        rho_p=rho.copy(); rho_p[:n1]=rho[:n1]-S/lam[:n1]; rho_p[n1:]=rho[n1:]+S/lam[n1:]
    band=np.where(np.abs(rho_p)<1)[0]
    room=M*(1-np.abs(rho_p[band]))*lam[band]; xfr=room/room.sum()
    eta=np.zeros_like(lam); eta[band]=lam[band]*xfr
    tg=2.0**g; tF=tg**2
    taus=np.exp(np.linspace(np.log(r**8),np.log(4*tF),161))
    def fun_ec(t):
        if t<=tg: return eta,0.0
        if t<=tF: return np.zeros_like(eta),A
        return eta,A
    s1,a1=sp(lam,rho_p,taus,fun_ec)
    res.append((s1/supf,len(band),sc,a1))
best=min(res)
print(f"cpk={cpk} A={A:.4f} a0={a0:.4f} delta={delta} nshift={nshift} supf={supf:.4f}: best EC(g={g}) R={best[0]:.4f} (n_band={best[1]}, shift={best[2]}, at {best[3]})")
