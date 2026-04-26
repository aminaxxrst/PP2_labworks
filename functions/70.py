def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list)) #15
#1+sum_list([2,3,4,5])
#1+2+sum_list([3,4,5])
#1+2+3+sum_list([4,5])
#1+2+3+4+sum_list([5])
#1+2+3+4+5+0
#15