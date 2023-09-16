"""
    列表(list): 由一些列按特定顺序排序的元素组成
    可以将任何东西加入到列表中,其中的元素可以没有任何关系
"""

# 在Python中,用方括号[]来表示列表;并用逗号来分隔其中的元素
bicycle = ['trek', 'xds', 'redline', 'specialized']
print(bicycle)

# 如果让Python将列表打印出来,Python将打印列表的内部表示,包括方括号
# ['trek', 'xds', 'redline', 'specialized']

# 访问列表的元素
# 列表是有序集合,因此要访问列表的任何元素,只要将该元素的位置或索引告诉Python即可
# 从列表bicycle中提取第一款自行车
print(bicycle[0])

# 可以使用方法title()让元素 'trek' 的格式更整洁
print(bicycle[0].title())


# 在Python中,列表的第一个元素是从0开始的
# Python为访问列表的最后一个元素提供了一种特殊的语法
# 通过将索引指定为-1,可以让Python返回最后一个列表元素
print(bicycle[-1])

# 使用列表中的各个值
# 可以像使用其他变量一样使用列表中的各个值
message = "My first bicycle was a " + bicycle[0].title()
print(message)

# 将一些朋友的姓名存储在一个列表中,并将其命名为 names
# 依次访问该列表中的每个元素,从而将每个朋友的姓名都打印出来
names = ["Tom", "Jerry", "Jack", "Rose"]
print(names)

# 继续使用上面的列表,但不打印每个朋友的姓名
# 而为每人打印一条消息.每条消息都包含相同的问候语,但抬头为相应朋友的姓名
print(names[0] + ", good morning!")
print(names[1] + ", good morning!")
print(names[2] + ", good morning!")
print(names[3] + ", good morning!")

# 修改列表元素
# 修改列表元素的语法与访问列表元素的语法相似
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表中添加元素
# 1.在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# 方法append()让动态创建列表易如反掌
# 可以先创建一个空列表,在使用一系列的append()语句添加元素
motorcycles = []
# motorcycles = list()  也可以通过此种方式,定义空列表
motorcycles.append('honda')
motorcycles.append('yamaha')

print(motorcycles)

# 2.在列表中添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.从列表中删除元素
# 3.1使用del语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# 还可以使用del语句删除列表
del motorcycles
# print(motorcycles) NameError: name 'motorcycles' is not defined

# 3.2使用pop()语句删除元素
# 方法pop()可以删除列表末尾元素,并且你能够接着使用它
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 弹出列表中任意位置处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
second_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(second_motorcycle)

# 4.根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

# 如果你可以邀请任何人一起共进晚餐(无论是在世的还是故去的)
# 你会邀请哪些人?请创建一个列表,其中包含至少 3 个你想邀请的人
# 然后,使用这个列表打印消息,邀请这些人来与你共进晚餐
invitation_list = ['jordan', 'curry', 'Durant', 'James', 'Park']
print(invitation_list[0].title() + " I'd like to invite you to dinner")
print(invitation_list[1].title() + " I'd like to invite you to dinner")
print(invitation_list[2].title() + " I'd like to invite you to dinner")
print(invitation_list[3].title() + " I'd like to invite you to dinner")
print(invitation_list[4].title() + " I'd like to invite you to dinner")

# Park无法赴约,所以邀请了Ball
print(invitation_list[-1].title() + "is busy!")
invitation_list[-1] = "Ball"
print(invitation_list[0].title() + " I'd like to invite you to dinner")
print(invitation_list[1].title() + " I'd like to invite you to dinner")
print(invitation_list[2].title() + " I'd like to invite you to dinner")
print(invitation_list[3].title() + " I'd like to invite you to dinner")
print(invitation_list[4].title() + " I'd like to invite you to dinner")

# 再邀请三位
print("We invited three more people")
# 第一位用insert()添加到名单开头
invitation_list.insert(0, "Tom")
# 第二位用insert()添加到名单中间
invitation_list.insert(int(len(invitation_list)/2), "Jerry")
# 第三位用append()添加到名单末尾
invitation_list.append("Jack")

for person in invitation_list:
    print(person.title() + " I'd like to invite you to dinner")

# 使用pop()删除嘉宾,直至只有两位嘉宾为止
while len(invitation_list) > 2:
    invitation_list.pop()

print(invitation_list)

# 使用del将最后两位嘉宾删除
del invitation_list[0]
del invitation_list[-1]
print(invitation_list)


# 组织列表
# 使用sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 也可以按相反的顺序进行永久性的排序
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# 倒着打印列表
# 方法reverse()永久修改列表元素的顺序
cars.reverse()
print(cars)

# 确定列表的长度
print(f"列表cars的长度为: {len(cars)}")
