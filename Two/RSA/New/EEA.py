def myEEA(a,b):
    """Solves gcd(a,b) = ax+by using the 
    Extended Euclidean Algorithm
    
    Input:
        a (int) : first number
        b (int) : second number
        
    Returns:
        gcd (int) : gcd(a,b)
        x (int): x such that gcd(a,b) = ax+by
        y (int): y such that gcd(a,b) = ax+by
    """
    r,last_r = b,a
    x,last_x = 0,1
    y,last_y = 1,0
    while r != 0:
        q = last_r // r
        last_r, r = r, last_r%r
        last_x, x = x, (last_x - q*x)
        last_y, y = y, (last_y - q*y)
    gcd = last_r
    x = last_x
    y = last_y
    return gcd, x, y
