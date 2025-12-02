import time
import random
print('This program cponstantly make you take care of two vehicles the bmw and the ferrari \n',
'REMEMBER : *type anything other than y in the program if you want the program to stop' , 'The cars both operate after fueling them and reduce in both fuel and heat')
class Vehicle() :
   def __init__(self , fuel , heater) :
      self.fuel = fuel
      self.heater = heater
class Bmw(Vehicle) :
   def __init__(self , fuel , heater) :
      self.fuel = 0
      self.heater = 0
   def fill(self):
      if self.fuel + 30 >= 100 :
         print('too full')
         return 
      self.fuel += 50
   def HUp(self) :
     if self.heater + 50 >= 80 or self.heater >=100 :
        print('leave it here for now not too much ya know ')
     self.heater += 30
    
class Ferrari(Vehicle) :
   def __init__(self , fuel , heater) :
      self.fuel = 0
      self.heater = 0
   def fill(self):
      if self.fuel + 30 >= 100 :
         print('too full')
         return 
      self.fuel += 30
   def HUp(self) :
     if self.heater + 50 >= 80 or self.heater >=100 :
        print('leave it here for now not too much ya know ')
     self.heater += 30
   def __str__(self):
      return 'hm'
bmw = Bmw(0 , 0)
ferar = Ferrari(0 , 0)
def run() :
  if bmw.fuel + ferar.fuel <= bmw.heater + ferar.heater  :
     print('Running program .....')
     time.sleep(5)
     q = input('would you like to fuel up both cars(y/n) ?')
     if q.lower().strip() == 'y' :
       print('filling both....')
       time.sleep(5)
       for i in (bmw , ferar) :
          i.fill()
     else :
        exit()
  elif bmw.heater + ferar.heater < bmw.fuel + ferar.fuel :
     q = input('would you like to heat up both cars(y/n)')
     if q.lower().strip() == 'y' :
        print('heating both....')
        time.sleep(5)
        for i in (bmw , ferar) :
          i.HUp()
     else :
        exit()

while True :
 print('Cars operating.......')
 time.sleep(5)
 r = random.randint(1 , 2)
 print(r)
 if  r == 2 :
    for i in (bmw , ferar):
        i.fuel -= random.randint(10 , 40)
        if i.fuel < 0 :
           i.fuel = 0
        print('Bmw heat , bmw fuel , ferar heat , ferar fuel')
        print(f'{bmw.heater}%,{bmw.fuel}%,{ferar.heater}%,{ferar.fuel}%')

 else :
     for i in (bmw , ferar):
       i.heater -=  random.randint(10 ,20)
       if i.heater < 0 :
          i.heater = 0
       print('Bmw heat , bmw fuel , ferar heat , ferar fuel')
       print(f'{bmw.heater}% ,{bmw.fuel}%,{ferar.heater}%,{ferar.fuel}%')

    
 run()

