x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)
diff = int(x) - int(y)
mult = int(x)*int(y)

print("The sum is: ", sum)
print("difference is: ", diff)
print("multiplied value is: ", mult)

mylist = ["cricket","batminton","hockey"]
print("the list is: ", mylist)
print(len(mylist))

mylist.remove("batminton")
print(mylist)

mylist.append("football")
print(mylist)
