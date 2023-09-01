people = [
    {'name': "Harry", 'house': "Gryffindor"},
    {'name': "Cho", 'house': "Ravenclaw"},
    {'name': "Draco", 'house': "Slytherin"}
]

# a way to sort dicts
# def f(person):
#     return person["name"]

# people.sort(key = f)

# print(people)

people.sort(key = lambda person:person["name"])

# here, person is the input to lambda person, a dict, and output is the value to be compared