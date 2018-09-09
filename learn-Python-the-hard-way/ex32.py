the_count = [1,2,3,4,5]
fruits = ['apple', 'orandes', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this is first kind of for-loop goes thruugh a list
for number in the_count:
    print("This is count %d" % number)

#same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list." % i)
    #append is a function that lists understand
    elements.append(1)


#now we can print them out too
for i in elements:
    print("Element was: %d" % i)
#append:在列表末尾添加元素
#range：函数，用来创建新的整数列表
#for可以使用未被定义的变量，在循环开始时，变量会被自动定义
#二位列表：列表中包含列表