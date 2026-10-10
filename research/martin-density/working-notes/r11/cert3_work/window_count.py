"""cert3: log_B-scale arithmetic of the class/cube window count (Section 5 of cert3_report.md).  Exponents of B = 4 Design/u.
E_A(L,N)  = 2 + 2N(2C+3) + Cs(2L+2) + CK + 4         (fix A: support-first pigeonhole; Section 5.3)
E_orig(p) = 2[1 + (2C+1)p] + Cs(2L+2) + CK + 4        (Q1/U1 count with exponent p)
available: omega(L)+20 with the proven lower bound omega(L) >= 2^L - 1, or omega(L)+L^2+20 (refa I2).
For E_orig only the trivial bound omega >= p is available; we show the margin needed would be (4C+1)p, i.e. NOT implied."""
for C, Cs, CK in [(3, 3, 3), (10, 10, 10)]:
    print(f"# constants C={C} C_*={Cs} C_K={CK}")
    for N in [1, 3, 10]:
        Lmin = None
        for L in range(1, 40):
            if L < N:   # P7: N <= L for L >= l_f
                continue
            EA = 2 + 2 * N * (2 * C + 3) + Cs * (2 * L + 2) + CK + 4
            if 2 ** L - 1 + 20 >= EA + 1 and Lmin is None:
                Lmin = L
        print(f"N={N}: fix A with omega>=2^L-1 works for all L >= {Lmin} (exponent E_A(L) = O(L)); with +L^2 in the exponent: "
              f"{min(L for L in range(max(1,N),60) if L*L + 19 >= 2 + 2*N*(2*C+3) + Cs*(2*L+2) + CK + 4 + 1)}")
    for p in [10, 100, 1000]:
        need = 2 * (1 + (2 * C + 1) * p)
        print(f"  original count, p={p}: cube part alone needs exponent {need} = {need/p:.1f} p; omega >= p gives only p")
