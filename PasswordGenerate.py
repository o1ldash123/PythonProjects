import random
import time
print('This program generates a strong random password based on  2 numbers ,3 upper case and 2 lower case letters ')
uppercase_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rn1 = random.randint(1, 10)
rn2 = random.randint(1, 10)
ul1 = random.choice(list(uppercase_letters))
ul2 = random.choice(lowercase_letters)
ul3 = random.choice(list(uppercase_letters))
lc1 = random.choice(lowercase_letters)
lc2 = random.choice(lowercase_letters)
def password_generate():
 global meassage
 meassage = ' '
 yes = input('Do you want to generate a password ? (yes/no) ')
 if yes.lower().strip() == 'yes' or yes.lower() == 'y' :
    meassage += '**** ' + ul1 +  ul2  + lc1 + ul3 + lc2 +  str(rn1 ) + str(rn2) + ' ****'
 else :
    print('Password generation cancelled.')
    return ' '

def main():
  password_generate()
  print('Your generated password...' )
  time.sleep(5)
  print('is')
  time.sleep(2)
  print(meassage)


main()