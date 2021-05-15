# Напишите функцию описания страны принимающую один обязательный аргумент = name, 
# так же функция должна принимать произвольное кол-во аргументов, которые будут описывать страну

# >>>func(name='USA', population='330 million', is_democratic=True)
# USA
# is_democratic - 330 million print f строки
# is_democratic - True

# >>>func(name='Kyrgyzstan', area='200 km2', 
# 	have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
# Kyrgyzstan
# area - 200 km2
# have_borders_with - ['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'] 
# ```

def func(name, is_democratic, *population):
    print(name, is_democratic, f'population - {population} million')
func('USA\n', 'True\n', 330)
def func1(name1, *area, **borders):
    borders = ['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China']
    print(name1, f'area -{area}km2\n', f'have_borders_with - {borders}')
func1('Kyrgyzstan\n', 200)
