cities = {'city': 'Москва', 'temperature': '20'}
print(cities.get('city'))
cities['temperature'] = int(cities.get('temperature')) - 5
print(cities)
print(cities.get('country','Россия'))
cities['date'] = '27.05.2019'
print(cities)
print(len(cities))