"""Q1 sanity check of Lemma S2c^tr (log2 scale).  T = T_lo(w) = 2^{-n'}, n' >= n(w) >= Design(L).  Worst case Design = n'.
gap_min >= T^{5 Design + 2}, x_0 >= T^{5 Design + 3}; window constants K_w <= (n A_0/T)^{C} gap_min^{-C} x_0^{-C} Design^{C}
(C absolute, A_0 = f-constant); s_late = (T gap_min x_0/(n A_0 K_w))^{C}; violation mass eps <= C_f T^{-1} log2(1/T) exp(-1/T)
(W_exp).  Report the least n' from which 64 rho eps/delta <= s_late and exp(-1/(2T)) <= s_late hold, for several absolute C and f-constants."""
import math
def log2_terms(n, C, A0, Cf, rho_delta):
    lT = -n                                   # log2 T
    D = n                                     # worst case Design(L) = n(w)
    lgap = (5*D + 2)*lT
    lx0 = (5*D + 3)*lT
    lKw = C*(math.log2(n) + math.log2(A0) - lT) - C*lgap - C*lx0 + C*math.log2(D)
    lslate = C*(lT + lgap + lx0 - math.log2(n) - math.log2(A0) - lKw)
    leps = math.log2(Cf) - lT + math.log2(n) - (2.0**n)*math.log2(math.e)   # exp(-1/T) = 2^{-2^n log2 e}
    lhs1 = math.log2(64*rho_delta) + leps
    lhs2 = -(2.0**(n - 1))*math.log2(math.e)
    return lhs1, lhs2, lslate
for C in (3, 10, 30):
    for A0, Cf, rd in ((10.0, 1e3, 1e2), (1e6, 1e12, 1e6)):
        first = None
        for n in range(4, 200):
            l1, l2, ls = log2_terms(n, C, A0, Cf, rd)
            if l1 <= ls and l2 <= ls:
                if first is None: first = n
            else:
                first = None
        l1, l2, ls = log2_terms(60, C, A0, Cf, rd)
        print('C=%2d A0=%.0e Cf=%.0e rho/delta=%.0e : comparison holds for all n >= %s ; at n=60: log2 s_late = %.3e, log2(64 rho eps/delta) = %.3e'
              % (C, A0, Cf, rd, first, ls, l1))
