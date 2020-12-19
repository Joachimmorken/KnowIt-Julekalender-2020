import math
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


ans = 0
for i in range(1, 1000000):
    divisors_sum = sum(list(factors(i)))
    diff = divisors_sum - 2 * i
    ans += 1 if diff > 0 and math.sqrt(diff).is_integer() else 0

print(ans)
