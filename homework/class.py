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
#Constructors
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
#Inheritence
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
#Multi level Inheritance
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
        
        print(f"${fare}")

bus1 = Bus("bus", 600, 50)
#bus1.bus_fare()

#-----------------------------------------------
#Method overriding
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
#Method Chaining
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
#Super Function
class Human:
    def __init__(self,name,age,pref):
        self.name=name
        self.age=age
        self.pref=pref

class Employee(Human):
    def __init__(self,name,age,pref,occupation):
        super().__init__(name,age,pref)
        self.occupation=occupation
    def __str__(self):
        return f"{self.name},{self.age},{self.pref},{self.occupation}"

Employee1=Employee("Justin",18,"soccer","reffing")
Employee2=Employee("Jeremy", 26,"spikeball","sales")
#print(Employee1)
#print(Employee2)

#------------------------------------------
#Multipule Inheritence
class Inflow:
    def add_cash(self,amount):
        self.total += amount
        self.transactions.append(f"added {amount}")
class Outflow:
    def remove_cash(self,amount):
        if amount<=self.total:
            self.total -=amount
            self.transactions.append(f"removed {amount}")
        else:
            print(f"Not enough money in account, you tried to remove {amount}, only {self.total} is in the account")

class Balance(Inflow,Outflow):
    def __init__(self):
        self.total = 0
        self.transactions = []
    def history(self):
        for transaction in self.transactions:
            print(transaction)
    def AccountBalance(self):
        print(self.total)

# JustinAccount=Balance()
# JustinAccount.add_cash(100)
# JustinAccount.add_cash(500)
# JustinAccount.remove_cash(50)
# JustinAccount.history()
# JustinAccount.remove_cash(5000)
# JustinAccount.AccountBalance()

#------------------------------------------
#Abstract classes
from abc import ABC, abstractmethod

class Traffic(ABC):
    @abstractmethod
    def Green(self):
        pass
    @abstractmethod
    def Yellow(self):
        pass
    @abstractmethod
    def Red(self):
        pass

class Traffic1(Traffic):
    def Color(self): #you can add extra methods to a class that inherrited abstract method
        print("The color is black")
    def Green(self):
        print("Go")
    def Yellow(self):
        print("slow down")
    def Red(self):
        print("stop")

StopLight= Traffic1()

#StopLight.Red()

#------------------------------------------
#Objects as arguments
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __str__(self):
         return f"{self.name},{self.age},{self.grade}"
def changeinfo(Students):
    changes= input("What do you want to change: ")#split attributes with ,
    changes = changes.split(",")

    for change in changes:
        new_value=input(f"What do you want the new {change} to be: ")
        

        change= change.strip() #change is attribute
        new_value= new_value.strip()

        setattr(Students,change,new_value)


    
Student1=Students("Justin",18,12)
Student2=Students("Jo",14,12)
Student3=Students("John",20,12)

#changeinfo(Student1)

#print(Student1)
#------------------------------------------
#Duck Typing

class Car:
    def foward(self):
        print("Car is in Drive")
    def reverse(self):
        print("Car is in reverse")

class Motorcycle:
    def foward(self):
        print("Bike is going foward")
    

class Rider:
    def ride(self,vehicle):
        try:
            vehicle.foward()
            vehicle.reverse()
            print("Its a car")
        except AttributeError:
            print("not a car")

car = Car()
Motorcycle= Motorcycle()

Vehicle1=Rider()

Vehicle1.ride(Motorcycle)

