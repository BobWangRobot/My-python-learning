from sys import argv

script, user_name, age = argv
prompt = 'Please tell me: '

print("Hi %s, I'm the %s script and I'm %s years old" %(user_name,script,age))
print("I'd like to ask you a few question.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s ?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright,so you said %r about like me.
You live in %r. Not sure where that is.
And you have a %r conputer. Nice.
""" % (likes, lives, computer))
input("Press Enter")
