from itertools import count


def is_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True


def closest_prime(n):
    if n <= 0:
        return 1
    closest = 0
    for p1 in count(n, step=-1):
        if is_prime(p1) and p1 <= n:
            closest = p1
            break
    return closest


i = 0
n_gifts = 5433000
delivered = 0
while i < n_gifts:
    if "7" in str(i):
        p = closest_prime(i)
        i += p + 1
    else:
        i += 1
        delivered += 1


print(delivered)
