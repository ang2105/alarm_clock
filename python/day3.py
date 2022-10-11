tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)

tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)

listx = list(tuplex) 

listx.remove("c") 

tuplex = tuple(listx)
print(tuplex)

#2

dict={1:"a",2:"b"}
up_dict={3:"4"}
print("Dictionary before updation: ",dict)
dict.update(up_dict)
print("Dictionary after updation: ",dict)

#3

set={"a","s","d","e","f"}
print("length of this set is ")
print(len(set))
