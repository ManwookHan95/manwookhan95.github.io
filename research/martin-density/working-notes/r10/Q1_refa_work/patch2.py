import sys
fn = sys.argv[1]
s = open(fn).read()
old = """        if j > 0:
            k = idx[j-1]; S += Phi[k]**2; Q -= nu[k]**2*Phi[k]**2
        if j == len(idx):
            return None
        num = R - M*M*S
        if num <= 0:
            return None
        t = mp.sqrt(num/Q)"""
new = """        if j > 0:
            k = idx[j-1]; S += Phi[k]**2
        if j == len(idx):
            return None
        Q = mp.fsum(nu[kk]**2*Phi[kk]**2 for kk in idx[j:])
        num = R - M*M*S
        if num <= 0:
            return None
        if Q <= 0:
            continue
        t = mp.sqrt(num/Q)"""
assert old in s, 'pattern'
s = s.replace(old, new)
open(fn, 'w').write(s)
print('patched', fn)
