from datetime import datetime
class Spy:
    def __init__(self,name,sal,age,rating):
        self.name = name
        self.sal = sal
        self.age = age
        self.rating = rating
        self.is0nline = True
        self.chats = []
        self.current_S_msg = None

class Chat_msg:
    def __init__(self,message, sent_by_me):
        self.msg = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy("Harsh", "Mr" , 18, 4.9)

friend1 = Spy("Srk", "Mr" , 49 , 4.8)
friend2 = Spy("Nanda", "Ms", 19, 4.7)
friend3 = Spy("Rk", "Mr", 28 , 4.9)

friends = []
friends.append(friend1)
friends.append(friend2)
friends.append(friend3)

