# Sherman-Morrison structure of single support moves (U2 3.3) and the exact kernel drift (V3 remark to Lemma VP).
# Single move at s in S_k ∩ F changes the coarse values by (mu_s^2/nu)(u_j(s) - gamma_j a_s/nu^2) Delta.
# For one coordinate s_k per tuned carrier k, the L_0 x L_0 Jacobian is D - gamma alpha^T/nu, det = det(D)(1 - sum rho_k gamma_k/nu^2).
import mpmath as mp, random
mp.mp.dps = 80
random.seed(3)
n, K, smax = 30, 4, 6
mu = [mp.mpf(2) ** (-(s + 2) ** 1.3) for s in range(n)]
S = {k: [s for s in range(smax, n) if (s - smax) % K == k] for k in range(K)}
u = []
for k in range(K):
    vec = [mp.mpf(0)] * n
    for s in random.sample(range(smax), 2): vec[s] = mp.mpf(random.uniform(-1, 1)) / 3
    for s in S[k]: vec[s] = mp.mpf(2) ** (-s) * mp.mpf('0.7')
    u.append(vec)
def variable_vals(a):
    nu = mp.sqrt(sum((m * x) ** 2 for m, x in zip(mu, a)))
    return nu, [sum(uk[s] * mu[s] ** 2 * a[s] / nu for s in range(n)) for uk in u]
def jac(a, coords):
    nu, v0 = variable_vals(a)
    J = mp.matrix(K, len(coords)); h = mp.mpf(10) ** -30
    for j, s in enumerate(coords):
        b = list(a); b[s] += h
        _, v1 = variable_vals(b)
        for i in range(K): J[i, j] = (v1[i] - v0[i]) / h
    return nu, J
tuned = [0, 1, 2]
for label, cfac in [('generic a', None), ('a = sum c_k u_k on F (ND\' fails)', [mp.mpf('0.8'), mp.mpf('-1.3'), mp.mpf('0.5')])]:
    if cfac is None:
        a = [mp.mpf(random.uniform(0.3, 1.0)) * (1 if random.random() < 0.6 else -1) for s in range(n)]
    else:
        a = [sum(cfac[i] * u[k][s] for i, k in enumerate(tuned)) for s in range(n)]
        a = [x if x != 0 else mp.mpf('1e-30') for x in a]   # keep every coordinate in F (tiny where the span vanishes)
    coords = [S[k][0] for k in tuned]
    nu, J = jac(a, coords)
    Jt = mp.matrix([[J[i, j] for j in range(len(tuned))] for i in tuned])
    gamma = [sum(mu[s] ** 2 * u[k][s] * a[s] for s in range(n)) for k in range(K)]
    rho = [a[S[k][0]] / u[k][S[k][0]] for k in tuned]
    D = [mu[S[k][0]] ** 2 * u[k][S[k][0]] / nu for k in tuned]
    sm = 1 - sum(rho[i] * gamma[k] for i, k in enumerate(tuned)) / nu ** 2
    pred = sm
    for d in D: pred *= d
    print(label, ': det(J_L0) =', mp.nstr(mp.det(Jt), 8), ' predicted det(D)(1 - sum rho gamma/nu^2) =', mp.nstr(pred, 8),
          ' SM denominator =', mp.nstr(sm, 8))
    # exact kernel drift for the second configuration
    if cfac is not None:
        _, v0 = variable_vals(a)
        b = list(a)
        for s in range(n): b[s] = a[s] * (1 + mp.mpf('0.01') * mp.sin(s))       # a general move on F (signs kept)
        nu1, v1 = variable_vals(b)
        e0 = [mu[s] * a[s] / nu for s in range(n)]; e1 = [mu[s] * b[s] / nu1 for s in range(n)]
        de2 = sum((x - y) ** 2 for x, y in zip(e0, e1))
        lhs = sum(cfac[i] * (v1[k] - v0[k]) for i, k in enumerate(tuned))
        print('   kernel drift sum c (val1 - val0) =', mp.nstr(lhs, 12), '  -kappa nu ||e1 - e0||^2/2 (kappa = 1) =', mp.nstr(-nu * de2 / 2, 12))
