from spy_details import spy_name,spy_rating,spy_age,spy_salutation

STATUS_MESSAGES = ["Busy","Available","Imperfecton is beautiful","Spy work is the best!"]
friends_name = []
friends_sal = []
friends_age = []
friends_rating=[]


def start_chat(spy_name,spy_age,spy_rating):
    menu_show = True
    current_S_message = None

    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Exit Application\n"

    while(menu_show):
        choice = raw_input(menu_choices)
        if(choice=='1'):
            print "Status update function called"
            current_S_message = add_status(current_S_message)
            print "Your Status message is: "+current_S_message+"\n"
        elif choice=='2':
            print "Add friend function called"
            no_Friends = add_friend()
            print "You have %d friend(s)!"%no_Friends
        else:
            print "Thank you for using SpyChat!"
            menu_show = False

def add_status(current_S_message):
    if current_S_message!=None:
        print "Your current status is: "+ current_S_message
    else:
        print "You have not set any status!"

    response = raw_input("Do you want to select status from old statuses..\n")

    if(response.upper()=='N'):
        new_S_msg = raw_input("Your status message that you want to add: ")
        if len(new_S_msg)>0:
            updated_S_msg = new_S_msg
        STATUS_MESSAGES.append(updated_S_msg)

    else:
        i = 1
        for msg in STATUS_MESSAGES:
            print str(i)+"."+msg
            i = i+1
        msg_choice = int(raw_input("Which message do you want to choose.."))
        if len(STATUS_MESSAGES)>=msg_choice :
            updated_S_msg = STATUS_MESSAGES[msg_choice-1]

    return  updated_S_msg

def add_friend():
    new_name = raw_input("Input your friends name: ")
    new_sal = raw_input("Is your friend Mr. or Ms: ")
    new_age = int(raw_input("Age of your spy friend: "))
    new_rating = raw_input("Enter Spy friends' spy rating: ")
    if(len(new_name)>0 and new_age<50 and new_age>12):
        friends_name.append(new_name)
        friends_sal.append(new_sal)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
    else:
        print "Invalid name or not appropriate age"
    return len(friends_name)

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
        start_chat(spy_name, spy_age, spy_rating)

    else:
        print "You are not of correct age!"




