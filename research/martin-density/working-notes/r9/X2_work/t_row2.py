import numpy as np, sys
sys.path.insert(0, '.')
from xmodel import Model
from scipy.optimize import brentq
def rho_of(c1, c3=0.3, k=1):
    M = Model(tg=[(1.0,0.2), (1.0,c1), (0.5,1.0), (-1.0,c3)])
    D = M.forced(M.a0, M.z0)
    return D['nuk'][k]/D['theta']*np.sign(D['val'][k]*M.sig[k]), M, D
for c1 in np.linspace(-1.0, 0.0, 11):
    r, M, D = rho_of(c1)
    print('c1 %.2f  signed rho_1 %.4f  val %s' % (c1, r, np.round(D['val'],4)))
