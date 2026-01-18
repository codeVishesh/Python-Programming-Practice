nums = [1,2,3,4,5,6]
for i in nums:
    print(i)


nums = [1,2,3,4,5,6]
key = 4
idx = 0
for i in nums:
    if(i == key):
        print("found at index", idx)
    idx = idx  +1


seq = range(10)
for i in range(2,10,2):
    print(i)

# sum of n
n = 5
i =0
sum =0
while i<=n:
    sum = sum +i
    i = i+1
print(sum)

n = 5
i = 1
fact = 1
while i <=n:
    fact = fact * i
    i = i+1
print(fact)