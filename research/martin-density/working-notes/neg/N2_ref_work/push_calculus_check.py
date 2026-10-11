# Check of the referee push calculus (i): (L*(omega - d w))(zhat) = sum_{k in P} omega(k) s_k lambda_k mu^_k, and (ii) block bound.
exec(open('pbmodel.py').read())
import random as rr
rr.seed(5)
for label, zf in (('f', zh), ('f_3', zhat_fun(3)), ('f_10', zhat_fun(10))):
    zeta, w, M, C, th, nz = forced(zf)
    P = [k for k in u if abs(abs(w[k]) - M) < mp.mpf('1e-40')]
    om = {k: mp.mpf(rr.uniform(-1, 1))*10 for k in rr.sample(list(u), 25)}
    d = sum(Phi[k]**2*w[k]*om.get(k, 0) for k in u)/C
    lhs = sum(Phi[k]*(om.get(k, 0) - d*w[k])*ev(u[k], zf) for k in u)
    rhs = sum(om.get(k, 0)*mp.sign(w[k])*Phi[k]*(abs(ev(u[k], zf)) - th*Phi[k]) for k in P)
    # (ii): block bound for a small t with an inward push on Sigma_+ peaks
    t = mp.mpf('1e-4'); S_t = [k for k in Splus if Phi[k] <= t/5]
    om2 = {k: mp.mpf('0.4')*M/t for k in S_t}
    d2 = sum(Phi[k]**2*w[k]*om2.get(k, 0) for k in u)/C
    W = {k: (1 - t*d2)*w[k] + t*om2.get(k, 0) for k in u}
    NW = max(abs(x) for x in W.values()) + mp.sqrt(sum((Phi[k]*W[k])**2 for k in u))
    bnd = 1 + t**2*sum((Phi[k]*om2[k])**2 for k in S_t)/(2*(C + t*d2*M))
    print(label, ' identity (i): lhs=%s rhs=%s diff=%s ;  (ii): N(W)-1=%s bound-1=%s' % (
        mp.nstr(lhs, 12), mp.nstr(rhs, 12), mp.nstr(lhs - rhs, 3), mp.nstr(NW - 1, 8), mp.nstr(bnd - 1, 8)))
