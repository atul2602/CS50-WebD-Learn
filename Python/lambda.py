people = [
    {'name': "Harry", 'house': "Gryffindor"},
    {'name': "Cho", 'house': "Ravenclaw"},
    {'name': "Draco", 'house': "Slytherin"}
]

# a way to sort dicts
def f(person):
    return person["name"]

people.sort(key = f)

print(people)