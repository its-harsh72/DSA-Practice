arr = [1,2,3,4,5,6,7,8,9,0,11,22,77,55,33,66,99,22,100,105,1,2,3,4,5,6,7,8,9,0]
a = arr[0]
b = arr[0]
for num in arr:
    if num>a:
        b = a
        a = num
    elif num>b and num!=a:
        b = num
        
print("First Largest Number: ",a)
print("Second Largest Number: ",b)
