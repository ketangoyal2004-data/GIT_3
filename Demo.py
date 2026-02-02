class std:
    def name(self,name):
        self.name = name
        return self.name
    
    def course(self,course):
        self.course = course
        return self.course  
    
    def branch(self,branch):
        self.branch = branch
        return self.branch  
    
    def Age(self,age):
        self.age = age
        return self.age

    def city(self,city):
        self.city = city
        return self.city
obj = std()
print(obj.name("Alice"))  
print(obj.course("Mathematics"))
print(obj.branch("Sci"))
print(obj.Age(21))
print(obj.city("New York"))