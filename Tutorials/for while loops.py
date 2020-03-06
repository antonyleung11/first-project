nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

print("\n" "break keyword")

# break keyword
for num in nums:
    if num == 3:
        print("number 3 has been found")
        break
    print(num)

print("\n" "continue keyword")

# continue keyword
for num in nums:
    if num == 3:
        print("number 3 has been found")
        continue  # this will skip to the next iteration so it won't print num for 3
    print(num)

# loop in a loop
nums2 = [1, 2, 3]

print("\n" "loop in a loop")

for num in nums2:
    for letter in "abc":
        print(num, letter)

# range method prints out from first parameter (1) to second paramter -1 (11 which is 10)
print("\n" "range method")

for i in range(1, 11):
    print(i)

# while loops will keep iterating until a certain condition is met or a break has been encountered
print("\n" "While loops")
x = 0

while x < 10:
    if x == 4:
        break
    print(x)
    x += 1

# if you encounter an infinite loop press ctrl c

