import sys
sys.argv = ['x']
exec(open('k1_check.py').read().split('if __name__')[0])
random.seed(11)
for t in range(8):
    Phi, zeta = random_block()
    th, A, M, C, nu = solve_block(Phi, zeta)
    rho = [n / th for n in nu]
    P = [k for k in range(len(Phi)) if rho[k] >= 1]
    Q = [k for k in range(len(Phi)) if rho[k] < 1]
    # identities E1, E2
    E1 = mp.fsum(Phi[k]**2*(nu[k]-th) for k in P) - A
    E2 = th**2*mp.fsum(Phi[k]**2 for k in P) + mp.fsum(nu[k]**2*Phi[k]**2 for k in Q) - A**2
    print(t, 'np', len(P), 'theta-AM/C', mp.nstr(th - A*M/C, 3), 'E1', mp.nstr(E1, 3), 'E2', mp.nstr(E2, 3))
