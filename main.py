from spy_details import spy_name,spy_rating,spy_age,spy_salutation

def start_chat(spy_name,spy_age,spy_rating):
    menu_choices = "What do you want to do..\n1.Add Status message\n"
    choice = raw_input(menu_choices)
    while(choice=='1'):
        print "Status update function called\n"
        choice = raw_input(menu_choices)

print "Hello! , Lets get started"
ans = raw_input("Do you want to continue as "+spy_salutation+"."+spy_name+"..")

if(ans=='Y'):
    #start with the app
    spy_name = spy_salutation+"."+spy_name
    print "Hello! " + spy_name + ", Welcome to spy chat!"
    print "Glad to have you with us!"
    start_chat(spy_name,spy_age,spy_rating)
else:
    spy_name = raw_input("What is your name: ")
    while (len(spy_name) == 0):
        print "Invalid input, please input correct name: "
        spy_name = raw_input("What is your name: ")

    spy_salutation = raw_input("What should we call you: ")
    while (len(spy_salutation) == 0):
        print "Invalid input, please input correct salutation: "
        spy_salutation = raw_input("Salutation: ")

    spy_name = spy_salutation + "." + spy_name
    print "Hello! " + spy_name + ", Welcome to spy chat!"
    print "Alright " + spy_name + ", I'd like to know a little more about..."
    spy_age = input("Hey!, Enter your age: ")
    if spy_age > 12 and spy_age < 50:
        spy_rating = input("How are you rated: ")
        if spy_rating >= 4.7:
            print "You are one of the best!"
        elif (spy_rating > 3.0 and spy_rating < 4.7):
            print "There is still a chance of improvement!"
        else:
            print "You need to work a lot more harder"

        spy_online = True
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " with rating: " + str(
            spy_rating)
        print "Glad to have you with us!"

    else:
        print "You are not of correct age!"




