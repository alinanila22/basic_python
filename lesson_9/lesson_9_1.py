# dict_ex = ["Даниил", "Николаев", "35", ["Москва", "Северодвинск", "Челябинск"]]
dict_ex = {"name": "Даниил", "lastname": "Николаев", "age": 35, "age": 37, "cities": ["Москва", "Северодвинск", "Челябинск"], "smoke": False}
#
# print(dict_ex['age'])

# dict_ex = dict(name="Даниид", last_name="Николаев")
# print(dict_ex)

# dict_ex = [["name", "Даниил"], ["last_name", "Николаев"]]
# print(dict(dict_ex))

# dict_ex = dict()

# """
# Ключами могут быть
# str
# int
# bool
# tuple
# """
# #del dict_ex['name']
# print(dict_ex)
# #пример : {'lastname': 'Николаев', 'age': 37, 'cities': ['Москва', 'Северодвинск', 'Челябинск'], 'smoke': False}
#
# print("name3" in dict_ex)

# dict_ex = dict.fromkeys(["Даниил", "Николаев", "35"], "йцкк")
# dict_ex.clear()
# dict_ex_2 = dict_ex.copy()
dict_ex_2 = dict(dict_ex)
# dict_ex_2['name'] = "Даня"

print(id(dict_ex))
print(dict_ex)
print(id(dict_ex_2))
print(dict_ex_2)
