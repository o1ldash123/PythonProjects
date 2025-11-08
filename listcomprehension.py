#my other folders got lost somehoq so this is my new python project folder
print('this program counts the number of  what ever letter u choose in a word example : h in hello = 1 ')
letter = input('pick a letter ')
word = input('choose a word ')
if  letter.upper() in  {'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z'}  :
  print('it is ')
else :
  print('invalid letters try picking a letter next time')
  exit()
  

def calc(words , letters ) :
  result = [i  for i in words if i.upper() == letters.upper()]
  return len(result)
  


print('The numbers of {}`s in {} is {}'.format(letter , word ,  calc(word , letter)))

