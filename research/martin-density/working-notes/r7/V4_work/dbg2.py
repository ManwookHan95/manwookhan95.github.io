exec(open('degenerate_check2.py').read().split('for pp in')[0])
bad = zsigned(Dv, z)
print("bad coords:", bad[:20], "count", len(bad))
Rw = (lam * w) @ Urows
for j in bad[:8]:
    contrib = [(l, lam[l]*w[l]*Urows[l, j]) for l in range(L) if Urows[l, j] != 0]
    owner = [l for l in range(L) if Urows[l, j] != 0]
    print(j, "z=", z[j], "D=", Dv[j], "in S of", [l for l in range(L) if j in S[l]], "contribs(lam w u):", [(l, f"{x:.3e}") for l, x in contrib], "eps:", [eps[l] for l in owner], "sgn val:", [np.sign(val[l]) for l in owner])
print("eps:", eps)
print("sgn val:", np.sign(val))
print("delta H / n vs |val|:", [(f"{delta[l]*h[l].sum()/n[l]:.3e}", f"{val[l]:.3e}") for l in range(L)])
