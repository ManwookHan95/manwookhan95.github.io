"""
cert0 / finding F1: V1 Lemma TU bank equations with a KN-1 hold carrier (EXACT model of Lemma TU Step 2).

Lemma B (3.1), exact for any diagonal base: after the pulls (row A^p, nu_p = ||U^*A^p||, e^p), banks m_l >= 0 at j'_l (u_l(j'_l) = v'_l,
s'_l := mu_{j'_l}), the value of carrier l is
     val_l(m) - val^p_l = (nu_p beta_l + m_l s'_l^2 v'_l)/N(m) - beta_l,   N(m) = sqrt(nu_p^2 + sum_k m_k^2 s'_k^2),
     beta_l = eps_l <U^*u_l, e^p>  (any sign, |beta_l| <= ||U|| ||u_l||_1).
Required increment Delta_l := x_l + (val^(2)_l - val^p_l) = x_l + 2 v_l(j_l) + (pull Hilbert terms) > 0.
Solution: m_l(y) = (Delta_l y + beta_l (y - nu_p))/(s'^2 v'), y = N solves y = Phi(y) := sqrt(nu_p^2 + sum s'^2 m_l(y)^2).
A bank must be NONNEGATIVE (mass with the sign eps of the contact).  m_h < 0 iff Delta_h N < -beta_h (N - nu_p).

We compare
  (A) Q1 2.2's per-carrier rule read literally: hold pull with v_h(j_p) = max(|x_h|, c), c = c_{L+1} (tiny), active pulls in window [eta, 2^G eta];
  (B) the fix: common window eta_* = max(|x|_inf, c) for every tuned carrier (V1 Lemma TU verbatim with eta := eta_*).
Regime: s'^2 v' fixed design numbers, eta -> 0 (as in the design: eta <= c_T ~ Design^{-3} while s'^2 v' >= Design^{-1/6}).
"""
import mpmath as mp
mp.mp.dps = 50

def solve_banks(Delta, beta, sv, s2, nu_p):
    # fixed point y = Phi(y) on [nu_p, inf) by bisection on Phi(y) - y (Phi is a contraction near nu_p in the regime of Lemma TU)
    def m_of(y):
        return [(D * y + b * (y - nu_p)) / q for D, b, q in zip(Delta, beta, sv)]
    def G(y):
        ms = m_of(y)
        return mp.sqrt(nu_p ** 2 + sum(s * m ** 2 for s, m in zip(s2, ms))) - y
    # Lemma TU Step 2: the fixed point lies in I = [nu_p, nu_p + kappa], kappa = 2(Phi(nu_p) - nu_p), where Phi is a contraction
    lo = mp.mpf(nu_p)
    hi = nu_p + 2 * G(lo) + mp.mpf(10) ** (-mp.mp.dps + 5)
    if G(hi) > 0:
        raise RuntimeError("outside the contraction regime of Lemma TU")
    for _ in range(300):
        mid = (lo + hi) / 2
        if G(mid) > 0:
            lo = mid
        else:
            hi = mid
    y = (lo + hi) / 2
    return y, m_of(y)

def scenario(eta, c, x_hold, K=4, beta_hold=-0.15, common=False):
    nu_p = mp.mpf('0.5')
    # active carriers: corrections x_l = +-eta, pulls at v = eta (window [eta, 2^G eta], lower end), so Delta = x + 2v in [eta, 3 eta]
    Delta, beta, sv, s2 = [], [], [], []
    for i in range(K):
        x = eta * (1 if i % 2 == 0 else -1)
        v = eta
        Delta.append(x + 2 * v)
        beta.append(mp.mpf('0.1') * (1 if i % 3 else -1))
        s2.append(mp.mpf('1e-2'))          # s'^2 = mu_{j'}^2
        sv.append(mp.mpf('1e-2') * mp.mpf('5e-2'))   # s'^2 v'
    # hold carrier
    v_h = eta if common else max(abs(x_hold), c)
    Delta.append(x_hold + 2 * v_h)
    beta.append(mp.mpf(beta_hold))
    s2.append(mp.mpf('1e-2')); sv.append(mp.mpf('1e-2') * mp.mpf('5e-2'))
    y, ms = solve_banks(Delta, beta, sv, s2, nu_p)
    # verify the exact equations
    N = mp.sqrt(nu_p ** 2 + sum(s * m ** 2 for s, m in zip(s2, ms)))
    res = max(abs((nu_p * b + m * q) / N - b - D) for b, m, q, D in zip(beta, ms, sv, Delta))
    thr = -beta_hold * (N - nu_p) / N
    return ms[-1], N - nu_p, thr, Delta[-1], res

if __name__ == "__main__":
    print("columns: eta, c=c_{L+1}, rule, Delta_hold, threshold -beta_h(N-nu_p)/N, N-nu_p, hold bank m_h, residual of exact equations")
    for eta in [mp.mpf('1e-6'), mp.mpf('1e-8'), mp.mpf('1e-10')]:
        c = eta ** 3          # c_{L+1} <= b^2 << eta'^2 (any c << eta^2 shows the effect)
        for common in (False, True):
            mh, dN, thr, Dh, res = scenario(eta, c, x_hold=c / 10, common=common)
            rule = "B common eta_*" if common else "A max(|x_h|,c)"
            print(f"eta={mp.nstr(eta,2):>6} c={mp.nstr(c,2):>6} {rule:15s} Delta_h={mp.nstr(Dh,3):>9} thr={mp.nstr(thr,3):>9} "
                  f"N-nu_p={mp.nstr(dN,3):>9} m_h={mp.nstr(mh,4):>11} res={mp.nstr(res,2)}  {'NEGATIVE bank' if mh < 0 else 'ok'}")
    print("\nsame with beta_hold = +0.15 (rule A):")
    for eta in [mp.mpf('1e-6'), mp.mpf('1e-8')]:
        c = eta ** 3
        mh, dN, thr, Dh, res = scenario(eta, c, x_hold=c / 10, beta_hold=+0.15, common=False)
        print(f"eta={mp.nstr(eta,2)} m_h={mp.nstr(mh,4)} ({'NEGATIVE' if mh < 0 else 'ok'})")
    print("\nscaling of the threshold: thr/eta^2 (should be ~ const = |beta| * sum_k (2..3)^2 * s'^2 nu_p/(s'^2 v')^2 / (2 nu_p^2))")
    for eta in [mp.mpf('1e-6'), mp.mpf('1e-8'), mp.mpf('1e-10'), mp.mpf('1e-12')]:
        mh, dN, thr, Dh, res = scenario(eta, eta ** 3, x_hold=eta ** 4, common=True)
        print(f"eta={mp.nstr(eta,2):>6}  thr/eta^2={mp.nstr(thr / eta ** 2, 6)}   m_h/eta={mp.nstr(mh / eta, 6)}")
