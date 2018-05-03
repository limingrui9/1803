list = []
name_list = []
count = 0
while count<3:
	dict = {}
	name = input('请输入名字:')	
	age = int(input('请输入年龄:'))
	sex = input('请输入性别:')
	qq = int(input('请输入qq:'))
	weight = int(input('请输入体重:'))
	if name not in name_list:

		dict['name'] = name
		dict['age'] = age
		dict['sex'] = sex
		dict['qq'] = qq
		dict['weight'] = weight
		list.append(dict)
		name_list.append(name)
		print(list)
		count+=1
	else:
		print("名字重复，请从新输入：")
age_sum = 0
for i in list:
	age_sum = age_sum+i.get("age")
	print(i)

print("平均年龄是%.2f"%(age_sum/len(list)))


for i in list:
	print(i)
#print(list)
