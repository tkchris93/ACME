def EEA(a,b):
	s = 0
	t = 1
	old_s = 1
	old_t = 0
	r = b
	old_r = a

	count = 0
	while r != 0:
		quotient = old_r / r
		
		#r, old_r = old_r - quotient * r, r 
		r, old_r = old_r, r % old_r
		s, old_s = old_s - quotient * s, s
		t, old_t = old_t - quotient * t, t
		
		'''
		old_r, r = r, (old_r - quotient * r)
		old_s, s = s, (old_s - quotient * s)
		old_t, t = t, (old_t - quotient * t)
		'''
		count += 1
		print count
		
	while old_s < 0:
		old_s += b 
		old_t -= 1
	print "Bezout coefficients:", old_s, old_t
	print "greatest common divisor:", old_r
	print "quotients by the gcd:", t, s
	
#Extended Euclidean Algorithm provided in previous lab
def EucAlg(e, phi_n):
	a = e
	b = phi_n
	x, lastX = 0, 1
	y, lastY = 1, 0
	while b != 0:
		q = a // b
		a, b = b, a % b
		x, lastX = lastX - q * x, x
		y, lastY = lastY - q * y, y
	while lastX < 0:
		lastX += phi_n
		lastY -= 1
	return lastX, lastY
