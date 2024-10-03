# print = 20 # do not use keyword names as variable names
# print(print) # because if used, then its functionality changes and on using that function it gives error

# college = "   manipal  "

# print(college.strip())
# print(college.rstrip())
# print(college.lstrip())

# escape characters

# text = "my name is "akshay"" --> throws error
# text = "my name is \"akshay\""
# print(text)

# fruits = ["apple", "papaya", "orange", "mango"]
# fruits[1:2] = ["blackcurrent", "cherry"]
# fruits[1:3] = ["watermelon"]
# print(fruits)

# print(fruits[::-1]) # to reverse the list without any loop or function

# lst = [[1,2,3],[4,5],[6,7]]
# lst[1][1] = 10 # accessing items in embedded list
# print(lst)

# tuple constructor

# tpl = tuple(("q","1","akshay"))
# tpl = ("blue",)
# print(tpl)
# print(type(tpl))

company = "upflairs"
x = company[-7::-1]
print(company[4::-1])
print(type(x))