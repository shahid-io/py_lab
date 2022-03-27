#number list
number = [1,2,3,4,4,5,56,6,]

#using constructor
number2  = list((1,2,3,4,5,6,7))

print("numbers : ",number,type(number),number2,type(number2))

#string list
fruits = ['mango','banana','grapes','orange']
print("fruits : ",fruits,type(fruits))

#using constructor
fruits2 = list(('mango','banana','grapes','orange'))
print("fruits : ",fruits2,type(fruits2))


#length of lists
print("number list length : ",len(number),"number2 list length : ",len(number2))
print("fruits list length : ",len(fruits),"fruits2 list length : ",len(fruits2))

print("count ",fruits[0].startswith('m'))
print(fruits[2].split())

#reverse
print("reverse list : ",number.reverse())
print("reverse list : ",fruits.sort(reverse = True))

