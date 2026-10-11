import numpy as np
import selfpin as S
from model import Row, qstar
for phl in [0.3, 0.45, 0.6]:
  for phc in [0.02, 0.05]:
    for phf in [0.1, 0.3]:
        def build(r_mass, r_type, a_r=0.0, Phi=np.array([phl, phl, phc, phf])):
            row = S.build(r_mass, r_type, a_r)
            return Row(row.a, row.z, row.U, Phi, row.mu)
        row = build(0.675, 'contact')
        print(phl, phc, phf, 'peaks', row.peaks(), 'w', row.w.round(4), 'sigma', round(row.sigma,4))
