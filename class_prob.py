#create a class with x,y,z variales:
class Rakib:
    x="Sazid"
    y=20
    z=30

#create 3 object:
ob1=Rakib()
ob2=Rakib()
ob3=Rakib()

#change default values of those objects:
ob1.x="Mehedi"
ob1.y=1200
ob1.z=750
print(ob1.x,ob1.y,ob1.z)

ob2.x="Dial Vai"
ob2.y=1450
ob2.z=7500
print(ob2.x,ob2.y,ob2.z)

ob3.x="Joy"
ob3.y=600
ob3.z=6000
print(ob3.x,ob3.y,ob3.z)
#change the default variable:
Rakib.x="Lookman"
Rakib.y=100
Rakib.z=500

ob4=Rakib()
print(ob4.x,ob4.y,ob4.z)


