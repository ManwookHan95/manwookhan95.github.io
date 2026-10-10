import numpy as np, sys
sys.path.insert(0, '.')
from xmodel import Model
for tg1 in [(1.0,-1.0), (0.3,-0.5), (0.2,-0.4), (0.1, -0.35)]:
    M = Model(tg=[(1.0,0.2), tg1, (0.5,1.0), (-1.0,0.3)])
    D = M.forced(M.a0, M.z0)
    print('tg1', tg1, 'val', np.round(D['val'],5), 'rho', np.round(D["nuk"]/D["theta"],4),
          'w', np.round(D['w'],4), 'C', round(D['C'],4), 'q0', round(D['q0'],4))
