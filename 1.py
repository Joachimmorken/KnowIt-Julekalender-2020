nums = [int(num) for num in open('1.in').read().split(',')]
n = len(nums)
sum_100k = (n + 1) * (n + 2)/2
sum_nums = sum(nums)
print(sum_100k - sum_nums)
