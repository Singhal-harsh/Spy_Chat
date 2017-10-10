import time


def check_name(name): #checking if the name is not empty that is no character input for name prompt
    while(len(name)==0): #not letting user to give wrong input
        time.sleep(0.3)
        print "Invalid Name!"
        time.sleep(0.3)
        name = raw_input("Please Enter correct name: ")
    return name  #return correct valid name

def check_Sal(sal): #checking if sal is not empty that is no character input for salutation prompt
    while(len(sal)==0): #not letting user to give wrong input
        time.sleep(0.3)
        print "Inavlid Salutation!"
        time.sleep(0.3)
        sal = raw_input("Enter correct Salutation: ")
    return sal #return correct valid sal

def check_age(age): #checking if the age is appropriate
    if(age>12 and age<50):
        return True  #returning true if its appropriate
    else:
        return False #returning false if the age is not right for being a spy

def Valid_Password(p): #checking if password is (8-15) chars or not
      while (len(p)<8 or len(p)>15) : #not letting user to give wrong input
         time.sleep(0.3)
         print "Invalid length of Password"
         time.sleep(0.3)
         p = raw_input("Enter Password: ")
      return p #return correct valid password