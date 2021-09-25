# calling fuction inside a while loop
# def num():
#     for number in range (20,30):
#         print(number)


#     letters = "abdullahi"
#     letters_in_abdullahi = []

#     for letter in letters:
#         letters_in_abdullahi.append(letter)
#         print(letters_in_abdullahi[-1])


#     name = 5
#     while name > 0:
#         name = name -1
#         print (f"hellow{name}")
        

# sharti = 3
# while True:
#     if sharti == 0:
#         break
#     num()
#     sharti = sharti - 1  

#     print(f"\n this is sharti number{sharti}")


subjects = ["math", "english", "kisw", "kisw", "math", "scie","math"]

for subject in subjects:
    if subject == "math":
        subjects.remove(subject)
print(subjects)

# def deleeete(list_name, element):
#     rm = list_name.remove(element)
#     print(rm)

# deleeete(subjects, "math")
