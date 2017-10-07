from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy,friends,Spy,Chat_msg
import csv

STATUS_MESSAGES = ["Busy","Available","Imperfection is beautiful","Spy work is the best!"]

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

def load_friends():
    with open("friends.csv","rb") as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy_temp = Spy(row[0],row[1],int(row[2]),float(row[3]))
            friends.append(spy_temp)


def send_msg():
    friend_ch = select_friend()
    original_img = raw_input("What is the name of the image? ")
    output_path = "output.jpg"
    text = raw_input("What is the secret message? ")
    Steganography.encode(original_img,output_path,text)

    new_chat = Chat_msg(text,True)

    friends[friend_ch].chats.append(new_chat)
    print "Your message is now crypted!"

def read_msg():
    sender = select_friend()
    output_path = raw_input("What is the name of the file? ")
    secret_text = Steganography.decode(output_path)

    new_chat = Chat_msg(secret_text,False)

    print new_chat.msg
    friends[sender].chats.append(new_chat)
    print "Your message is now decrypted!"
    for chat in friends[sender].chats:
        if(chat.sent_by_me):
            a = "right"
        else:
            a = "left"
        print chat.msg+a

def start_chat(spy) :
    spy.name = spy.sal + ". " + spy.name
    print "Authentication complete. Welcome "
    print spy.name + " age: " + str(spy.age) + " with rating: " + str(spy.rating)
    print "Glad to have you with us!"

    menu_show = True

    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Select Friend\n"
    menu_choices = menu_choices+"4.Send Message\n5.Read Message\n6.Exit Application\n"

    load_friends()
    while(menu_show):
        choice = raw_input(menu_choices)
        if(choice=='1'):
            print "Status update function called.."
            spy.current_S_msg = add_status(spy.current_S_msg)
            print "Your Status message is: "+spy.current_S_msg+"\n"
        elif (choice=='2'):
            print "Add friend function called..."
            no_Of_Friends = add_friend()
            print "You have %d friend(s)!"%no_Of_Friends
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

def add_status(current_S_msg) :
    if current_S_msg!=None:
        print "Your current status is: "+ current_S_msg
    else:
        print "You have not set any status!"

    response = raw_input("Do you want to select status from old statuses?(Y/N)\n")

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

    return updated_S_msg

def add_friend():
    new_friend = Spy("","",0,0.0)

    new_friend.name = raw_input("Input your friends name: ")
    new_friend.name = check_name(new_friend.name)
    new_friend.sal = raw_input("Is your friend Mr or Ms: ")
    new_friend.sal= check_Sal(new_friend.sal)
    new_friend.name =  new_friend.sal +". " + new_friend.name
    new_friend.age = int(raw_input("Age of your spy friend: "))
    new_friend.rating= input("Enter your spy friend's spy rating: ")
    if(check_age(new_friend.age)):
        friends.append(new_friend)
        with open("friends.csv","wb") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.sal,new_friend.age,new_friend.rating,new_friend.is0nline])
    else:
        print "Invalid name or not appropriate age!"

    return len(friends)

def select_friend():
    if(len(friends)==0):
        print "You have no friends!"
        return 0
    for friend in friends:
        print "%s age: %d with rating of %.1f is online"%(friend.name,friend.age,friend.rating)
    i = 1
    for friend in friends:
        print str(i)+"."+friend.name
        i = i+1
    index = input("Select a friend from the above list by entering the index before the name: ")
    while(index>len(friends)):
        print "Invalid input"
        index = input("Enter correct index: ")
    return (index-1)

print "Hello! , Lets get started"
ans = raw_input("Do you want to continue as "+spy.sal+"."+spy.name+"?(Y/N): ")

if(ans.upper()=='Y'):
    #start with the app
    start_chat(spy)
else:
    spy.name = raw_input("What is your name? ")
    spy.name=check_name(spy.name)
    spy.sal = raw_input("What should we call you? ")
    spy.sal = check_Sal(spy.sal)

    print "Hello! " + spy.sal+". " + spy.name + ", Welcome to spy chat!"
    print "Alright " + spy.sal+". " + spy.name + ", I'd like to know a little more about you!"

    spy.age= input("Hey!, Enter your age: ")

    if check_age(spy.age):
        spy.rating = input("How are you rated? ")
        if spy.rating >= 4.7:
            print "You are one of the best!"
        elif (spy.rating > 3.0 and spy.rating < 4.7):
            print "There is still a chance of improvement!"
        else:
            print "You need to work a lot more harder"

        spy.is0nline = True
        start_chat(spy)
    else:
        print "You are not of correct age!"




