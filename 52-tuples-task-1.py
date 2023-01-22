people = []
n = int(input())
for i in range(n):
    person = input()
    name, age = person.split(" ")
    person_tuple = (name, int(age))
    people.append(person_tuple)
print(people)