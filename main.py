from steganography.steganography import Steganography
import time
from spy_details import spy,friends,Spy,Chat_msg
from users_details import Users,User
from termcolor import colored
from Validity import *
import csv

#using time.sleep() in project to make it look good in eyes

STATUS_MESSAGES = ["Busy","Available","Imperfection is beautiful","Spy work is the best!"]

def check_special_words(s_tobeSplit):
    #Using split function to check for special words
    secret_text_words = s_tobeSplit.split()
    for word in secret_text_words:
        #in loop for checking single special word
        if word == "SOS":
            time.sleep(0.3)
            print colored("FBI called, Emergency respond team will be there ASAP.","red")
        if word == "EXTRACT":
            time.sleep(0.3)
            print colored("Extraction team sent to your location.","red")
    count = 0
    for words in secret_text_words:
        #in loop for checking two special words
        if count + 1 < len(secret_text_words): #making sure that it doesn't go out of bound
            if secret_text_words[count].upper() == "SAVE" and secret_text_words[count + 1].upper() == "ME":
                time.sleep(0.3)
                print colored("FBI called, Emergency respond team will be there ASAP.","red")
            if secret_text_words[count].upper() == "HELP" and secret_text_words[count + 1].upper() == "ME":
                time.sleep(0.3)
                print colored("Another agent is coming to help you ASAP.","red")
        count = count+1

def load_friends():
    #opened friends.csv and reading row by row
    with open("friends.csv","rb") as friends_data:
        reader = csv.reader(friends_data)
        for row in reader:
            #create a new temp spy
            spy_temp = Spy(row[0],row[1],int(row[2]),float(row[3]))
            #append this friend spy to friends list
            friends.append(spy_temp)

def load_users():
    #opened and reading users.csv row by row
    with open("users.csv","rb") as users_data:
        reader = csv.reader(users_data)
        for row in reader:
            #created temp user
            user_temp = User(row[0],row[1],row[2],row[3],int(row[4]),float(row[5]))
            #append the user into users list
            Users.append(user_temp)

def load_chat(ch):
    name_friend = friends[ch].name
    #changing name to color red
    red_name_friend = colored(name_friend,'red')
    time.sleep(0.3)
    print "Chats with %s are:"%red_name_friend
    #reading file
    with open("chats.csv","rb") as chats_data:
        reader = csv.reader(chats_data)
        #using a check for users which dont have any chats
        check = False
        for row in reader:
            #searching for name row by row
            if(row[0]==name_friend):
                #if found, printing the chat message with required color
                check = True
                time.sleep(0.3)
                print row[1]
                Time = row[2]
                blue_time = colored(Time,"blue")
                time.sleep(0.3)
                #printing time of the chat message with required color
                print (blue_time+"\n")

        if check==False :
            time.sleep(0.3)
            #if name not found in the chats file
            print "You have no chats with the selected friend!"

def send_msg():
    #select friend called to get index for which friend,msg is to be sent
    friend_ch = select_friend()
    time.sleep(0.3)
    #asking for name of the image to be encrypted with secret text
    original_img = raw_input("What is the name of the image? ")
    output_path = "output.jpg"
    time.sleep(0.3)
    text = raw_input("What is the secret message? ")
    Steganography.encode(original_img,output_path,text)
    #using steganography module to encode text into an image giving output path
    new_chat = Chat_msg(text,True)
    Time = new_chat.time
    Time = Time.strftime("%b %d %Y %H:%M:%S") #coverting time to string
    friends[friend_ch].chats.append(new_chat) #append new chat
    Name = friends[friend_ch].name
    #writing name, text and time of the chat message in chats.csv
    with open("chats.csv","ab") as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([Name,text,Time])
    time.sleep(0.3)
    print "Your message is now crypted!"

def read_msg():
    #select friend called to get index of which friend the message u want to read from
    sender = select_friend()
    time.sleep(0.3)
    output_path = raw_input("What is the name of the file? ")#name of the image that has encoded message
    try:
        secret_text = Steganography.decode(output_path)
        #decoding message using steganography module
        new_chat = Chat_msg(secret_text, False)
        friends[sender].chats.append(new_chat)
        check_special_words(secret_text) #checking for special words
        time.sleep(0.3)
        print "Your message is now decrypted!,It is: "
        time.sleep(0.6)
        print colored(secret_text,"blue") #printing colored message in color blue
    except IOError:
        #exception of IOError to prevent program from stopping when this error is incurred
        print "File Not Found"

def display_friends() :
    if (len(friends) == 0):
        print "You have no friends!"
        return 0
    for friend in friends:
        #printing friends details using attributes of object(friend) of class Spy
        t = "%s.%s of age %d with rating of %.1f is online!" % (friend.sal, friend.name, friend.age, friend.rating)
        green_t = colored(t,"green")
        print green_t #printing in green color
        time.sleep(0.4)

def start_chat(spy) :
    #concatenating name with salutation
    spy.name = spy.sal + ". " + spy.name
    time.sleep(0.3)
    #welcome message
    print "Authentication complete,Welcome " \
          +spy.name + " of age " + str(spy.age) + " with rating of " + str(spy.rating)
    print "Glad to have you with us!"

    load_friends() #load friends (adding friends from file to temp list)
    time.sleep(0.6)
    display_friends()#display friends as asked in extra objectives

    print "First, Lets show you your chat history!\nSelect a friend with whom you want to see your chats!"
    ch = select_friend()
    load_chat(ch) #loading chats from file and displaying it as asked in extra objectives

    menu_show = True #check when user entered n=choice for exiting
    menu_choices = "What do you want to do..\n1.Add Status message\n2.Add Friend\n3.Read Chats\n"
    menu_choices = menu_choices+"4.Send a Message\n5.Read a Message\n6.Exit Application\n"
    while(menu_show):
        time.sleep(0.5)
        choice = raw_input(menu_choices)
        if(choice=='1'):
            spy.current_S_msg = add_status(spy.current_S_msg)
            if(spy.current_S_msg==None): #checkinng if invalid input was given
                print "Invalid input, No status updated!"
                continue
            time.sleep(0.3)
            print "Your Status message is: "+spy.current_S_msg+"\n" #displaying current status message
        elif (choice=='2'):
            no_Of_Friends = add_friend() #getting no of friends after add friend
            time.sleep(0.3)
            print "You have %d friend(s)!"%no_Of_Friends #display no of friends
        elif(choice=='3'):
            time.sleep(0.3)
            print "Select a friend with whom you want to see your chats!"
            ch1 = select_friend() #selecting a friend for chats
            load_chat(ch1) #loading and displaying chats
        elif (choice=='4'):
            send_msg() #call for sending msg
        elif(choice=='5'):
            read_msg() #call for reading msg
        elif choice=='6':
            time.sleep(0.3)
            print "Thank you for using SpyChat!" #exit message
            menu_show = False
        else:
            time.sleep(0.3)
            print "Wrong input!"
            print "Closing application" #wrong input entered
            time.sleep(0.5)
            exit() #closing application

def add_status(current_S_msg) :
    if current_S_msg!=None: #checking for msg to be none (i.e not set still)
        time.sleep(0.3)
        print "Your current status is: "+ current_S_msg #displaying current status
    else:
        time.sleep(0.3)
        print "You have not set any status!" #telling user about no status set

    time.sleep(0.3)
    # asking user to chose from old statuses or to give his own status
    response = raw_input("Do you want to select status from old statuses?(Y/N)\n")

    if(response.upper()=='N'):
        time.sleep(0.3)
        #asking the user for his own status message
        new_S_msg = raw_input("Your status message that you want to add: ")
        if len(new_S_msg)>0:
            updated_S_msg = new_S_msg
        STATUS_MESSAGES.append(updated_S_msg) #updating status list with new updated message

    elif(response.upper()=='Y'):
        i = 1
        for msg in STATUS_MESSAGES:
            print str(i)+"."+msg
            i = i+1
            time.sleep(0.3)
        #asking the user to select from the above displayed list
        msg_choice = int(raw_input("Which message do you want to choose.."))
        if msg_choice<=len(STATUS_MESSAGES) :
            updated_S_msg = STATUS_MESSAGES[msg_choice-1]  #assigning updated msg to msg from the list
        else:
            time.sleep(0.3)
            print "Wrong input!" #telling user about wrong input
            updated_S_msg = None #setting updated_S_msg to be none so that add status becomes of no effect
    else:
        time.sleep(0.3)
        print "Wrong input!" #telling user about wrong input
        updated_S_msg = None #setting updated_S_msg to be none so that add status becomes of no effect

    return updated_S_msg #returning updated msg

def add_friend():
    #creating a new default friend
    new_friend = Spy("","",0,0.0)
    time.sleep(0.3)
    new_friend.name = raw_input("Input your friends name: ") #asking for friend's name
    new_friend.name = check_name(new_friend.name) #checking the validity of the name
    time.sleep(0.3)
    new_friend.sal = raw_input("Is your friend Mr or Ms: ") #asking foor salutation
    new_friend.sal= check_Sal(new_friend.sal)#checking the validity of the salutation
    time.sleep(0.3)
    new_friend.age = int(raw_input("Age of your spy friend: ")) #age input in int
    time.sleep(0.3)
    new_friend.rating= input("Enter your spy friend's spy rating: ") #rating input in float
    if(check_age(new_friend.age)): #check for appropriate age
        friends.append(new_friend) #if valid new friend to be appended at the end of the friends list
        #writing details of new friend at the end of the file using ab
        with open("friends.csv","ab") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.sal,new_friend.age,new_friend.rating,new_friend.is0nline])
    else:
        time.sleep(0.3)
        print "Sorry you are not of appropriate age to be a Spy!" #inappropriate age

    return len(friends) #return length of friends list

def select_friend():
    i = 1
    #displaying friends from friends list starting count from 1
    for friend in friends:
        print str(i)+". "+friend.sal+"."+friend.name
        i = i+1
        time.sleep(0.4)
    #asking user to select a friend
    index = input("Select a friend from the above list by entering the number before the name? ")
    while(index>len(friends)): #index cannot e greater than len of friends list
        print "Invalid input" #output for invalid input
        index = input("Enter correct index: ") #not allowing user to enter wrong input
    return (index-1) #return selected friend by returning index

def select_user():
    i = 1
    #displaying user from users list starting the count from 1
    for user_spy in Users:
        print str(i)+"."+user_spy.username
        i = i+1
        time.sleep(0.4)
    index = input("Select from above which user are you? ")
    while (index > len(Users)): #index cannot be greater than len of users list
        print "Invalid input"
        index = input("Enter correct index: ") #not allowing user to enter wrong input
    return (index - 1) #return selected user by retuning index

#starting msgs in colour
print colored("Hey There","red")
print colored("This is SpyChat.","blue")
#prompt for whether default user or not
ans = raw_input("Do you want to continue as "+spy.sal+"."+spy.name+"?(Y/N): ")

if ans.upper()=='Y': #when user is the default user
    #loop for password tries
    counter = 5
    while(counter>0):
        time.sleep(0.1)
        p = raw_input("Password: ") #asking for password
        if (p == "HarshS1234"): #checking for correct password
            start_chat(spy) #start with the app
            break
        else:
            time.sleep(0.3)
            print colored("Incorrect Password!","red") #displaying incorrect password in red
            if counter-1==0: #for last try
                print colored("You are out of tries!","red")  #last try done printing it in red
                time.sleep(0.3)
                print "Closing Application!"
                exit()
            else:
                print "%d tries remaining!!" % (counter - 1)  # displayes no of tries remaining
        counter = counter-1
    exit()
elif ans.upper()=='N': #when not the default user
    choice = raw_input("Are you an existing user of SpyChat? ") #exsting or new user
    if choice.upper()=='Y': #when existing user
        load_users() #users from file added to the list
        index = select_user() #select which user are you
        time.sleep(0.3)
        print "Hello %s!"%Users[index].username #display message of hello with username
        #password loop
        counter = 5
        while (counter > 0):
            time.sleep(0.3)
            p = raw_input("Enter Password: ")
            if (p == Users[index].password): #checking with the password stored in the list
                temp_user = Users[index] #creating a temp user
                #equating details of the spy in the used program equal to the authenticated user details
                spy.name = temp_user.name
                spy.sal = temp_user.sal
                spy.age = temp_user.age
                spy.rating = temp_user.rating
                start_chat(spy) #start with the menu
                break
            else:
                time.sleep(0.3)
                print colored("Incorrect Password!", "red")  # displaying incorrect password in red
                if counter - 1 == 0:  # for last try
                    print colored("You are out of tries!", "red")  # last try done printing it in red
                    time.sleep(0.3)
                    print "Closing Application!"
                    exit()
                else:
                    print "%d tries remaining!!" % (counter - 1)  # displayes no of tries remaining
            counter = counter - 1

    elif choice.upper() == 'N': #when new user
        time.sleep(0.3)
        print "SpyChat promises to be the best chat application."
        print "Our sign up is very easy and efficient!" #sign up started
        time.sleep(0.3)
        #asking for details and assigning them to spy details
        spy.name = raw_input("Kindly enter your name: ")
        spy.name = check_name(spy.name) #validity check
        time.sleep(0.3)
        spy.sal = raw_input("What should we call you? ")
        spy.sal = check_Sal(spy.sal) #validity check
        time.sleep(0.3)
        print "Hello! " + spy.sal + ". " + spy.name + ", Welcome to spy chat!"
        time.sleep(0.3)
        spy.age = input("Kindly enter your age: ")
        if check_age(spy.age): #checking for appropriate age
            spy.rating = input("How are you rated? ")
            #appropriate message for given rating of the spy
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
            print "Your username is : " + username #telling user about username
            time.sleep(0.3)
            #asking for password
            password_newUser = raw_input("Please Enter a password for your account(8-15chars): ")
            password_newUser = Valid_Password(password_newUser) #validity of password
            #creating a new user (object) of User(class) with details got in signup
            new_user = User(username,password_newUser,spy.name,spy.sal,spy.age,spy.rating)
            Users.append(new_user) #adding the new user to the users list
            #writing the new users details into users file using ab
            with open("users.csv", "ab") as users_data:
                writer = csv.writer(users_data)
                writer.writerow([new_user.username,new_user.password,spy.name,spy.sal,spy.age,spy.rating])
            start_chat(spy) #start with the menu

        else: #not correct age
            time.sleep(0.3)
            print "You are not of correct age!"
            exit()

    else: #wrong input
        time.sleep(0.3)
        print "Wrong input! "
        exit()
else:
    #closing application as the input provided was wrong
    time.sleep(0.3)
    print "Wrong Input!"
    print "Closing application!"
    time.sleep(0.7)
    exit()



