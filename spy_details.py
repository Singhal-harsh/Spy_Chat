from datetime import datetime
#a class having details of a spy
class Spy:
    def __init__(self,name,sal,age,rating):
        self.name = name
        self.sal = sal
        self.age = age
        self.rating = rating
        self.is0nline = True
        self.chats = []
        self.current_S_msg = None

#a class with details of a chat message
class Chat_msg:
    def __init__(self,message, sent_by_me):
        self.msg = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#creating a default spy
spy = Spy("Harsh", "Mr" , 18, 4.9)

#creating default friends of type Spy(Class)
friend1 = Spy("Anushka", "Ms" , 25 , 4.8)
friend2 = Spy("Priyanka", "Ms", 27, 4.7)
friend3 = Spy("Deepika", "Ms", 28 , 4.9)

#adding friends to the list
friends = []
friends.append(friend1)
friends.append(friend2)
friends.append(friend3)

