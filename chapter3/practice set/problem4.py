#  Replace the double space from problem 3 with single spaces
#  Write a program to detect double space in a string.
name = "vishal is a good boy  and smart"
print(name.find("  "))
print(name.replace("  "," "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them
