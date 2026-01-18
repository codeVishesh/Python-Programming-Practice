# strings are immutable in java but lists are mutable

student = ["vishesh", 34, "meeerut", "UP"]
print(student)
print(student[2])
print(student[1:2])

student.append("riya")
print(student)

marks = [2,6,8,1]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

age = [6,4,9,1]
age.reverse()
print(age)

ages = [1,2,3,4]
ages.insert(2,100)
print(ages)

houseNum = [2,5,7,1]
# remove element
houseNum.remove(5)  
print(houseNum)
# remove index
houseNum.pop(0)
print(houseNum)

# ques
movies = []
mov1 = input("1st movie: ")
mov2 = input("2st movie: ")
mov3 = input("3st movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# palindrome

list1 = [1,2,3,2,1]
copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("yes")
else:
    print("Not")

