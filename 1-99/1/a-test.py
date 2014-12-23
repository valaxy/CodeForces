from a import solve

# test
assert (solve(6, 6, 4) == 4)

# small flagstone
assert (solve(1, 1, 1) == 1)

# big flagstone
assert (solve(10, 10, 100) == 1)

print('ok')