
class cal:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def sub(a,b):
        print(a - b)

obj = cal()
obj.add(10,20)
obj.sub(20,10)


class std:
    def name(self,name):
        self.name = name
        return self.name
    
    def course(self,course):
        self.course = course    
        return self.course
    
obj = std() 
print(obj.name("Alice"))  
print(obj.course("Mathematics"))

