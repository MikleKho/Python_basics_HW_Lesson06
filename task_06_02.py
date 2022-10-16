# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

def list_num(num_limit):
    list = [[i * 20, i * 21] for i in range(1, int(num_limit // 20) + 1)]
    list_out = [num for group in list for num in group if num <= num_limit]
    return list_out

print(list_num(int(input("Введите максимальное число ---> "))))
