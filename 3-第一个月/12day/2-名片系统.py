print("名片系统v1.0版本".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))
cards = []#定义空列表
while True:
	fun_number = int(input("请选择功能"))
	if fun_number ==1:
		flag  = 0 #默认值 0代表不在里面
		card={}#定义空字典
		name = input("请输入名字")
		for temp in cards:
			if name == temp["name"]:
				flag = 1 #在里面
				break
			#[{1},{2},{3}]
		
		if flag == 1:#重复了直接结束当次循环，继续下次循环
			print("名字重复了")
			continue
		job = input("请输入职位")
		phone = int(input("请输入手机号"))
		company = input("请输入公司名字")
		address = input("请输入公司地址")
		#list = [{},{},{}]	
		#if flag == 0:#走到这里flag一定等于0
		card["name"] = name
		card["job"]  = job
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		#放到列表中
		cards.append(card)
		print("新增成功\n")
	elif fun_number == 2:
		name = input("请输入要查的姓名")
		flag = 0 #假设不在里面
		count = 0 #默认找到了零次 
		for temp in cards:
			count+=1 #记录找的次数
			if name == temp["name"]:
				flag = 1
				#print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s\n"%(temp["name"],temp["job"],temp["phone"],temp["company"],temp["address"]))
				break
			
		if flag == 0:
			print("查无此人\n")	
		else:
			print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s\n"%(cards[count-1]["name"],cards[count-1]["job"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"]))
	elif fun_number == 3:
		name  = input("你输入要修改的名字")	
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30," "))
				print("2:修改职位".center(30," "))
				print("3:修改手机号".center(30," "))
				print("4:修改公司名称".center(30," "))
				print("5:修改公司地址".center(30," "))
				change_num = int(input("请选择修改序号"))
				if change_num == 1:
					name = input("请输入新的名字")
					temp["name"] = name
				elif change_num == 2:
					job = input("请输入新的职位")
					temp["job"] = job
				elif change_num == 3:
					phone = int(input("请输入手机号"))
					temp["phone"] = phone
				elif change_num == 4:
					company = input("请输入新的公司名")
					temp["company"] =company
				elif change_num == 5:
					address = input("请输入新的地址")
					temp["address"] = address
				else:
					print("输入有误\n")
	elif fun_number == 4:
		name = input("请输入要删除的名字")
		flag = 0 #假设默认不存在
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				sure_num = int(input("确定要删除吗1:确定 2:返回"))
				if sure_num == 1:
					cards.remove(temp)
					print("删除成功")
			
				break

		if flag == 0:
			print("没有此人")	
	elif fun_number == 5:
		#二次确认
		break