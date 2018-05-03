count = 0 
mysum = 0

while count<=100:
    if count%2 == 0:
        mysum = count + mysum
    count += 1
print("偶数和为%d"%mysum)

while count<=100:
    if count%2 != 0:
        mysum = count+mysum
    count += 1
print("奇数和为%d"%mysum)
'''
while count <= 100:
    count += 1
    mysum = count + mysum
print("和为%d"%mysum)
'''
