from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy,friends,Spy,Chat_msg
from users_details import Users,User

from Validity import *
import csv

STATUS_MESSAGES = ["Busy","Available","Imperfection is beautiful","Spy work is the best!"]

def check_special_words(s_tobeSplit):
    secret_text_words = s_tobeSplit.split()
    for word in secret_text_words:
        if word == "SOS":
            print "FBI called, Emergency respond team will be there ASAP."
        if word == "EXTRACT":
            print "Extraction team sent to your location."
    count = 0
    for words in secret_text_words:
        if count + 1 < len(secret_text_words):
            if secret_text_words[count].upper() == "SAVE" and secret_text_words[count + 1].upper() == "ME":
                print "FBI called, Emergency respond team will be there ASAP."
            if secret_text_words[count].upper() == "HELP" and secret_text_words[count + 1].upper() == "ME":
                print "Another agent is coming to help you ASAP."
        count = count+1

def load_friends():
    with open("friends.csv","rb") as friends_data:
        reader = csv.reader(friends_data)
        for row in reader:
            spy_temp = Spy(row[0],row[1],int(row[2]),float(row[3]))
            friends.append(spy_temp)

def load_users():
    with open("users.csv","rb") as users_data:
        reader = csv.reader(users_data)
        for row in reader:
            user_temp = User(row[0],row[1],row[2],row[3],int(row[4]),float(row[5]))
            Users.append(user_temp)

def load_chat(ch):
    name_friend = friends[ch].name
    print "Chats with %s are: "%name_friend
    with open("chats.csv","rb") as chats_data:
        reader = csv.reader(chats_data)
        check = False
        for row in reader:
            if(row[0]==name_friend):
                check = True
                print row[1]+"\nTime: "+row[2]

        if check==False :
            print "You have no chats with the selected friend!"

def send_msg():
    friend_ch = select_friend()
    original_img = raw_input("What is the name of the image? ")
    output_path = "output.jpg"
    text = raw_input("What is the secret message? ")
    Steganography.encode(original_img,output_path,text)

    new_chat = Chat_msg(text,True)
    time = new_chat.time
    time = time.strftime("%b %d %Y %H:%M:%S")
    friends[friend_ch].chats.append(new_chat)
    Name = friends[friend_ch].name
    with open("chats.csv","ab") as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([Name,text,time])
    print "Your message is now crypted!"

def read_msg():
    sender = select_friend()
    output_path = raw_input("What is the name of the file? ")
    try:
        secret_text = Steganography.decode(output_path)

        new_chat = Chat_msg(secret_text, False)

        check_special_words(secret_text)

        print "Your message is now decrypted!"
        for chat in friends[sender].chats:
            if (chat.sent_by_me):
                a = "right"
            else:
                a = "left"
            print chat.msg +" " +  a
    except IOError:
        print "File Not Found"

def display_friends() :
    if (len(friends) == 0):
        print "You have no friends!"
        return 0
    for friend in friends:
        print "%s.%s of age %d with rating of %.1f is online!" % (friend.sal, friend.name, friend.age, friend.rating)

def start_chat(spy) :
    spy.name = spy.sal + ". " + spy.name
    print "Authentication complete,Welcome " \
          +spy.name + " of age " + str(spy.age) + " with rating of " + str(spy.rating)
    print "Glad to have you with us!"

    load_friends()
    display_friends()
    print "First, Lets show you your chat history!\nSelect a friend whom you want to see your chats!"
    ch = select_friend()
    load_chat(ch)

    menu_show = True
    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Select Friend\n"
    menu_choices = menu_choices+"4.Send Message\n5.Read Message\n6.Exit Application\n"
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
        elif choice=='6':
            print "Thank you for using SpyChat!"
            menu_show = False
        else:
            print "Wrong input!"
            exit()

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
    new_friend.age = int(raw_input("Age of your spy friend: "))
    new_friend.rating= input("Enter your spy friend's spy rating: ")
    if(check_age(new_friend.age)):
        friends.append(new_friend)
        with open("friends.csv","ab") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.sal,new_friend.age,new_friend.rating,new_friend.is0nline])
    else:
        print "Invalid name or not appropriate age!"

    return len(friends)

def select_friend():
    i = 1
    for friend in friends:
        print str(i)+". "+friend.sal+"."+friend.name
        i = i+1
    index = input("Select a friend from the above list by entering the number before the name? ")
    while(index>len(friends)):
        print "Invalid input"
        index = input("Enter correct index: ")
    return (index-1)

def select_user():
    i = 1
    for user_spy in Users:
        print str(i)+"."+user_spy.username
        i = i+1
    index = input("Select from above which user are you? ")
    while (index > len(Users)):
        print "Invalid input"
        index = input("Enter correct index: ")
    return (index - 1)


print "Hey There.\nThis is SpyChat."
ans = raw_input("Do you want to continue as "+spy.sal+"."+spy.name+"?(Y/N): ")

if ans.upper()=='Y':
    #start with the app
    counter = 5
    while(counter>0):
        p = raw_input("Password: ")
        if (p == "HarshS1234"):
            start_chat(spy)
            break
        else:
            print "Incorrect Password!"
            print "%d tries remaining!!"%(counter-1)
        counter = counter-1
    exit()
elif ans.upper()=='N':
    choice = raw_input("Are you an existing user of SpyChat? ")
    if choice.upper()=='Y':
        load_users()
        index = select_user()
        print "Hello %s!"%Users[index].username
        counter = 5
        while (counter > 0):
            p = raw_input("Enter Password: ")
            if (p == Users[index].password):
                temp_user = Users[index]
                spy.name = temp_user.name
                spy.sal = temp_user.sal
                spy.age = temp_user.age
                spy.rating = temp_user.rating
                start_chat(spy)
                break
            else:
                print "Incorrect Password!"
                print "%d tries remaining!!" % (counter - 1)
            counter = counter - 1

    elif choice.upper() == 'N':
        print "SpyChat promises to be the best chat application."
        print "Our sign up is very easy and efficient!"
        spy.name = raw_input("Kindly enter your name: ")
        spy.name = check_name(spy.name)
        spy.sal = raw_input("What should we call you? ")
        spy.sal = check_Sal(spy.sal)

        print "Hello! " + spy.sal + ". " + spy.name + ", Welcome to spy chat!"

        spy.age = input("Kindly enter your age: ")
        if check_age(spy.age):
            spy.rating = input("How are you rated? ")
            if spy.rating >= 4.7:
                print "You are one of the best!"
            elif (spy.rating > 3.0 and spy.rating < 4.7):
                print "There is still a chance of improvement!"
            else:
                print "You need to work a lot more harder"

            username = spy.name+"@SpyChat"
            print "Your username is : " + username
            password_newUser = raw_input("Please Enter a password for your account(8-15chars): ")
            password_newUser = Valid_Password(password_newUser)
            new_user = User(username,password_newUser,spy.name,spy.sal,spy.age,spy.rating)
            Users.append(new_user)
            with open("users.csv", "ab") as users_data:
                writer = csv.writer(users_data)
                writer.writerow([new_user.username,new_user.password,spy.name,spy.sal,spy.age,spy.rating])
            start_chat(spy)
        else:
            print "You are not of correct age!"
            exit()

    else:
        print "Wrong input! "
        exit()
else:
    print "Wrong Input!"
    print "Closing application!"
    exit()



