class Car():

	def __init__(self,color,name):
		self.color = color
		self.name = name	
	def __str__(self):
		return "%s车的颜色是%s"%(self.name,self.color)
 
	def move(self):
		print("%s车开始跑"%self.name)

	def stop(self):
		print("%s车停了"%self.name)


bmw = Car("蓝色","宝马")
bmw.move()
bmw.stop()
print(bmw)


bc = Car("红色","奔驰")
bc.move()
bc.stop()
print(bc)
print(id(bc))