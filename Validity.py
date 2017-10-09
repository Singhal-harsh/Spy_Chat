import time

def check_name(name):
    while(len(name)==0):
        time.sleep(0.3)
        print "Invalid Name!"
        time.sleep(0.3)
        name = raw_input("Please Enter correct name: ")
    return name

def check_Sal(sal):
    while(len(sal)==0):
        time.sleep(0.3)
        print "Inavlid Salutation!"
        time.sleep(0.3)
        sal = raw_input("Enter correct Salutation: ")
    return sal

def check_age(age):
    if(age>12 and age<50):
        return True
    else:
        return False

def Valid_Password(p):
      while (len(p)<8 or len(p)>15) :
         time.sleep(0.3)
         print "Invalid length of Password"
         time.sleep(0.3)
         p = raw_input("Enter Password: ")
      return p