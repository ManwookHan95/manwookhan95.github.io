import numpy as np
worst = {'a': -1, 'b': -1, 'c': -1}
for rho in np.linspace(0.01, 0.9999, 400):
    eta0 = (1 - rho**2)/(2*rho**2)            # largest eta_0 allowed by rho^2(1+eta0) <= (1+rho^2)/2
    s0 = np.sqrt(1 - rho**2); Q = (1 - rho**2)/12
    s = np.linspace(-s0, s0, 2001)
    S = np.sqrt(1 + s**2)
    worst['a'] = max(worst['a'], np.max(1 + (rho**2*s**2/2)*(1+eta0) + Q*s**2 - S))
    worst['b'] = max(worst['b'], np.max(np.sqrt(1 + rho**2*s**2) + Q*s**2 - S))
    sl = np.concatenate([np.linspace(s0, 10, 3000), np.logspace(1, 6, 500)])
    worst['c'] = max(worst['c'], np.max(np.sqrt(1 + rho**2*sl**2) + (1 - rho**2)*s0*sl/3 - np.sqrt(1 + sl**2)))
print('max violations (should be <= 0):', worst)
# 5.3 slip: sqrt(1+eta0/2) - 1/100 >= 1 needed
for rho in [0.9, 0.95, 0.98, 0.99, 0.999]:
    eta0 = (1 - rho**2)/(2*rho**2)
    print(rho, 'eta0max', round(eta0, 5), 'sqrt(1+eta0/2)-1/100 =', round(np.sqrt(1+eta0/2) - 0.01, 6), '(must be >= 1)')
