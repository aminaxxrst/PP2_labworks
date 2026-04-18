def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
#fibonacci(6) + fibonacci(5)
#fibonacci(5) + fibonacci(4) + fibonacci(4) + fibonacci(3)
#fibonacci(4) + fibonacci(3) + fibonacci(3) + fibonacci(2) + fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
#fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1) + fibonacci(2) + fibonacci(1) + fibonacci(1) + fibonacci(0) + fibonacci(2) + fibonacci(1) + fibonacci(1) + fibonacci(0) + fibonacci(1) + fibonacci(0) + 1
#fibonacci(2) + fibonacci(1) + fibonacci(1) + fibonacci(0) + fibonacci(1) + fibonacci(0) + 1 + fibonacci(1)+ fibonacci(0) + 1 + 1 + 0 + fibonacci(1) + fibonacci(0) + 1 + 1 + 0 + 1 + 0 + 1
#fibonacci(1) + fibonacci(0) + 1 + 1 + 0 + 1 + 0 + 7 + 1 + 0 + 1 + 0
# 1 + 0 + 12
# 13
# 0 1 1 2 3 5 8 13