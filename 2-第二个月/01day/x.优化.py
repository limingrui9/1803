

file_name = input("请输入文件的名字")
old_file = open(file_name,"r")
content = old_file.read()

position = file_name.rfind(".")
new_file_name = file_name[0:position]+"备份"+file_name[position:]
#file_name[0:position]
#file_name[position:]



new_file = open(file_name+"复制"+file_name,"w")
new_file.write(content)



old_file.close()
new_file.close()

