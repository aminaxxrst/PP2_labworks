#yield- what makes a function a generator and instead of return you can write yield
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
#1
#2
#3
#4
#5