# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, 
# and store each as a value in your dictionary. Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

numbers = {
    'person1' : 20,
    'person2' : 10,
    'person3' : 24,
    'person4' : 7,
    'person5' : 11
}

for key,value in numbers.items():
    print(key)
    print(value)