#coding=utf-8

class Anmial:
    def __init__(self):
        print(type(self))
        print("--------------------------------------------")

class Dog(Anmial):

    num = 100

    def __init__(self):
        super().__init__()
        Anmial.__init__(Anmial)
        Anmial.__init__(self)
        Anmial().__init__()
        print('init....')
        self.__name = "dog"

    #def __init__(self, name):
    #    print('init name....')
    #    self.__name = name

    def __setName(self,name): 
        self.__name = name;

    def setName(self,name):
        self.__setName(name)

    def showName(self):
        print(self.__name)

	# 类方法，必须要有@classmethod
	@classmethod
    def setNum(cls,num):
        cls.num = num

    @staticmethod
    def staticMethod():
        print("11111111111111111111")

    def __del__(self):
        print('over.....')



dog = Dog()

#dog.setName("123")
dog.showName()
#print(dog.__name)

dog.number = 1
print(dog.number)

dog.num = 200
print(dog.num)
print(Dog.num)

del dog.num
print(dog.num)

Dog.setNum(123)
print(Dog.num)
dog.setNum(456)
print(Dog.num)

Dog.staticMethod()
dog.staticMethod()

print(type(Dog))
print(type(dog))

print('1'*12)
print(Dog)



