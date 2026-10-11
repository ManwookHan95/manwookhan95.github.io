"""Sanity check of Prop 1.5(a) of N1: if T=(f, rho g) with ||(f,g)|| <= 1, p*(f)=1, and S is an operator with
||S - T|| < delta attaining its norm at x_S, then the norming direction y = S x_S/||S x_S|| = (cos phi, sin phi)
(cos phi >= 0) satisfies |sin phi| <= 2 sqrt(delta/(1-rho^2)).
Finite-dimensional model: X = R^3 with p = l_4 norm (smooth); operators into l_2^2 are pairs of functionals.
||(f,g)|| = max_{p(x)<=1} sqrt(f(x)^2+g(x)^2), computed by dense sampling of the unit sphere of p plus local refinement.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(1)
q = 4.0
def p(x):
    return np.sum(np.abs(x) ** q, axis=-1) ** (1 / q)
def grad_p(x):
    n = p(x)
    return np.sign(x) * np.abs(x) ** (q - 1) / n ** (q - 1)

# dense sample of S_p
Z = rng.normal(size=(200000, 3)); Z /= p(Z)[:, None]

def opnorm(F, G):
    vals = (Z @ F) ** 2 + (Z @ G) ** 2
    i = np.argmax(vals)
    x0 = Z[i]
    # local refinement on the sphere
    obj = lambda x: -(((x @ F) ** 2 + (x @ G) ** 2) / p(x) ** 2)
    res = minimize(obj, x0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 4000})
    x = res.x / p(res.x)
    return np.sqrt(-res.fun), x

def find_mate(f, xn):
    # a mate g of f: g(xn)=0 and ||(f,g)||<=1; take g along a random direction killed at xn, scaled down until contractive
    v = rng.normal(size=3); v -= (v @ xn) / (f @ xn) * f * 0  # placeholder
    # choose g orthogonal (as functional) to xn: g(xn) = 0
    g = rng.normal(size=3); g -= (g @ xn) / (xn @ xn) * xn
    lo, hi = 0.0, 5.0
    for _ in range(40):
        mid = (lo + hi) / 2
        n, _ = opnorm(f, mid * g)
        if n <= 1 + 1e-10: lo = mid
        else: hi = mid
    return lo * g

worst = 0.0
for trial in range(30):
    xn = rng.normal(size=3); xn /= p(xn)
    f = grad_p(xn)                # p*(f) = 1, attained at xn
    g = find_mate(f, xn)          # g in C(f) (numerically)
    rho = rng.uniform(0.3, 0.95)
    delta = 10 ** rng.uniform(-4, -1.5)
    E = rng.normal(size=(2, 3)); E /= max(opnorm(E[0], E[1])[0], 1e-12); E *= 0.999 * delta
    F, G = f + E[0], rho * g + E[1]
    nS, xS = opnorm(F, G)
    y = np.array([F @ xS, G @ xS]); y /= np.linalg.norm(y)
    if y[0] < 0: y = -y
    bound = 2 * np.sqrt(delta / (1 - rho ** 2))
    ratio = abs(y[1]) / bound
    worst = max(worst, ratio)
    if trial < 8:
        print(f"rho={rho:.3f} delta={delta:.2e} |sin phi|={abs(y[1]):.3e} bound={bound:.3e} ratio={ratio:.3f}")
print("max ratio |sin phi|/bound over trials:", round(worst, 4), "(must be <= 1)")
