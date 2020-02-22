courses = [
    "History",
    "Math",
    "Physics",
    "CompSci",
]  # lists can be mutable, can have dupes , denoted by [ ]

tuple1 = (
    "History",
    "Math",
    "Physics",
    "CompSci",
)  # tuples are immutable (no append inserts etc.) like a CONSTANT

set1 = {
    "History",
    "Math",
    "Physics",
    "CompSci",
    "Math",
}  # sets cannot have dupes and is used for comparison like set1.difference(set2)

set2 = {"History", "Math", "Physics", "Art", "Design"}

print(set1.intersection(set2))

print(set1.difference(set2))

courses.sort()

courses.sort(reverse=True)

for index, course in enumerate(
    courses, start=1
):  # enumerate numbers each item starting from 'start'
    print(index, course)

# you can join lists together by using 'extend'
list1 = ["History", "Math", "Physics", "CompSci"]
list2 = ["Art", "English"]

list1.extend(list2)

print(list1)
