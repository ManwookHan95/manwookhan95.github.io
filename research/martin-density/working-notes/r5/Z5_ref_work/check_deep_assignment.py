# Referee check: elementary inequalities of the cushion-sparse exactification (Theorem S-inf-CS of Z5_ref_notes).
# At a support coordinate j (s = sgn a_j, |a| = |a_j|), scale t, two-sided decomposition values Bp = B_+(j), Bm = B_-(j),
# exact switching value X = X_j. Cushion allowance A = 2|a|/t. f+ = (-s Bp - |a|/t)_+, f- = (s Bm - |a|/t)_+.
# Non-deep (s X >= -2A): common shift sigma in [y - A, x + A] closest to 0, x = s Bp, y = s(Bp - X).
# Deep (s X < -2A): b+ := -s A, b- := b+ - X.
# Claims: (1) |Bp - b+| <= f+ + f- + |dB - X| in both cases, dB = Bp - Bm;
#         (2) (s b+)_- <= A always; (s b-)_+ <= A (non-deep), (s b-)_+ <= |X| (deep);
#         (3) |b+| <= A + |X|, |b-| <= A + 2|X|.
import numpy as np
rng = np.random.default_rng(7)
worst = [0.0]*6; cnt = {"deep":0, "nondeep":0}
for trial in range(400000):
    s = rng.choice([-1.0, 1.0]); aa = 10**rng.uniform(-8, 0); t = 10**rng.uniform(-4, 0)
    X = rng.standard_normal() * 10**rng.uniform(-6, 3)
    Bp = rng.standard_normal() * 10**rng.uniform(-6, 3)
    err = rng.standard_normal() * 10**rng.uniform(-8, 1)
    dB = X + err; Bm = Bp - dB
    A = 2*aa/t
    fp = max(-s*Bp - aa/t, 0.0); fm = max(s*Bm - aa/t, 0.0)
    x = s*Bp; y = s*(Bp - X)
    if s*X >= -2*A:
        cnt["nondeep"] += 1
        lo, hi = y - A, x + A
        sig = 0.0 if lo <= 0 <= hi else (hi if hi < 0 else lo)
        bp = Bp - sig*s
        bm = bp - X
        c2 = max(max(-s*bm, 0), 0)  # placeholder
        viol_m = max(max(s*bm, 0) - A, 0)
    else:
        cnt["deep"] += 1
        bp = -s*A; bm = bp - X
        viol_m = max(max(s*bm, 0) - abs(X), 0)
    lhs1 = abs(Bp - bp); rhs1 = fp + fm + abs(dB - X)
    worst[0] = max(worst[0], (lhs1 - rhs1)/max(1.0, abs(Bp)+abs(X)))
    worst[1] = max(worst[1], (max(-s*bp, 0) - A)/max(1.0, A))
    worst[2] = max(worst[2], viol_m/max(1.0, abs(X)+A))
    worst[3] = max(worst[3], (abs(bp) - A - abs(X))/max(1.0, A+abs(X)))
    worst[4] = max(worst[4], (abs(bm) - A - 2*abs(X))/max(1.0, A+abs(X)))
print("counts:", cnt)
print("max normalized violations (should be <= ~1e-15):", ["%.2e" % w for w in worst[:5]])

# Flip cost of the - data at deep coordinates, model: v_l(j) = 2^-j on S = {j >= 1}, |a_j| = 2^-(1+beta) j,
# bounded switching |X_j| = D v_l(j); flip cost at scale r<0: Fl(r) = sum 2(|r| (s b-)_+ - |a_j|)_+ with (s b-)_+ <= D v + |a|/t.
# Claim: Fl(r) <= 4|r| D m(2 D |r|), m(y) = sum{v_j : |a_j| < y v_j}; and Fl(r)/r^2 -> 0 iff beta < 1.
J = np.arange(1, 300).astype(float)
for beta in [0.5, 0.9, 1.0, 1.5]:
    v = 2.0**(-J); a = 2.0**(-(1+beta)*J); D = 1.0
    out = []
    for t in [1e-2, 1e-4, 1e-6]:
        cflat = 0.05
        for r in [cflat*t, cflat*t/10, cflat*t/100]:
            A = 2*a/t
            deep = D*v > 2*A
            sbm = np.where(deep, D*v - A + 0.0, A) + a/t  # anti-sign part incl. balance term |kappa||a_j| <= |a_j|/t
            Fl = np.sum(2*np.maximum(r*sbm - a, 0))
            mm = np.sum(v[a < 2*D*r*v])
            out.append((t, r, Fl/r**2, Fl <= 4*r*D*mm + 1e-300))
    print("beta=%.1f" % beta, " ".join("t=%.0e r/t=%.0e Fl/r^2=%.2e ok=%s" % (o[0], o[1]/o[0], o[2], o[3]) for o in out[::3]))
