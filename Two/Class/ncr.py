from math import factorial

def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)
    
n = 10
print sum([nCr(n,k)*k**2 for k in xrange(1,n+1)])
print n*(n+1)*2**(n-2)
