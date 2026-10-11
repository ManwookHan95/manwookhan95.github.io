import mpmath as mp, random
exec(open('frozen_check.py').read().split("m = 2\n")[0])
m=2; b=mp.mpf('1e-3'); u=mp.mpf('0.1'); mu=mp.mpf('0.02'); fine={8,9,10}; Pf={0,1}
zeta, Phi, rho = make_block(m,b,u)
th, A, nu = true_block(zeta, Phi)
print('theta', th, 'rho', [mp.nstr(x,5) for x in rho])
SPf = sum(abs(zeta[k]) for k in Pf) + sum(abs(zeta[k]) for k in fine)
SQf = sum(nu[k]**2*Phi[k]**2 for k in range(8) if k not in Pf)
print('Psi_f(0+)', SPf**2 - SQf, 'A', A, 'sum_Pf|zeta|', SPf, 'SQf', SQf)
z2 = list(zeta)
for it in range(8):
    thf2, Af2, nu2 = frozen_block(z2, Phi, Pf, fine)
    print(it, 'thf', mp.nstr(thf2,12), 'Af', mp.nstr(Af2,8), 'rho weak', mp.nstr(nu2[2]/thf2,8), mp.nstr(nu2[3]/thf2,8))
    for k in (2,3):
        z2[k] = mp.sign(z2[k])*(1-mu/2)*thf2*Phi[k]**2
