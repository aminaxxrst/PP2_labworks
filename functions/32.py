def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3)) #6
print(my_function(10, 20, 30, 40)) #100
print(my_function(5)) #5