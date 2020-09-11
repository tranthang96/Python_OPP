#thuoc tinh rieng cua mojt lop
class myClass(object):
    def __init__(self):
        self.x = 10
        self .__y = 5

    def abc():
    	print(self.y)
    	print(self.x)
 
class Class1(myClass):
    def __init__(self):
        self.z = 20
 
ob1 = Class1()

print(ob1.abc)
