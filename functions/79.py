# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp) #[0, 1, 4, 9, 16]

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp) #<generator object <genexpr> at 0x0000021C93664EE0>
print(list(gen_exp)) #[0, 1, 4, 9, 16]