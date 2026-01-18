str1 = "vishesh"
str2 = "Gupta"
finalstr = str1 + " " + str2

print(finalstr)
print(len(finalstr))

ch = finalstr[1]
print(ch)

# slicing
print(finalstr[1:4])

print(finalstr.endswith("upta"))
print(finalstr.capitalize())
print(finalstr.replace("vishesh", "riya"))
print(finalstr.find("h"))
print(finalstr.count("sh"))