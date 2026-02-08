#print("hello world")
#college_name="LIET"
#print(college_name)

#a=10
#print(a)
# 5=10
# s=10
# $=10
# college="LIET"
# college_name="LIET"
#college022_name="LIET"
# print(college_name)
#print(college022_name)
# 124name="LIET"
#_name="Priya"
#__name="Jiya"
# a="01"
# Age=19
# age=18
# print(Age)
# print(age)

# <<< String
#college_name="LIET"
#print("My college name is",college_name)
#print(type(college_name))
#print(len(college_name))
#print(f"Hello my college name {college_name} and i am from alwar")

# college_name = "liet"
# print(type(college_name))
# print(len(college_name))


#>>>>>>>>>>>>>indexing
# college_name = "liet"
# print(college_name[0])
# print(college_name[1])
# print(college_name[2])
# print(college_name[3])

#>>>>>>>>>>>slicing
# college_name = "liet"
# print(college_name[0:4])
# print(college_name[0:3])
# print(college_name[1:4])
# print(college_name[1:3])
# print(college_name[0:])
# print(college_name[-1])


#>>>>>>>>operations
# college_name = "liet"
# college_address = "alwar"
# print(college_name + college_address)
# lower_case = college_name.lower() # convert to lower case
# print(lower_case)

# college_name = "liet"
# upper_case = college_name.upper() # convert to upper case
# print(upper_case)

# college_name = "liet"
# casefold_case = college_name.casefold() # convert to casefold case #(TASK:-FIND DIFFERENCE BETWEEN CASEFOLD AND LOWER)
# print(casefold_case)

# college_name = "liet"
# title_case = college_name.title() # convert to title case
# print(title_case)
# print(college_name.capitalize()) #TASK 2

# paragraph = """Technology plays an important role in our daily lives by making tasks faster, easier, and more efficient. From smartphones that help us communicate instantly to computers that support education and work, technology connects people across the world. It also improves healthcare, transportation, and entertainment. However, it is important to use technology wisely and balance screen time with real-world activities to maintain a healthy lifestyle."""
# print(paragraph)

# college_name = "liet"
# print(college_name.find("e")) # find the index of "e"
# print(college_name.count("i")) # count the number of "i"

# clg = "liet"
# print(clg*3)

#>>>>>>>list{collection of items} 
#heterogeneous(can store different data types)
#duplicates are allowed
#list is mutable
# list = [1,2,3,4,5]
# print(list)
# print(type(list))
# print(len(list))

# print(list[0])
# print(list[2])
# print(list[0:3])
# print(list[0:])

#lst = [1,2,3,3.5,5,5,"hello","liet"]
#lst.append(40)#element add at last element
#lst.insert(56,7)
#lst.extend(10,20)
#lst.pop()#remove the last element
#lst.pop(0)
#print(lst)

#lst.remove(3.5)
#print(lst)

#lst.reverse()#tast3
#lst.clear()
#lst.count()
#lst.copy()
#lst.sort()
#print(lst)

#>>>>>>>tuple
#heterogeneous(can store different data types)
#duplicates are allowed
#immutable
#tpl = (1,2,3,4,4,5.6,"hello","hiieee")
#print("this is my first tuple :-",tpl)
#print(type(tpl))
# print(len(tpl))
# print(tpl[0])
# print(tpl[1:4])

# a = 1,2,3,4,5
# print(a)
# type(a)
# len(a)

# a,b,c = (1,2,3) #unpacking tuple
# print(a)
# print(b)
# print(c)

# tpl = (1,2,3,4,4,5.6,"hello","hiieee")#typecasting
# lst = list(tpl)
# print(lst)
# lst.append = ("liet alwar")
# tpl = tuple(list)
# print(tpl)

#>>>>>>dictionary{key:value}
#>>key must be unique
#>>

# student= {
#     "name":"priya",
#     "age":"19",
#     "address":"alwar",
#     "college_name" :"liet"
    
# }
# print(student)
# print(type(student))
# print(len(student))
# print(student["name"])
# print(student["age"])
# print(student["address"])
# print(student["college_name"])

#print(student.keys())
#print(student.values())
#print(student.items())

 #task3:-update,deep copy,copy
 # print(student.get("name"))

#adding multiple names to key:-
student= {
    "name":["priya","jiya","riya"]
}
print(student["name"])

