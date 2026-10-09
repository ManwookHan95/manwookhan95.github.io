"""Model N (E notes part 4) with error carrying (EC): at f', for tau <= tau_gen the core-error cost is removed
(errors carried by converted generic coordinates, Hilbert cost ~ t^4, neglected), for tau > tau_gen the frozen
error of the band certificate is absorbed in the base as in Model N.  Error-dominated regime a0 = 0.03.
Band: ONE group scalar (both types shifted toward 0, opposite detector coefficients) -> J = 1 or 2 converted resources."""
import numpy as np, sys
from modelN import solve, f_config
r=0.5; M=0.5; A=1.0; B=0.5
a0=float(sys.argv[1]); delta=float(sys.argv[2]); gen_oct=float(sys.argv[3]); shiftc=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
lam,rho=f_config(r,-20,24,delta); n1=len(lam)//2
def sup_prof(lam,rho,eta,taus,Afun):
    best=0.0; arg=None
    for t in taus:
        for sg in (1,-1):
            v=solve(t,sg,lam,rho,eta,1.0,Afun(t),B,M,a0)[0]
            if v>best: best=v; arg=(t,sg)
    return best,arg
taus_f=np.exp(np.linspace(0,np.log(1/r),24,endpoint=False))
supf,_=sup_prof(lam,rho,np.zeros_like(lam),taus_f,lambda t:A)
S=shiftc*(1+delta)  # one shift converting the band at scale ~1
rho_p=rho.copy(); lam1=lam[:n1]
rho_p[:n1]=rho[:n1]-S/lam1; rho_p[n1:]=rho[n1:]+S/lam1
band=np.where(np.abs(rho_p)<1)[0]
taus=np.exp(np.linspace(np.log(r**8),np.log(r**-16),193))
tau_gen=r**(-gen_oct)
room=M*(1-np.abs(rho_p[band]))*lam[band]; xfr=room/room.sum()
eta=np.zeros_like(lam); eta[band]=lam[band]*xfr
# with EC: A=0 for tau<=tau_gen, frozen error eta absorbed above
supEC,argEC=sup_prof(lam,rho_p,eta,taus,lambda t:(0.0 if t<=tau_gen else A))
supNo,argNo=sup_prof(lam,rho_p,eta,taus,lambda t:A)
print(f"a0={a0} delta={delta} band={np.round(lam[band],3)} rho={np.round(rho_p[band],2)} supf={supf:.4f}")
print(f"  without EC (room weights): R={supNo/supf:.4f} at {argNo}")
print(f"  with EC up to {gen_oct} octaves above band: R={supEC/supf:.4f} at {argEC}")
# variant: the frozen error itself is carried up to tau_F = tau_gen^2 (band units), resource errors up to tau_gen
tau_F=tau_gen**2
def sup2(taus):
    best=0.0; arg=None
    for t in taus:
        for sg in (1,-1):
            if t<=tau_gen: v=solve(t,sg,lam,rho_p,eta,1.0,0.0,B,M,a0)[0]
            elif t<=tau_F: v=solve(t,sg,lam,rho_p,np.zeros_like(eta),1.0,A,B,M,a0)[0]
            else: v=solve(t,sg,lam,rho_p,eta,1.0,A,B,M,a0)[0]
            if v>best: best=v; arg=(t,sg)
    return best,arg
taus2=np.exp(np.linspace(np.log(r**8),np.log(max(r**-16,4*tau_F)),241))
s2,a2=sup2(taus2)
print(f"  with EC of resource errors to tau_gen and of frozen error to tau_F={tau_F:.3g}: R={s2/supf:.4f} at {a2}")
