arr = [1,2,3,4,5,6,7,8,9,0,11,22,77,55,33,66,99,22,100,105,1,2,3,4,5,6,7,8,9,0]
a = arr[0]
b = arr[0]
for item in range(1,len(arr)):
    if arr[item]>a:
        a =  arr[item] 
    elif arr[item]<b:
        b = arr[item]
print("Max number :",a)
print("Minimun num:",b)