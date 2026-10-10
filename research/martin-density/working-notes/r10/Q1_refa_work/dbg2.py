import mpmath as mp, random, traceback
src=open('pm_ref.py').read()
src=src.replace("    t = tofM(M, nu, Phi)\n    A = mp.fsum", "    t = tofM(M, nu, Phi)\n    if t is None:\n        print('NONE at M', mp.nstr(M,30), 'thr', mp.nstr(1/(1+mp.sqrt(mp.fsum(p**2 for p in Phi))),30)); print('nu',[mp.nstr(x,6) for x in nu]); print('Phi',[mp.nstr(x,4) for x in Phi]); raise SystemExit\n    A = mp.fsum")
src=src.split("print('mu, r, W")[0]
exec(src)
mu, r, W = mp.mpf('1e-6'), mp.mpf('1e-2'), mp.mpf('1e-14')
o = instance(mu, r, W)
print(o)
