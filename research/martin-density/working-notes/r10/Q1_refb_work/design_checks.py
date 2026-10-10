"""Referee (b) for Q1: design-level sanity checks (independent of Q1's scripts).
1. (GM) choice: admissible set nonempty, maximum an endpoint in Q(y), for random rational targets.
2. K_kappa identity: 1 - R^2 = sigma (1 + 2a + sigma)/(a + sigma)^2 from a^2 = sigma + k^2 R^2, k = a + sigma.
3. Cluster capacity induction: c_{L+i} >= (1/2) c^cl 4^{1-i} under worst-case generic choices.
4. Absorber R from lb versus from c: R increases by at most a bounded amount; least entry bound.
"""
from fractions import Fraction as Fr
import itertools, random, math
import mpmath as mp

random.seed(7)

# ---------- 1. (GM) ----------
def H(l):
    # H_l = sum_{i>=1} 2^{-2^l (2i+1)} = 2^{-3*2^l}/(1 - 2^{-2^{l+1}})
    return Fr(1, 2**(3*2**l)) / (1 - Fr(1, 2**(2**(l+1))))

def gm_delta(y, l, normU=Fr(1,4)):
    Hl = H(l)
    dmax = min(Fr(1, 2**l), 1/(4*(1+normU)*Hl))
    g = dmax*Hl/(32*3**len(y))
    # excluded open intervals in delta: |S + eps*delta*H| < g
    bad = []
    for sig in itertools.product((-1,0,1), repeat=len(y)):
        S = sum(s*v for s, v in zip(sig, y))
        for eps in (1,-1):
            # S + eps*delta*H in (-g, g)  <=> delta in ((-g - S)/(eps H), (g - S)/(eps H)) (ordered)
            a = (-g - S)/(eps*Hl); b = (g - S)/(eps*Hl)
            lo, hi = min(a,b), max(a,b)
            bad.append((lo, hi))
    lo0, hi0 = dmax/2, dmax
    # candidates: hi0 and all endpoints inside [lo0, hi0]
    cands = [hi0] + [e for iv in bad for e in iv if lo0 <= e <= hi0]
    def ok(d):
        return all(not (lo < d < hi) for lo, hi in bad)
    good = [d for d in cands if ok(d)]
    tot_bad = sum(hi - lo for lo, hi in bad)
    return max(good) if good else None, tot_bad, dmax

worst_ratio = 0
for trial in range(60):
    n = random.randint(1, 4)
    x = [Fr(random.randint(-9, 9) or 1, random.randint(1, 9)) for _ in range(n)]
    s = sum(abs(v) for v in x)
    y = [v/s for v in x]           # l1-normalized rational proxy (q* normalization adds an algebraic factor; irrelevant here)
    l = random.randint(2, 5)
    d, tb, dmax = gm_delta(y, l)
    assert d is not None and dmax/2 <= d <= dmax
    worst_ratio = max(worst_ratio, float(tb/dmax))
print("1. (GM): 60 random rational targets: admissible max exists, is rational; max excluded length/delta_max =", round(worst_ratio, 4), "(bound 1/8)")

# ---------- 2. K_kappa identity ----------
mp.mp.dps = 50
maxerr = 0
for trial in range(200):
    sigma = mp.mpf(10)**(-random.uniform(0, 8))
    R2 = mp.mpf(random.uniform(0, 0.999999))
    k = (sigma + mp.sqrt(sigma**2*R2 + sigma*(1-R2)))/(1-R2)
    a = k - sigma
    lhs = 1 - R2
    rhs = sigma*(1 + 2*a + sigma)/(a + sigma)**2
    maxerr = max(maxerr, abs(lhs - rhs)/lhs)
    assert a > 0 and abs(a**2 - (sigma + k**2*R2)) < mp.mpf(10)**(-40)*max(1, a**2)
print("2. 1 - R^2 = sigma(1+2a+sigma)/(a+sigma)^2: max rel err", mp.nstr(maxerr, 3), "; hence R^2 <= 1 - sigma when a + sigma <= 1")

# ---------- 3. cluster capacity ----------
worst = 1.0
for trial in range(200):
    L = random.randint(2, 40); Rcl = random.randint(1, 60)
    ccl = 1.0
    prev = ccl*4  # c_L >= 4 c^cl since c^cl <= c_L/4
    cs = []
    for i in range(1, Rcl+1):
        cmax = min(ccl*4**(1-i), prev/4)
        c = (1 - 2.0**(-(L+i)))*cmax    # worst generic choice (lower end)
        cs.append(c); prev = c
        worst = min(worst, c/(ccl*4**(1-i)))
print("3. cluster: min over trials of c_{L+i}/(c^cl 4^{1-i}) =", round(worst, 6), "(claim >= 1/2)")

# ---------- 4. absorber R from lb ----------
def R_of(mu2c2):
    R = 1
    while 2.0**(3-R) > mu2c2/4: R += 1
    return R
worstR = 0; worst_entry = 1e9
for trial in range(200):
    p0 = random.randint(11, 30)
    logmu2 = -(2*p0**2 + 2)*math.log(2)
    c = 10**(-random.uniform(1, 30))
    lb = c*random.uniform(1/8, 1)          # lb in [c/8, c] (shown in the report)
    # work in logs to avoid underflow: R = least R >= 1 with (3-R) log2 <= log(mu^2 lb^2/4)
    tgt_lb = (logmu2 + 2*math.log(lb) - math.log(4))/math.log(2)
    tgt_c = (logmu2 + 2*math.log(c) - math.log(4))/math.log(2)
    R_lb = max(1, math.ceil(3 - tgt_lb)); R_c = max(1, math.ceil(3 - tgt_c))
    worstR = max(worstR, R_lb - R_c)
    # least entry eta = 4*2^{-R}/q*(x) with q*(x) <= 8; compare with mu^2 c^2: log2(eta) - log2(mu^2 c^2)
    log2eta = 2 - R_lb - 3
    worst_entry = min(worst_entry, log2eta - (logmu2 + 2*math.log(c))/math.log(2))
print("4. absorber: R(lb) - R(c) <= ", worstR, "; min log2(eta_k/(mu^2 c^2)) =", round(worst_entry, 3), "(claim >= -13)")
