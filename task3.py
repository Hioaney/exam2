
students = {'python': ['John', 'Agness', 'Angela', 'Nash', 'Sultan', 'Janyl', 'Adyl', 'Nursultan',],
	   'javascript': ['Andrew', 'Michael','Emirlan', 'Chyngyz', 'Aidin'],
	   'java': ['Marcus', 'Don', 'Aliaskar', 'Aktanbek', 'Aigerim']}


names_ages = {'Janyl': 12, 'Nursultan': 15, 'Meerim': 18, 'Emir': 20, 'Susann': 25, 'Marcus': 9, 'Aidin': 18, 
'Aigerim': 17, 'Angela': 12, 'Albert': 26, 'Jyldyz': 40, 'Doe': 51}


names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin', 
'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe']
try:
    def func(names, names_ages):
        x = names.copy() 
        s = names_ages.copy()
        print(x, s)
    print(func(names, names_ages))
except KeyError: 
    print('Такого имени не существует')
    
            
