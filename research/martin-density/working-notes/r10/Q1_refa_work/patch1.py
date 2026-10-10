s = open('pm_ref.py').read()
s = s.replace("mp.mp.dps = 90", "mp.mp.dps = 64")
s = s.replace("    for _ in range(300):\n        mid = (lo + hi)/2\n        if g(mid) > 0: lo = mid", "    for _ in range(230):\n        mid = (lo + hi)/2\n        if g(mid) > 0: lo = mid")
s = s.replace("mp.mpf(10)**(-80)", "mp.mpf(10)**(-58)")
s = s.replace("if abs(S2['A'] - A_) < mp.mpf(10)**(-70): break", "if abs(S2['A'] - A_) < mp.mpf(10)**(-55): break")
old = """    d = nP
    lo, hi = mp.mpf(0), 4*Phi[d]**2"""
new = """    target = [None]*len(Phi)
    for k in range(nP + nO):
        target[k] = abs(zeta[k])/Phi[k]**2          # intended rho at theta = 1
    for _ in range(4):                               # rescale coarse values so that rho = target at the actual threshold
        S = solve(zeta, Phi); th = S['M']/S['t']
        for k in range(nP + nO):
            zeta[k] = (1 if zeta[k] > 0 else -1)*target[k]*th*Phi[k]**2
    S = solve(zeta, Phi)
    if not all(S['rho'][k] >= 1.2 for k in range(nP)) or not all(S['rho'][k] < 1 for k in range(nP, nP + nO)):
        return None
    d = nP
    lo, hi = mp.mpf(0), 4*Phi[d]**2*S['M']/S['t']"""
assert old in s
s = s.replace(old, new)
s = s.replace("    for _ in range(200):\n        mid = (lo + hi)/2\n        z = list(zeta); z[d] = sgn*mid", "    for _ in range(150):\n        mid = (lo + hi)/2\n        z = list(zeta); z[d] = sgn*mid")
s = s.replace("for mu, r, W in (('1e-6', '1e-2', '1e-14'), ('1e-10', '1e-3', '1e-22'), ('1e-14', '1e-2', '1e-30')):",
              "for mu, r, W in (('1e-6', '1e-2', '1e-14'), ('1e-9', '1e-3', '1e-20'), ('1e-12', '1e-2', '1e-26')):")
open('pm_ref.py','w').write(s)
print('patched')
