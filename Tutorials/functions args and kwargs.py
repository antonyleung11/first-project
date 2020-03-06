#  def keyword to define a function
print("pass keyword")


def hello_func():
    pass  # pass keyword is used when we're not done filling in our func yet, will print out none becos no return val


print(hello_func())

# return keyword + chain functions (upper)
print("\n" "return keyword")


def hello_func2():
    return "hello func2"


print(hello_func2().upper())  # prints the return value str in UPPERCASE

# parameters
print("\n" "parameters")


def hello_func3(
    greeting, name="You"
):  # '=' in the argument list sets a default argument
    return "{} {}.".format(
        greeting, name
    )  # .format will substitute whatever is in the parenthesis into the {}


print(hello_func3("Hi", "Antony"))
print(hello_func3("Hello"))

# *args and **kwargs
print("\n" "args and kwargs")


def student_info(
    *args, **kwargs
):  # allows us to accept a random number of keyword arguments (we don't know how many), args and kwargs are conventional names
    print(
        args
    )  # prints out a tuple of our positional arguments (math, art) works with both lists and tuples
    print(
        kwargs
    )  # prints out dictionary/obj with our KVPs (KW-args= Keyword arguments)


student_info("Math", "Art", name="John", age=22)  # random info about student john

# by using the * and ** in the execution of the function, you can unpack the *tuple or **dictionary
print("\n" "*args and **kwargs")


def student_info2(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "Art"]
info = {"name": "John", "age": 22}
student_info(
    courses, info
)  # instead of passing the values individually, it will pass the complete tuple and dictionary
student_info(
    *courses, **info
)  # using the * and ** will pass invidually becos it will pass a random number of keyword args, rather than the 1 tuple and 1 dictionary

