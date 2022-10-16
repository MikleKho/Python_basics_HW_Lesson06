# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
#  содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


# names_list = "Иван Мария Петр Илья Марина Петр Алина Бибочка Борис".split()

def make_voc(names_list):
    for i in range(len(names_list)):
        if names_list[i][0] in list(names_voc.keys()):
            names_voc[names_list[i][0]].append(names_list[i])
        else:
            names_voc[names_list[i][0]] = [names_list[i], ]
    return dict(sorted(names_voc.items()))

names_list = input("Введите имена, разделяя пробелом ---> ").split()
names_voc = {}
print(make_voc(names_list))

