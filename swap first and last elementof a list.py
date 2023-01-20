list=[2,4,6,7,8,9]

#one method
list[0],list[-1]=list[-1],list[0]

print('after swap:',list)

#another method pop

first=list.pop(0)
last=list.pop(-1)

list.insert(0,last)
list.append(first)

print('swapping:',list)
