def max_dist(li):
    if len(li)==0:
        return 0
    maximum = max(li)
    minimum = min(li)
    return maximum-minimum


assert max_dist([1,2,3]) == 2 , "Error cas 1"
assert max_dist([1,2,3,2.5]) == 2 , "Error cas 2"
assert max_dist([1,5,2]) == 4 , "Error cas 3"
assert max_dist([]) == 0 , "Error cas 4"