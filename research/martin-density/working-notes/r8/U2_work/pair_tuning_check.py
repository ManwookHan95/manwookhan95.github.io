# Sanity check of Lemma TR-inf case (c): with a diagonal base U k_s = mu_s e_s, a pair of moves on two support
# coordinates s < s' of the same signature set, with Delta = -(alpha_{s'}/alpha_s) Delta', changes the value of the
# owning carrier at first order by (mu_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta' and every other carrier only at
# second order.  Values: val_k = u_k(zhat), zhat = z + U e, e = U^* a/||U^* a||, z = sgn a on F (unchanged by the moves).
import numpy as np
import mpmath as mp
mp.mp.dps = 60
rng = np.random.default_rng(1)
n = 14
mu = [mp.mpf(2)**(-(s+1)**1.5) for s in range(n)]      # fast-decaying diagonal base (mild, to stay in range)
a = [mp.mpf(rng.uniform(0.2,1.0))*(1 if rng.random()<0.6 else -1) for s in range(n)]
F = list(range(n))                                     # every coordinate in the support
z = [mp.sign(x) for x in a]
# carriers: owner l0 has signature on coordinates S0 = {5,7,9}; other carriers random but vanishing on S0
S0 = [5,7,9]
v0 = [mp.mpf(0)]*n
for s in S0: v0[s] = mp.mpf(2)**(-s)
others = []
for k in range(6):
    u = [mp.mpf(rng.normal()) for s in range(n)]
    for s in S0: u[s] = mp.mpf(0)
    others.append(u)
def vals(avec):
    nu = mp.sqrt(sum((mu[s]*avec[s])**2 for s in range(n)))
    e = [mu[s]*avec[s]/nu for s in range(n)]
    zhat = [z[s] + mu[s]*e[s] for s in range(n)]
    return nu, [sum(u[s]*zhat[s] for s in range(n)) for u in [v0]+others]
nu, base = vals(a)
s, sp = 5, 9                                           # s < s'
rho = lambda q: a[q]/v0[q]
alpha = lambda q: mu[q]**2*a[q]/nu**2
for Dp in [mp.mpf('1e-6'), mp.mpf('-1e-6'), mp.mpf('1e-9'), mp.mpf('-1e-9')]:
    D = -(alpha(sp)/alpha(s))*Dp
    a2 = list(a); a2[s] += D; a2[sp] += Dp
    _, new = vals(a2)
    pred = (mu[sp]**2*v0[sp]/nu)*(1 - rho(sp)/rho(s))*Dp
    d_owner = new[0]-base[0]
    d_other = max(abs(new[k]-base[k]) for k in range(1,len(new)))
    print(f"Delta'={mp.nstr(Dp,3):>8}  owner change={mp.nstr(d_owner,12):>20}  predicted={mp.nstr(pred,12):>20}  "
          f"rel.err={mp.nstr(abs(d_owner-pred)/abs(pred),3):>10}  max other change={mp.nstr(d_other,3)}")
# compare with a single (unpaired) move at s': common term present at first order
Dp = mp.mpf('1e-6'); a3 = list(a); a3[sp] += Dp
_, new3 = vals(a3)
print("single move at s': max other change =", mp.nstr(max(abs(new3[k]-base[k]) for k in range(1,len(new3))),4),
      " (first order: ~ |gamma| alpha_{s'} Delta'/nu)")
