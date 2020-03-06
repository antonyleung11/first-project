language = "Java"

# use elif as 'else if'

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("false")

# python does not have switch case, instead it uses if, elif and else

# booleans , and , or , not
user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin page")
else:
    print("Bad Creds")

if not logged_in:
    print("please log in")
else:
    print("Welcome")

# object identity 'IS' comparison operator
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print("a id= " + str(id(a)))
print("b is= " + str(id(b)))

# checks to see whether the id of each list is the same, each list as their own ids
print(a is b)

