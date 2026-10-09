"""Referee check of Y4 N3: is the reported quantity |Delta theta_1|+|Delta theta_2| (absolute) or divided by t?
Re-run Y4's model (imported read-only from ../Y4_work) and print both the objective and objective/t."""
import sys, numpy as np
sys.path.insert(0, '../Y4_work')
from n3_ray import build, ray_module, min_switch
from toy import s_of
for eps_rel in [1.0, 0.01]:
    M, D, l1, l2 = build(eps_rel)
    b = M.blocks[0]; C = D['C'][0]; q = lambda l: b['Phi'][l] * D['w'][0][l] / C
    c = 0.024
    g, om = ray_module(M, D, l1, l2, c)
    ts = np.geomspace(3e-3, 1.0, 12)
    worst = max(max(M.pstar(D['f'] + t * g), M.pstar(D['f'] - t * g)) - s_of(t) for t in ts)
    print(f"eps_rel={eps_rel} D_B={q(l1)+2*q(l2):+.2e} mate defect on grid {worst:+.1e}")
    for t in ts:
        v, st = min_switch(M, D, g, l1, l2, t)
        print(f"   t={t:.3e}  objective={v:.3e}  objective/t={v/t:.3e}  [{st}]")
