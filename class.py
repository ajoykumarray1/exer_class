class Person:
    def __init__(self,name,idnum):
        self.n=name
        self.asad=idnum
        print("This",self.asad)

    def Hi(self):
        print(self.n)
p1=Person("Asad",10)
p1.Hi()
p2=Person("Ajoy",15)
p2.Hi()
