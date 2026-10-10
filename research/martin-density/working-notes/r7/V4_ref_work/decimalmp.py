"""Tiny mpmath-like shim over decimal.Decimal (mpmath is not installed)."""
import decimal
from decimal import Decimal
class _MP:
    def __init__(self):
        self._dps = 50
    @property
    def dps(self): return self._dps
    @dps.setter
    def dps(self, v):
        self._dps = v; decimal.getcontext().prec = v
mp = _MP()
def mpf(x):
    if isinstance(x, float): return Decimal(repr(x))
    return Decimal(x)
def sqrt(x): return Decimal(x).sqrt()
def sign(x):
    x = Decimal(x)
    return Decimal(1) if x > 0 else (Decimal(-1) if x < 0 else Decimal(0))
def nstr(x, k):
    return format(float(x), '.%dg' % k) if abs(Decimal(x)) > Decimal('1e-300') or x == 0 else '%.*E' % (k-1, Decimal(x))
