people = []
n = int(input())
for i in range(n):
    person = input()
    name, age = person.split(" ")
    person_tuple = (name, int(age))
    people.append(person_tuple)
print(people)
search_name = 'Ivan'
found = False
for name, age in people:
    if name == search_name:
        print(age)
        found = True
        break
if not found:
    print("Not foudn")