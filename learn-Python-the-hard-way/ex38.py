ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gril","Boy "]

while len(stuff) != 10:
    next_one = more_stuff.pop()#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There 's %d items now."%len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])#whoa fancy
print(stuff.pop())
print(' '.join(stuff))#what? cool!返回通过指定字符连接序列中元素后生成的新字符串。
print('#'.join(stuff[3:5]))#super stellar
