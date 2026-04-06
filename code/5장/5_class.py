# 5_CLASS.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}!")
        
    def setName(self, name : str):
        '''
        Sset the Animal class's name
        Animal 클래스의 이름재정의
        :param name: Animal의 이름
        '''
        self.name = name
        
    def getName(self) -> str:
        '''
        Return the Animal class's name
        Animal 클래스의 이름봔한
        :return: Animal의 이름
        '''
        return self.name
        
class Dog(Animal):
    def __init__(self, name, age=1):
        super().__init__(name)
        self.age = age
        
    def speak(self):
        super().speak()
        print(f"{self.name} says Woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says moew!")
        
my_dog = Dog("spot")
my_cat = Cat("headache")

my_dog.speak()
my_cat.speak()

