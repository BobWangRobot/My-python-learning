from sys import argv

script, filename = argv
print("We are going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file")
target = open(filename,'w')

print("Turncating the file, Goodbye!")
target.truncate()
print("Now, I 'm going to ask you for three lines.")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")
print("I'll write these to the file.")

a = '\n'

target.write(line1+a+line2+a+line3)

print("And finally,we close it.")
target.close()

