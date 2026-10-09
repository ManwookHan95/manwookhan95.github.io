import numpy as np, warnings
warnings.filterwarnings('ignore')
from model import build_f
from model2 import make_model2
from normers import normer_face
M = build_f(make_model2())
P = normer_face(M, nobj=60, seed=3)
D = np.vstack([P - M['xi'], M['xi'][None,:]])
u, s, vt = np.linalg.svd(D)
print('sv', np.round(s, 7))
rank = (s > 1e-5*s[0]).sum()
G = vt[rank:]          # orthonormal basis of admissible mate directions (annihilate all normers)
print('rank', rank, 'mate-space dim', G.shape[0])
np.save('Gbasis.npy', G)
# how do these directions look relative to u_k and a?
for i, g in enumerate(G):
    print(i, np.round(g, 3))
