from spy_details import Spy
#user class inheriting from spy class as all details are almost same apart from username and password
class User(Spy):
    def __init__(self,username,password,name,sal,age,rating):
        Spy.__init__(self,name,sal,age,rating)
        self.username = username
        self.password = password

#creating three default users
user1 = User("Amitabh@SpyChat","BigB1234","Amitabh","Mr",49,5.0)
user2 = User("Shahrukh@SpyChat","Srk2Novber","Shahrukh","Mr",48,4.9)
user3 = User("Amir@SpyChat","SecretSuperstar","Amir","Mr",48,4.9)

#adding them to a list
Users = []
Users.append(user1)
Users.append(user2)
Users.append(user3)