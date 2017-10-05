from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy

STATUS_MESSAGES = ["Busy","Available","Imperfection is beautiful","Spy work is the best!"]
friends = []

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

def send_msg():
    friend_ch = select_friend()
    original_img = raw_input("What is the name of the image: ")
    output_path = "output.jpg"
    text = raw_input("What is the secret message: ")
    Steganography.encode(original_img,output_path,text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_ch]["chats"].append(new_chat)
    print "Your message is now crypted!"

def read_msg():
    sender = select_friend()
    output_path = raw_input("What is the name of the file: ")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    print new_chat["message"]
    friends[sender]["chats"].append(new_chat)
    print "Your message is now decrypted!"

def start_chat(spy) :
    spy["spy_name"] = spy["spy_salutation"] + ". " + spy["spy_name"]
    print "Authentication complete. Welcome "
    print spy["spy_name"] + " age: " + str(spy["spy_age"]) + " with rating: " + str(spy["spy_rating"])
    print "Glad to have you with us!"

    menu_show = True
    current_S_message = None

    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Select Friend\n"
    menu_choices = menu_choices+"4.Send Message\n5.Read Message\n6.Exit Application\n"

    while(menu_show):
        choice = raw_input(menu_choices)
        if(choice=='1'):
            print "Status update function called.."
            current_S_message = add_status(current_S_message)
            print "Your Status message is: "+current_S_message+"\n"
        elif (choice=='2'):
            print "Add friend function called..."
            no_Friends = add_friend()
            print "You have %d friend(s)!"%no_Friends
        elif(choice=='3'):
            print "Select Friend called.."
            t = select_friend()
        elif (choice=='4'):
            print "Send message called.."
            send_msg()
        elif(choice=='5'):
            print "Read message called.."
            read_msg()
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

    elif(response.upper()=='Y'):
        i = 1
        for msg in STATUS_MESSAGES:
            print str(i)+"."+msg
            i = i+1
        msg_choice = int(raw_input("Which message do you want to choose.."))
        if len(STATUS_MESSAGES)>=msg_choice :
            updated_S_msg = STATUS_MESSAGES[msg_choice-1]
    else:
        print "Wrong input!"

    return  updated_S_msg

def add_friend():
    new_friend = {
        "name": "",
        "age": 0,
        "salutation": "",
        "rating": 0.0,
        "online": True,
        "chats" :[]
    }

    new_friend["name"] = raw_input("Input your friends name: ")
    new_friend["name"] = check_name(new_friend["name"])
    new_friend["salutation"] = raw_input("Is your friend Mr or Ms: ")
    new_friend["salutation"] = check_Sal(new_friend["salutation"])
    new_friend["name"] =  new_friend["salutation"] +". " + new_friend["name"]
    new_friend["age"] = int(raw_input("Age of your spy friend: "))
    new_friend["rating"]= input("Enter your spy friend's spy rating: ")
    if(check_age(new_friend["age"])):
        friends.append(new_friend)
    else:
        print "Invalid name or not appropriate age!"
    return len(friends)

def select_friend():
    if(len(friends)==0):
        print "You have no friends!"
        return 0
    for friend in friends:
        print "%s age: %d with rating of %.1f is online"%(friend["name"],friend["age"],friend["rating"])
    i = 1
    for friend in friends:
        print str(i)+"."+friend["name"]
        i = i+1
    index = input("Select a friend from the above list by entering the index before the name: ")
    while(index>len(friends)):
        print "Invalid input"
        index = input("Enter correct index: ")
    return (index-1)

print "Hello! , Lets get started"
ans = raw_input("Do you want to continue as "+spy["spy_salutation"]+"."+spy["spy_name"]+"..")

if(ans.upper()=='Y'):
    #start with the app
    start_chat(spy)
else:
    spy["spy_name"] = raw_input("What is your name: ")
    spy["spy_name"]=check_name(spy["spy_name"])
    spy["spy_salutation"] = raw_input("What should we call you: ")
    spy["spy_salutation"] = check_Sal(spy["spy_salutation"])

    print "Hello! " + spy["spy_salutation"]+". " + spy["spy_name"] + ", Welcome to spy chat!"
    print "Alright " + spy["spy_salutation"]+". " + spy["spy_name"] + ", I'd like to know a little more about you!"

    spy["spy_age"]= input("Hey!, Enter your age: ")

    if check_age(spy["spy_age"]):
        spy["spy_rating"] = input("How are you rated: ")
        if spy["spy_rating"] >= 4.7:
            print "You are one of the best!"
        elif (spy["spy_rating"] > 3.0 and spy["spy_rating"] < 4.7):
            print "There is still a chance of improvement!"
        else:
            print "You need to work a lot more harder"

        spy["spy_online"] = True
        start_chat(spy)
    else:
        print "You are not of correct age!"




