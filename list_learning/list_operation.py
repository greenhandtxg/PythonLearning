"""
    操作列表
"""

# 遍历整个列表
# 使用for循环遍历整个列表
cars = ['toyota', 'honda', 'yamaha']
for car in cars:
    print(car)

# 创建数值列表
# 使用函数range()
for value in range(1, 4):
    print(value, end=' ')  # 1 2 3
print()

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers, end=' ')
print()

even_number = list(range(2, 11, 2))
print(even_number, end=' ')
print()

odd_number = list(range(1, 10, 2))
print(odd_number, end=' ')
print()

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 对数字列表执行简单的统计计算
digits = list(range(1, 10))
digits.append(0)
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'michael']

# 提取2-4个元素
print(players[1:4])

# 如果没有指定第一个索引,Python将会自动从列表开头开始
print(players[:4])

# 如果没有指定第二个索引,Python将会自动从列表尾部结束
print(players[2:])

# 无论列表多长,此语法都能使你输出从特定位置到表尾的所有元素
# 如果想要输入列表最后三个元素
print(players[-3:])  # ['michael', 'florence', 'eli']

# 倒序
print(players[::-1])

# 遍历切片
for player in (players[:3]):
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foots = my_foods[:]

print(my_foods)
print(friend_foots)

my_foods.append('cannoli')
friend_foots.append('ica cream')

print(my_foods)
print(friend_foots)



