cities = set()
city = ''
while city != 'stop':
    city = input()
    if city in cities:
        print('Repeated')
    else:
        cities.add(city)
        print("Ok")
cities.remove('stop')
print(cities)
