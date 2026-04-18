#recursive function must have 2 parts:
#base case- condition that stops the recursion
#recursive case- function calling itself with an argument
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5)) #120
#5*factorial(4)
#5*4*factorial(3)
#5*4*3*factorial(2)
#5*4*3*2*factorial(1)
#5*4*3*2*1=120