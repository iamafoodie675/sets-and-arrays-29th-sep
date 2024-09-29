import array as arr 
array_num = arr.array('i',[1,3,5,3,7,9,3,3,3,9])
print("original array :",array_num)

print("Number of occurences of number 3: ",array_num.count(3))

array_num.reverse()
print("reversed array: ",array_num)