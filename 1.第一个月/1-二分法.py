'''
list = [1,3,5,7,9,11,13,15,17,19,21]
key = 17
min = 0
max = len(list)-1
center = int((min + max)/2)
if key in list:

    while True:
        if list[center]> key:
            center = center-1
        elif key>list[center]:
            center = center+1
        elif key == list[center]:
            print("%s在数组里面第%s位"%(key,center))
            break
'''

list = [13,6,10,21,30,50,4,89,2]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
key = 4
min = 0
max = len(list)-1
center = int((min + max/2))
if key in list:
    while True:
        if list[center]>key:
            center = center-1
        elif list[center]<key:
            center = center+1
        elif key == list[center]:
            print("%s在列表里面是第%s位"%(key,center))
            break
        
