list = []
#增
def add():
	user = {}
	name = input('请输入姓名：')
	student_number = input('请输入学号：')
	subject = input('请输入科目:')
	grade = int(input('请输入分数：'))
	user['name'] = name
	user['student_number'] = student_number
	user['subject'] = subject
	user['grade'] = grade
	list.append(user)
#删
def delete():
	student_number = input('请输入要删除的学号：')
	for i in range(0,len(list)):
		if list[i]['student_number'] == student_number:
			list.pop(i)
			break
#改
def change():
	student_number = input('请输入要修改的学号：')
	Show = True
	for i in range(0,len(list)):
		if list[i]['student_number'] == student_number:
			add_user(i)
			Show = False
			break
		if Show:
			print('查无此人！')
#增加更改的数据
def add_user(position):
	k = True
	while k:
		mode = int(input('请输入要修改的信息：\n1.姓名\n2.学号\n3.科目\n4.分数\n5.返回上一步\n:'))
		if mode == 1:
			name = input('请输入姓名：')
			list[position]['name'] = name		
		elif mode == 2:
			student_number = input('请输入学号：')
			list[position]['student_number'] = student_number
		elif mode == 3:
			subject = input('请输入科目:')
			list[position]['subject'] = subject
		elif mode == 4:
			grade = int(input('请输入分数：'))
			list[position]['grade'] = grade
		elif mode == 5:
			k = False
#查
def examine():
	student_number = input('请输入要查找的学号：')
	flag = 0
	count = 0
	for i in list:
		count += 1
		if student_number == i['student_number']:
			flag = 1
			break


	if flag == 0:
		print('查无此人！')
	else:
		print('姓名:%s\n学号:%s\n科目:%s\n分数%d'%(list[count-1]["name"],list[count-1]["student_number"],list[count-1]["subject"],list[count-1]["grade"]))
#菜单
def Menu():
	while True:
		print("学生成绩管理系统".center(30,"*"))
		print("1:录入成绩".center(30,"-"))
		print("2:查看成绩".center(30,"-"))
		print("3:修改成绩".center(30,"-"))
		print("4:删除学生".center(30,"-"))
		print("5:  退出  ".center(30,"-"))
		mode = int(input("请选择功能序号"))
		if mode == 1:
			add()
		elif mode == 2:
			examine()
		elif mode == 3:
			change()
		elif mode == 4:
			delete()
		elif mode == 5:
			break
Menu()
