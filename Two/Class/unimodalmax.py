def find_max(l, index):
    if len(l) == 1:
        # maximum found
        return l[0]
    elif l[index-1] - l[index] < 0:
        # if increasing
        return find_max(l[index:], len(l[index:])//2)
    elif l[index-1] - l[index] > 0:
        # if decreasing
        return find_max(l[:index], len(l[:index])//2)
    else:
        print "invalid list"

'''Temporal complexity is O(log n)

Using the Master Theorm,
    a = 1 because we call find_max 1 time per recursive call
    b = 2 because we split our list into 2 pieces per recursive call
    d = 0 because the code that is executed within each recursive call
          is independent of n.
    d = 0 = log_2(1) = log_b(a), so by the Master Theorem, find_max has O(log n).
'''
