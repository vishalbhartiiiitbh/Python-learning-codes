friend=["visahl","suraj","manish","nishant","aarav"]
print(friend[0])
friend[0]="rohit" #unlike the strings lists are mutable 
print(friend[0])# in list we can addd any typr of material
print(friend[1:3])

friend.append("raju")
print(friend)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)