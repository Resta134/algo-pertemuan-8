person = [
    {'nama' : 'resta', 'age' : '19'},
    {'nama' : 'ina', 'age' : '20'},
    {'nama' : 'sabrina', 'age' : '22'}
]

person_new = {'nama' : 'sule', 'age' : '30'}
person.append(person_new)
print(person)

for i in person:
    print('-',i['nama'], 'umur : ',i ['age'])