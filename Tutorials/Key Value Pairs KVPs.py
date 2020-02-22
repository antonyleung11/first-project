# key value pairs - A Dictionary denoted by { } and each key val pair is separated by ,
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"], "phone": 98765}

print(student["name"])

# you can also get the value of the key by using .get (if a key isnt available such as email then it wont throw error)

print(student.get("email"))  # returns none
print(student.get("email", "default val"))  # 2nd argument gives a default val

student["phone"] = "123333"

print(student.get("phone"))  # will update the phone number

# update method
student.update({"name": "Jane", "age": 29})

print(student)

# to delete use del
del student["age"]

print(student)  # deletes the age

# use pop to delete a key put put the deleted key into a variable
deletedPhone = student.pop("phone")
print(student)
print(deletedPhone)

# see all keys or values or all
print(student.keys())
print(student.values())
print(student.items())

# loop thru kvps
for key, value in student.items():  # each kvp in (key,value)
    print(key, value)
