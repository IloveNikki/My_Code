for value in range(1,2):
    print(value)
numbers=list(range(1,101))
for number in numbers:
    print(number)


nums=list(range(1,20,2))
for num in nums:
  print(num)




nums=list(range(3,31,3))
squares=[]
for num in nums:
    squares.append(num/3)
print(squares)
print(squares[:3])
print("The first three items in the list are:")
for square in squares[:3]:
    print(square)


print(squares[-3:])
print("The last three items in the list are:")
for square in squares[-3:]:
    print(square)

squares=[]
for num in range(1,11):
    squares.append(num**3)
print(squares)



