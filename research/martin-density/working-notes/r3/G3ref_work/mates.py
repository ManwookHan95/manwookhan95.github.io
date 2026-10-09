import numpy as np, warnings
warnings.filterwarnings('ignore')
from model import pstar, build_f
from model2 import make_model2

SGRID = np.concatenate([-np.logspace(-2.5, 2, 36), np.logspace(-2.5, 2, 36)])

def contractive(M, g):
    worst = -1e9
    for s in SGRID:
        val = pstar(M, M['f'] + s*g) - np.sqrt(1+s*s)
        worst = max(worst, val)
        if val > 2e-9: return False, val
    return True, worst

def scale_to_boundary(M, g0, iters=22):
    lo, hi = 0.0, 1.0
    while contractive(M, hi*g0)[0]: hi *= 2
    for _ in range(iters):
        mid = 0.5*(lo+hi)
        if contractive(M, mid*g0)[0]: lo = mid
        else: hi = mid
    return lo

def random_mate(M, rng, kind='random'):
    n = M['n']
    g0 = rng.standard_normal(n)
    if kind == 'contact':          # push weight onto the contact / near-contact coordinates
        g0 *= 0.2; g0[2] += 2.0; g0[3] += 1.0
    g0 -= (g0 @ M['xi'])/(M['a'] @ M['xi']) * M['a']      # g0(xi) = 0
    c = scale_to_boundary(M, g0)
    return 0.999*c*g0

if __name__ == '__main__':
    rng = np.random.default_rng(5)
    M = build_f(make_model2())
    g = random_mate(M, rng, 'contact')
    print('g', np.round(g, 4))
    np.save('g_contact.npy', g)
