## Loops : there are two loops: for and while loop

## for loop
#list of friends
friends = ["Abdullahi", "Ali", "Abdi","Hassan", "Rashid"]
friends.append("Sadio Mane")
friends.append("Mo salah")
# greet every friend in the list
for friend in friends:
    print(f"Hello {friend}")

# adding each letter in Abdullahi  in a list
# variable with my name
name = "Abdullahi"
# an empty list
letters_in_abdullahi = []

# for loop to get each letter in abdullahi,
# and add it to letters_in_abdullahi variable
for letter in name:
    letters_in_abdullahi.append(letter.title())
    print(letters_in_abdullahi)


# get each numer in a range of numeber
#numbers = [1, 2, 3, 4, 5]

# print each number in numbers variable
# for number in numbers:
#     print("hello")

for number in range(1,5):
    print(number)