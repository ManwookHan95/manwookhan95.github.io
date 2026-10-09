import numpy as np
rng=np.random.default_rng(0)
T=1.0; J=32
def bottom_up(c,Ts):
    D=[0.0]
    for t in Ts: D.append((t-D[-1])/c)
    return np.max(np.abs(D))
def top_down(c,Ts):
    D=[0.0]
    for t in Ts[::-1]: D.append(t-c*D[-1])
    return np.max(np.abs(D))
for c in (0.3,0.7,0.9,1.0,1.5,3.0):
    worst_bu=max(bottom_up(c,rng.uniform(0.5*T,T,J)) for _ in range(2000))
    worst_td=max(top_down(c,rng.uniform(0.5*T,T,J)) for _ in range(2000))
    alt=bottom_up(c,[T*(-1)**i for i in range(J)])
    print(f"c={c}: one-type random targets in [T/2,T]: bottom-up max|move|={worst_bu:.3g}, top-down max|move|={worst_td:.3g} (T/(1-c)={'inf' if c>=1 else round(T/(1-c),3)}); alternating types bottom-up={alt:.3g}")
