from steganography.steganography import Steganography
import time
from spy_details import spy,friends,Spy,Chat_msg
from users_details import Users,User
from termcolor import colored
from Validity import *
import csv

STATUS_MESSAGES = ["Busy","Available","Imperfection is beautiful","Spy work is the best!"]

def check_special_words(s_tobeSplit):
    secret_text_words = s_tobeSplit.split()
    for word in secret_text_words:
        if word == "SOS":
            time.sleep(0.3)
            print colored("FBI called, Emergency respond team will be there ASAP.","red")
        if word == "EXTRACT":
            time.sleep(0.3)
            print colored("Extraction team sent to your location.","red")
    count = 0
    for words in secret_text_words:
        if count + 1 < len(secret_text_words):
            if secret_text_words[count].upper() == "SAVE" and secret_text_words[count + 1].upper() == "ME":
                time.sleep(0.3)
                print colored("FBI called, Emergency respond team will be there ASAP.","red")
            if secret_text_words[count].upper() == "HELP" and secret_text_words[count + 1].upper() == "ME":
                time.sleep(0.3)
                print colored("Another agent is coming to help you ASAP.","red")
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

    red_name_friend = colored(name_friend,'red')
    time.sleep(0.3)
    print "Chats with %s are:"%red_name_friend
    with open("chats.csv","rb") as chats_data:
        reader = csv.reader(chats_data)
        check = False
        for row in reader:
            if(row[0]==name_friend):
                check = True
                time.sleep(0.3)
                print row[1]
                Time = row[2]
                blue_time = colored(Time,"blue")
                time.sleep(0.3)
                print (blue_time+"\n")

        if check==False :
            time.sleep(0.3)
            print "You have no chats with the selected friend!"

def send_msg():
    friend_ch = select_friend()
    time.sleep(0.3)
    original_img = raw_input("What is the name of the image? ")
    output_path = "output.jpg"
    time.sleep(0.3)
    text = raw_input("What is the secret message? ")
    Steganography.encode(original_img,output_path,text)

    new_chat = Chat_msg(text,True)
    Time = new_chat.time
    Time = Time.strftime("%b %d %Y %H:%M:%S")
    friends[friend_ch].chats.append(new_chat)
    Name = friends[friend_ch].name
    with open("chats.csv","ab") as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([Name,text,Time])
    time.sleep(0.3)
    print "Your message is now crypted!"

def read_msg():
    sender = select_friend()
    time.sleep(0.3)
    output_path = raw_input("What is the name of the file? ")
    try:
        secret_text = Steganography.decode(output_path)

        new_chat = Chat_msg(secret_text, False)
        friends[sender].chats.append(new_chat)
        check_special_words(secret_text)
        time.sleep(0.3)
        print "Your message is now decrypted!,It is: "
        time.sleep(0.6)
        print colored(secret_text,"blue")
    except IOError:
        print "File Not Found"

def display_friends() :
    if (len(friends) == 0):
        print "You have no friends!"
        return 0
    for friend in friends:
        t = "%s.%s of age %d with rating of %.1f is online!" % (friend.sal, friend.name, friend.age, friend.rating)
        green_t = colored(t,"green")
        print green_t
        time.sleep(0.4)

def start_chat(spy) :
    spy.name = spy.sal + ". " + spy.name
    time.sleep(0.3)
    print "Authentication complete,Welcome " \
          +spy.name + " of age " + str(spy.age) + " with rating of " + str(spy.rating)
    print "Glad to have you with us!"

    load_friends()
    time.sleep(0.6)
    display_friends()

    print "First, Lets show you your chat history!\nSelect a friend with whom you want to see your chats!"
    ch = select_friend()
    load_chat(ch)

    menu_show = True
    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Read Chats\n"
    menu_choices = menu_choices+"4.Send a Message\n5.Read a Message\n6.Exit Application\n"
    while(menu_show):
        time.sleep(0.5)
        choice = raw_input(menu_choices)
        if(choice=='1'):
            spy.current_S_msg = add_status(spy.current_S_msg)
            time.sleep(0.3)
            print "Your Status message is: "+spy.current_S_msg+"\n"
        elif (choice=='2'):
            no_Of_Friends = add_friend()
            time.sleep(0.3)
            print "You have %d friend(s)!"%no_Of_Friends
        elif(choice=='3'):
            time.sleep(0.3)
            print "Select a friend with whom you want to see your chats!"
            ch1 = select_friend()
            load_chat(ch1)
        elif (choice=='4'):
            send_msg()
        elif(choice=='5'):
            read_msg()
        elif choice=='6':
            time.sleep(0.3)
            print "Thank you for using SpyChat!"
            menu_show = False
        else:
            time.sleep(0.3)
            print "Wrong input!"
            print "Closing application"
            time.sleep(0.5)
            exit()

def add_status(current_S_msg) :
    if current_S_msg!=None:
        time.sleep(0.3)
        print "Your current status is: "+ current_S_msg
    else:
        time.sleep(0.3)
        print "You have not set any status!"

    time.sleep(0.3)
    response = raw_input("Do you want to select status from old statuses?(Y/N)\n")

    if(response.upper()=='N'):
        time.sleep(0.3)
        new_S_msg = raw_input("Your status message that you want to add: ")
        if len(new_S_msg)>0:
            updated_S_msg = new_S_msg
        STATUS_MESSAGES.append(updated_S_msg)

    elif(response.upper()=='Y'):
        i = 1
        for msg in STATUS_MESSAGES:
            print str(i)+"."+msg
            i = i+1
            time.sleep(0.3)
        msg_choice = int(raw_input("Which message do you want to choose.."))
        if len(STATUS_MESSAGES)>=msg_choice :
            updated_S_msg = STATUS_MESSAGES[msg_choice-1]
    else:
        time.sleep(0.3)
        print "Wrong input!"

    return updated_S_msg

def add_friend():
    new_friend = Spy("","",0,0.0)
    time.sleep(0.3)
    new_friend.name = raw_input("Input your friends name: ")
    new_friend.name = check_name(new_friend.name)
    time.sleep(0.3)
    new_friend.sal = raw_input("Is your friend Mr or Ms: ")
    new_friend.sal= check_Sal(new_friend.sal)
    time.sleep(0.3)
    new_friend.age = int(raw_input("Age of your spy friend: "))
    time.sleep(0.3)
    new_friend.rating= input("Enter your spy friend's spy rating: ")
    if(check_age(new_friend.age)):
        friends.append(new_friend)
        with open("friends.csv","ab") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.sal,new_friend.age,new_friend.rating,new_friend.is0nline])
    else:
        time.sleep(0.3)
        print "Invalid name or not appropriate age!"

    return len(friends)

def select_friend():
    i = 1
    for friend in friends:
        print str(i)+". "+friend.sal+"."+friend.name
        i = i+1
        time.sleep(0.4)
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
        time.sleep(0.4)
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
        time.sleep(0.1)
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
        time.sleep(0.3)
        print "Hello %s!"%Users[index].username
        counter = 5
        while (counter > 0):
            time.sleep(0.3)
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
                time.sleep(0.3)
                print "Incorrect Password!"
                print "%d tries remaining!!" % (counter - 1)
            counter = counter - 1

    elif choice.upper() == 'N':
        time.sleep(0.3)
        print "SpyChat promises to be the best chat application."
        print "Our sign up is very easy and efficient!"
        time.sleep(0.3)
        spy.name = raw_input("Kindly enter your name: ")
        spy.name = check_name(spy.name)
        time.sleep(0.3)
        spy.sal = raw_input("What should we call you? ")
        spy.sal = check_Sal(spy.sal)
        time.sleep(0.3)
        print "Hello! " + spy.sal + ". " + spy.name + ", Welcome to spy chat!"
        time.sleep(0.3)
        spy.age = input("Kindly enter your age: ")
        if check_age(spy.age):
            spy.rating = input("How are you rated? ")
            if spy.rating >= 4.7:
                time.sleep(0.3)
                print "You are one of the best!"
            elif (spy.rating > 3.0 and spy.rating < 4.7):
                time.sleep(0.3)
                print "There is still a chance of improvement!"
            else:
                time.sleep(0.3)
                print "You need to work a lot more harder"

            username = spy.name+"@SpyChat"
            time.sleep(0.3)
            print "Your username is : " + username
            time.sleep(0.3)
            password_newUser = raw_input("Please Enter a password for your account(8-15chars): ")
            password_newUser = Valid_Password(password_newUser)
            new_user = User(username,password_newUser,spy.name,spy.sal,spy.age,spy.rating)
            Users.append(new_user)
            with open("users.csv", "ab") as users_data:
                writer = csv.writer(users_data)
                writer.writerow([new_user.username,new_user.password,spy.name,spy.sal,spy.age,spy.rating])
            start_chat(spy)
        else:
            time.sleep(0.3)
            print "You are not of correct age!"
            exit()

    else:
        time.sleep(0.3)
        print "Wrong input! "
        exit()
else:
    time.sleep(0.3)
    print "Wrong Input!"
    print "Closing application!"
    time.sleep(0.7)
    exit()



