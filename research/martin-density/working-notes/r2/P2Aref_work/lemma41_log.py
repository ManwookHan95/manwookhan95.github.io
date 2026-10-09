# Referee check of P2 Lemma 4.1 "deep replication": sum_{Phi<theta} lambda_k <= 2 m theta fails for admissible Phi.
# Phi_m(k) = 2^{-m-j^2} on blocks k in [j^2-j, j^2) (j >= 2), else 2^{-m-k}; Phi_m(k) <= 2^{-m-k} holds (admissible rescaling of T).
from fractions import Fraction
m = 1; KMAX = 500
Phi = {}
for k in range(1, KMAX):
    Phi[k] = Fraction(1, 2**(m+k))
j = 2
while j*j < KMAX:
    for k in range(j*j - j, j*j):
        if k >= 1: Phi[k] = Fraction(1, 2**(m + j*j))
    j += 1
for j in range(3, 20):
    theta = Fraction(101, 100) / 2**(m + j*j)
    S = sum(p for p in Phi.values() if p < theta)
    print("j=%2d  log2(1/theta)=%6.1f   sum_{Phi<theta} Phi / theta = %.3f" % (j, m + j*j - 0.0144, float(S/theta)))
