people = 30
cars = 40
buses = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine,let's stay home then")
##if 和elif 的区别：python会遍历每个if，但是如果遇到elif，在第一个可执行elif下就会停止，不会继续往下走