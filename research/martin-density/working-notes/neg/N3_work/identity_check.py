import numpy as np
rng = np.random.default_rng(0)
# |B| - zB = (1-|z|)|B| + 2 (zB)_-   for |z|<=1
B = rng.normal(size=100000); z = rng.uniform(-1,1,size=100000)
lhs = np.abs(B) - z*B
rhs = (1-np.abs(z))*np.abs(B) + 2*np.maximum(-(z*B),0)
print("identity1 max err", np.max(np.abs(lhs-rhs)))
# |B| + zB = (1-|z|)|B| + 2 (zB)_+
lhs2 = np.abs(B) + z*B
rhs2 = (1-np.abs(z))*np.abs(B) + 2*np.maximum(z*B,0)
print("identity2 max err", np.max(np.abs(lhs2-rhs2)))
# |x+y| = |x| + sgn(x) y + 2(-sgn(x) y - |x|)_+
x = rng.normal(size=100000); y = rng.normal(size=100000)*3
lhs3 = np.abs(x+y); rhs3 = np.abs(x)+np.sign(x)*y+2*np.maximum(-np.sign(x)*y-np.abs(x),0)
print("identity3 max err", np.max(np.abs(lhs3-rhs3)))
# (x)_- <= (x+c)_- + c for c>=0
c = np.abs(rng.normal(size=100000))
print("ineq4 violations", np.sum(np.maximum(-x,0) > np.maximum(-(x+c),0)+c+1e-12))
# (x-y)_- <= x_- + y_+
print("ineq5 violations", np.sum(np.maximum(-(x-y),0) > np.maximum(-x,0)+np.maximum(y,0)+1e-12))
