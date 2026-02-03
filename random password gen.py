import random

def make_password(passLength):
    password = ''
    digitCount = 0
    letterCount = 0
    upperCount = 0
    specCount = 0
    roll = 0
    for i in range(0,passLength):
       add = random.choice(makeCharaters)
       
       if add.isdigit() == True:
           digitCount += 1
       elif add.isalpha() == True:
            roll = random.randint(1,2)
            if roll == 1:
                letterCount += 1
            elif roll == 2:
                add = add.upper()
                upperCount +=1
       else:
            specCount+= 1
            
                
            
       password += add
    check_password(digitCount,upperCount,specCount,passLength,password)
    
def check_password(digitCount,upperCount,specCount,passLength,password):
    if digitCount == 0 or upperCount == 0 or specCount == 0:
        print('trying again')
        make_password(passLength)
    else:
        print(password)
        with open("passwords.txt","a")as f:
            f.write(f'\n{password}\n')

        
def user_input():
    passLength = 20
    make_password(passLength)
makeCharaters = [
    'a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9','.','$','@','!']

with open("passwords.txt","w")as f:
    f.write("passwords:")

user_input()
