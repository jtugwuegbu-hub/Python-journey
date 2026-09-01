class ActiveAccount:
    def total(self):
        print(self.a + self.b)
    def average(self):
        print((self.a + self.b)/2)

account1=ActiveAccount()
account2=ActiveAccount()

account1.a=100
account1.b=500

account2.a=200
account2.b=400

#account1.total()

#-------------------------------------------------------
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def talk(self):
        print(self.firstname, self.lastname, "can talk")

person1= Person("Justin", "Ugwuegbu")
person2= Person("Jesse", "Ugwuegbu")

#person1.talk()
#person2.talk()

#-----------------------------------------------------------
class Amphibian:

    def walk(self):
        print("Walks on land")

    def swim(self):
        print("Swims in water")


class Frog(Amphibian):
   pass

class Alligator(Amphibian):

    def diet(self):
        print("Eats meat")


frog1 = Frog()
alligator1 = Alligator()

# frog1.walk()
# frog1.swim()

# alligator1.walk()
# alligator1.swim()
# alligator1.diet()

#----------------------------------------------
class Vehicle: #parent class
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def bus_fare(self):
        fare= self.capacity * 100

        if self.mileage > 500:
            fare *= 1.5
        elif self.mileage > 100:
            fare *= 1.1
        
        print(fare)

bus1 = Bus("bus", 600, 50)
#bus1.bus_fare()

#-----------------------------------------------
class Door: #parent class
    def open(self):
        print("push to open")
    def close(self):
        print("the door is closing")

class Outsider(Door):
    def open(self):
        print("pull to open")

class Insider(Door):
    pass

door1=Outsider()
door2=Insider()

# door1.open()
# door1.close()
# door2.open()
# door2.close()

#------------------------------------
class Calculate:
    def add(self,numbers):
        self.total=sum(numbers)
        self.amount=len(numbers)
        return self
    def avergae(self):
        print(self.total/self.amount)
        return self.total
Calculate1=Calculate()

#Calculate1.add([10,20,30,40]).avergae()

#------------------------------------------
class Human:
    def __init__(self,name,age,pref):
        self.name=name
        self.age=age
        self.pref=pref

class Employee(Human):
    def __init__(self,name,age,pref,occupation):
        super().__init__(name,age,pref)
        self.occupation=occupation
    def info(self):
        print(self.name,self.age,self.pref,self.occupation)

Employee1=Employee("Justin",18,"soccer","reffing")
Employee2=Employee("Jeremy", 26,"spikeball","sales")
# Employee1.info()
# Employee2.info()