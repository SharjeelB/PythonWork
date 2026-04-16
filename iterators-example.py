def get_numbers():
    return [1, 2, 3, 4, 5]

nums = get_numbers()
#for n in nums:
   # print(n)
    #print("character at position 3 is : " + str(n))


numbers = [10, 20, 30,40]

it = iter(numbers)


print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

next(it)


#Dictionary example

data = {"name": "John", "age": 30}

it = iter(data)

print(next(it))  # name
print(next(it))  # age


it = iter(data.values())
print(next(it))