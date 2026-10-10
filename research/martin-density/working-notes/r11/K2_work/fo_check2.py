# first-order formulas in high precision (mpmath) to avoid cancellation at deep coordinates
import mpmath as mp, random
mp.mp.dps = 60
random.seed(7)
def run():
    worst = mp.mpf(0)
    for trial in range(300):
        n = random.randint(8, 25)
        mu = [mp.mpf('0.5')*mp.mpf('0.7')**i*mp.mpf(random.uniform(0.5,1)) for i in range(n)]
        F = [random.random() < 0.5 for i in range(n)]; F[0] = True
        a = [mp.mpf(random.gauss(0,1))*mp.mpf(random.uniform(0.01,1)) if F[i] else mp.mpf(0) for i in range(n)]
        q = sum(abs(x) for x in a) + mp.sqrt(sum((mu[i]*a[i])**2 for i in range(n)))
        a = [x/q for x in a]
        z = [mp.sign(a[i]) if F[i] else mp.mpf(random.uniform(-1,1)) for i in range(n)]
        def val(aa, zz, u):
            nu = mp.sqrt(sum((mu[i]*aa[i])**2 for i in range(n)))
            return sum(u[i]*(zz[i] + mu[i]*mu[i]*aa[i]/nu) for i in range(n)), nu
        u = [mp.mpf(random.gauss(0,1))*mp.mpf('0.8')**i for i in range(n)]
        v0, nu = val(a, z, u)
        kap = sum(mu[i]**2*u[i]*a[i] for i in range(n))/nu**2
        Fi = [i for i in range(n) if F[i]]
        s = random.choice(Fi); dm = mp.mpf('1e-20')*mp.sign(a[s])
        a2 = list(a); a2[s] += dm
        v1, _ = val(a2, z, u)
        pred = mu[s]**2/nu*(u[s] - kap*a[s])*dm
        scale = mu[s]**2/nu*(abs(u[s]) + abs(kap*a[s]))*abs(dm)
        worst = max(worst, abs((v1 - v0) - pred)/scale)
        # bank at a non-support coordinate with z set to a contact sign
        offs = [i for i in range(n) if not F[i]]
        if offs:
            s = random.choice(offs); z2 = list(z); z2[s] = mp.mpf(1) if random.random()<0.5 else mp.mpf(-1)
            v0b, nub = val(a, z2, u)
            a3 = list(a); a3[s] = z2[s]*mp.mpf('1e-20')
            v1b, _ = val(a3, z2, u)
            pred = mu[s]**2/nub*u[s]*z2[s]*mp.mpf('1e-20')
            sc = mu[s]**2/nub*abs(u[s])*mp.mpf('1e-20')
            if sc > 0: worst = max(worst, abs((v1b-v0b)-pred)/sc)
    return worst
print("first-order formulas (support mass, bank), max relative error (mpmath 60 digits):", mp.nstr(run(), 5))
