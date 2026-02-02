class loops:
    def star1(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print() 

obj = loops()
obj.star1(5)          