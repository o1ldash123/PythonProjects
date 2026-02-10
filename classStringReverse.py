class revString() :
    newString = ' '
    def __init__(self , cString, length ) :
       self.cString = cString
       self.length = length
    def reverse(self) :
      self.length = len(self.cString)
      for i in range(1,self.length +1) :
        self.newString += self.cString[i * -1]
      print(mine)
    def __str__(self):
      return self.newString
print('This program reverses the word u give it using a class')
"""Iput = input('type the word you will like to reverse ')    
mine = revString('help' , 0)
mine.reverse()"""
a = 2 *((3 * 2) + (3*8) + (8 * 2))
b = 2 * ((11 * 2) + (2*11) + (2*2))
c = 2 * (2 * 3)
print(a + b - c)
a = 2 * ((3 *2) + (3 * 10) + (2*10))
b = 2 * ((2 * 2) + (2 * 8) + (2 * 8))
c = 2 * (2 * 2)
print( a + b - c)











