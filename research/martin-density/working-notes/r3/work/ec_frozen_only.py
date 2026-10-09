import numpy as np, sys
from modelN import solve, f_config
r=0.5; M=0.5; A=1.0; B=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); tauF=float(sys.argv[3])
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
def sp(lam,rho,taus,etafun):
    best=0;arg=None
    for t in taus:
        for sg in (1,-1):
            v=solve(t,sg,lam,rho,etafun(t),1.0,A,B,M,a0)[0]
            if v>best: best=v;arg=(round(t,3),sg)
    return best,arg
supf,_=sp(lam,rho,np.exp(np.linspace(0,np.log(2),24,endpoint=False)),lambda t:np.zeros_like(lam))
S=(1+delta); rho_p=rho.copy(); rho_p[:n1]=rho[:n1]-S/lam[:n1]; rho_p[n1:]=rho[n1:]+S/lam[n1:]
band=np.where(np.abs(rho_p)<1)[0]
room=M*(1-np.abs(rho_p[band]))*lam[band]; xfr=room/room.sum()
eta=np.zeros_like(lam); eta[band]=lam[band]*xfr
taus=np.exp(np.linspace(np.log(r**8),np.log(max(4*tauF,2**16)),241))
# frozen error carried (eta := 0 in the comparison) for t<=tauF; but for t <= band, certificate uses x=xfr: cost of
# representation errors: with eta=0 the model charges A*lam*|x|/tau for band use -> emulate exact certificate by eta=lam*x at t<=1
def etaf(t):
    if t<=1.0: return eta
    return np.zeros_like(eta) if t<=tauF else eta
s,a=sp(lam,rho_p,taus,etaf)
print(f"a0={a0} delta={delta} tauF={tauF}: R={s/supf:.4f} at {a}")
