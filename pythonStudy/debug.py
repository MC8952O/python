myTuple = ()
print(type(myTuple)) #<class 'tuple'>
myTuple = (1, 2, 'hello python', 23.4, (1, 3, 'mia'), [12, 'mia', 12.4, (1,)], True)
print(myTuple)
#遍历元组
for i in myTuple:
    print(i, end =" ")
print()
print(myTuple[::-2])
print(myTuple[-5:-1:1]) #
print(myTuple[-4:-2:-1])
myTuple[5][1] = 'mia1'
print(myTuple)
print(myTuple.count(1)) #2