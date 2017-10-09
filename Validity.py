def check_name(name):
    while(len(name)==0):
        print "Invalid Name!"
        name = raw_input("Please Enter correct name: ")
    return name

def check_Sal(sal):
    while(len(sal)==0):
        print "Inavlid Salutation!"
        sal = raw_input("Enter correct Salutation: ")
    return sal

def check_age(age):
    if(age>12 and age<50):
        return True
    else:
        return False

def Valid_Password(p):
      while len(p)<8 and len(p)>15:
         print "Invalid length of Password"
         p = raw_input("Enter Password: ")
      return p