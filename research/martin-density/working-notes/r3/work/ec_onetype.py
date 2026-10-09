"""Model N, ONE absolute shift V (both types shifted the same way: P+ converted in a band, P- pushed deeper),
with error carrying: resource errors carried for tau<=tau_gen, frozen error carried for tau<=tau_F=tau_gen^2."""
import numpy as np, sys
from modelN import solve, f_config
r=0.5; M=0.5; A=1.0; B=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); g=float(sys.argv[3]); sc=float(sys.argv[4])
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
def sp(lam,rho,taus,fun):
    best=0;arg=None
    for t in taus:
        for sg in (1,-1):
            eta,Aeff=fun(t)
            v=solve(t,sg,lam,rho,eta,1.0,Aeff,B,M,a0)[0]
            if v>best: best=v;arg=(round(t,3),sg)
    return best,arg
supf,_=sp(lam,rho,np.exp(np.linspace(0,np.log(2),24,endpoint=False)),lambda t:(np.zeros_like(lam),A))
S=sc*(1+delta); rho_p=rho-S/lam
band=np.where(np.abs(rho_p)<1)[0]
room=M*(1-np.abs(rho_p[band]))*lam[band]; xfr=room/room.sum()
eta=np.zeros_like(lam); eta[band]=lam[band]*xfr
tg=2.0**g; tF=tg**2
taus=np.exp(np.linspace(np.log(r**8),np.log(4*tF),241))
def fun_ec(t):
    if t<=tg: return eta,0.0
    if t<=tF: return np.zeros_like(eta),A
    return eta,A
s0,a0_=sp(lam,rho_p,taus,lambda t:(eta,A))
s1,a1=sp(lam,rho_p,taus,fun_ec)
print(f"a0={a0} delta={delta} shift={sc} band lam={np.round(lam[band],3)} rho={np.round(rho_p[band],2)}: noEC R={s0/supf:.4f} at {a0_}; EC(g={g}) R={s1/supf:.4f} at {a1}")
