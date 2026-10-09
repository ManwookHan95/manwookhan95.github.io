import numpy as np, cvxpy as cp
from model import qstar, Nblk, blocknorm_and_normer, pstar, build_f

def make_model2(seed=1, delta=0.05, Unorm=0.1, resonant=True, Phibase=0.5):
    rng = np.random.default_rng(seed)
    n = 16
    U = rng.standard_normal((n, n)); U *= Unorm/np.linalg.norm(U, 2)
    a = np.zeros(n); a[0], a[1] = 0.6, -0.3
    nu = np.linalg.norm(U.T @ a); a = a/(np.abs(a).sum() + nu)
    z = np.zeros(n)
    z[0], z[1], z[2], z[3] = 1.0, -1.0, 1.0, 0.97          # F = {0,1}, contact 2, near-contact 3
    z[10:16] = [0.3, -0.2, 0.1, 0.25, -0.3, 0.15]           # signature coordinates (room)
    K = 6
    sig = [10+k for k in range(K)]
    Y = np.zeros((K, n))
    Y[0, 2] = 1.0                       # ~ contact e_2*  (peak)
    Y[1, 4] = 0.5; Y[1, 5] = -0.5       # ~ 0 on zhat     (non-peak)
    Y[2, 3] = 1.0; Y[2, 10] = 0.2       # ~ near-contact, touches coarser signature 10 (peak)
    Y[3, 6] = 1.0; Y[3, 11] = -0.3      # non-peak candidate
    Y[4, 2] = -0.6; Y[4, 7] = 0.4       # negative peak
    Y[5, 8] = 0.7; Y[5, 9] = -0.7; Y[5, 12] = 0.1
    u = np.zeros((K, n))
    for k in range(K):
        v = Y[k].copy(); v[sig[k]] += delta
        u[k] = v/(np.abs(v).sum() + np.linalg.norm(U.T @ v))
    Phi = Phibase**(np.arange(K)+1)
    return dict(n=n, U=U, a=a, z=z, K=K, sig=sig, u=u, Phi=Phi, lam=Phi.copy(), delta=delta, F=[0,1])

if __name__ == '__main__':
    M = build_f(make_model2())
    th = M['Mw']*M['sigma']/M['C']
    print('q0', M['q0'], 'M', M['Mw'], 'C', M['C'])
    print('w', np.round(M['w'], 5))
    print('u.xi', np.round(M['u']@M['xi'],4))
    print('theta*Phi', np.round(th*M['Phi'],4))
    print('p*(f)', pstar(M, M['f']))
