# subtract.py
def subtract(a,b):
	# pad 'b' with 0s
	diff = len(a)-len(b)
	b = [0]*diff + b
	
	answer = []
	for i in xrange(1,len(a)+1):
		if a[-i] < b[-i]:
			"""Borrow. In the case that we are borrowing from a zero, 
			the entry will become -1. When the algorithm hits that
			entry, it will be handled on the next loop when we add 10.
			""" 
			a[-(i+1)] -= 1
			a[-i] += 10
		answer = [a[-i] - b[-i]] + answer
	return answer

