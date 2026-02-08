def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list)) #9
#max_of_rest=find_max([7,2,9,1])
#max_of_rest=find_max([2,9,1])
#max_of_rest=find_max([9,1])
#max_of_rest=find_max([1])=1

#compare 1 with 9, numbers=[9,1], max_of_rest=9
#compare 9 with 2, numbers=[2,9,1], max_of_rest=9
#compare 9 with 7, numbers=[7,2,9,1], max_of_rest=9
#compare 9 with 3, numbers=[3,7,2,9,1], max_of_rest=9