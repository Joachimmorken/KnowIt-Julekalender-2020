import sympy as sp

primes = []
nums_set = set(([0, 1]))
nums = [0, 1]

for i in range(2, 1800813):
    j = nums[i - 2] - i
    if j >= 0 and j not in nums_set:
        nums.append(j)
        nums_set.add(j)
        if sp.isprime(j):
            primes.append(j)
    else:
        n = nums[i - 2] + i
        nums.append(n)
        nums_set.add(n)
        if sp.isprime(n):
            primes.append(n)

print(len(primes))
