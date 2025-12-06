class Numerals :
   def __init__(self , num):
      self.num  = num
   numDictionary = {1 : 'i' , 2 : 'ii' , 10 : 'X' , 3 : 'iii' , 4 : 'iv' , 5 :'v' , 6 : 'vi' , 7 : 'vii' , 8: 'viii' , 9 : 'ix'}
   def compute (self) :
      print('Numerals :', self.numDictionary[self.num].upper())

print('enter any number from 1 to 10 to change it to roman numeral')
i = input()
cles = Numerals(int(i))
if int(i) > 10 or int(i) < 1:
  print('that number is above ten')
  pass
else :
   cles.compute()