# define a class
class human:
    #initialize attribute/properties name,age
    def __init__(self,name,age):
        self.name = name #"yilian"
        self.age=age #56
    #method
    def laugh(self):
        print(f"{self.name}",end="")
        for i in range(5):
            print(":-)",end="")
        print()
    def cry(self):
        print(":-(")

#build an object
I =human("yilian",56)
he = human("Cindy",34)
I.laugh()
he.cry()