# Independent test of Lemma R+ (S3 3.2): N(y) <= 1 + X/(2(C+2g)), X <= 4||D(w'-w)||^2 + 4 sum_A Phi^2, for random/adversarial blocks
import numpy as np
rng = np.random.default_rng(123)
def normalize(v, Phi):
    # scale so that ||v||_inf + ||Phi v|| = 1
    return v / (np.max(np.abs(v)) + np.linalg.norm(Phi * v))
worst = -1; worstX = -1; cnt = 0; cntpos = 0
for trial in range(20000):
    n = rng.integers(5, 40)
    Phi = 0.5 ** rng.uniform(1, 12, size=n) * rng.uniform(0.2, 1, size=n)
    # w: many peaks at +-1, some non-peaks
    s = rng.choice([-1., 1.], size=n)
    w = s * np.where(rng.random(n) < 0.6, 1.0, rng.uniform(0, 1, size=n))
    w = normalize(w, Phi)
    # w': perturb w (small or large), flip some peaks, create new peaks
    pert = rng.choice([1e-4, 1e-3, 1e-2, 1e-1, 0.5])
    wp = w + pert * rng.normal(size=n)
    flip = rng.random(n) < 0.1
    wp[flip] = -wp[flip]
    newp = rng.random(n) < 0.1
    wp[newp] = np.sign(wp[newp] + 1e-12) * np.max(np.abs(wp)) * 1.0
    wp = normalize(wp, Phi)
    M, C = np.max(np.abs(w)), np.linalg.norm(Phi * w)
    Mp, Cp = np.max(np.abs(wp)), np.linalg.norm(Phi * wp)
    g = Cp - C
    if abs(g) > C / 4: continue
    cnt += 1; cntpos += (g > 0)
    tol = 1e-12
    P = np.abs(np.abs(w) - M) < tol; Pp = np.abs(np.abs(wp) - Mp) < tol
    S1 = P & Pp & (np.sign(w) == np.sign(wp))
    S2 = (~P) & (~Pp) & (np.abs(2 * wp - w) <= Mp - abs(g))
    A = ~(S1 | S2)
    gp = max(g, 0.0)
    y = np.where(S1 | S2, 2 * wp - w, (1 - gp / Mp) * wp)
    Ny = np.max(np.abs(y)) + np.linalg.norm(Phi * y)
    Y = y - wp
    RA = np.dot(Phi * wp, Phi * (wp - w) * A) + (gp / Mp) * np.sum((Phi * wp * A) ** 2)
    X = np.sum((Phi * (wp - w)) ** 2) + np.sum((Phi * Y) ** 2) + 2 * abs(RA)
    bound = 1 + X / (2 * (C + 2 * g))
    worst = max(worst, Ny - bound)
    Xb = 4 * np.sum((Phi * (wp - w)) ** 2) + 4 * np.sum(Phi[A] ** 2)
    worstX = max(worstX, X - Xb)
print('cases', cnt, 'with C\'>C', cntpos, 'max N(y)-bound', worst, 'max X - Xbound', worstX)
