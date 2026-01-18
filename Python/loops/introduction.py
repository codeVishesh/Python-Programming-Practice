count = 1
while count <=5:
    print("hello")
    count = count +1

i = 1
while i<=100:
    print(i)
    i = i+1

i = 1
while i<=10:
    print(3*i)
    i = i+1

nums = [1,2,3,4,5,6,7,8,9,100]

index = 0
while index < len(nums):
    print(nums[index])
    index = index +1


nums = [1,2,3,4,5,6,7,8,9,100]
idx = 0
key = 5
while idx < len(nums):
    if(nums[idx] == key):
       print("found at index", idx)
    idx = idx +1

# odd numbers
i = 1
while i<=10:
    if(i%2 == 0):
        i = i+1
        continue
    print(i)
    i = i+1

# even numbers
i = 1
while i<=10:
    if(i%2 != 0):
        i = i+1
        continue
    print(i)
    i = i+1
