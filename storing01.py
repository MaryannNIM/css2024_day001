# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:05:53 2024

@author: User

"""
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)

print(B2)


#Using list
age = [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
print(age)


print(age[0])
print(age[1])
print(age[10])





print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)



gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])


country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])



my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

print(my_list[0:3])



person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}

print(person['name'])

print(person.get('age'))

print(person['address'])







import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

df = pd.DataFrame(data)

print(df)


print(df['age'])
print(df['gender'])


print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())


print(df[df['age'] > 30])

print(df[1:4])


df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)


df.drop(columns=['new_column'], inplace=True)
print(df)

