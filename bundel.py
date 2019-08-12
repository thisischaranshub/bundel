import pymysql
import os

username = "root"
password = ''
host = "localhost"
database = "bundel"

conn = pymysql.connect(host,username,password,database)
cur = conn.cursor()

response = input('''
        1.sign up
        2.Log in
    ''')
if response == "1":
    print("register to login")

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    Conformyourpassword = input("Re-enter your password: ")
    Mobilenumber = input("enter your mobile number: ")
    Emailid = input("Enter your email-id: ")
    query = "INSERT INTO sign_up values('%s','%s','%s','%s','%s')"%(username,password,Conformyourpassword,Mobilenumber,Emailid)
    cur.execute(query)
    conn.commit()
    print("values inserted successfully")
elif  response == "2":
    username = input("enter your username: ")
    password = input("enter your password: ")

    print("welcome bibliophile")

    query = "select*FROM sign_up"

    cur.execute(query)

    data = cur.fetchall()

    for i in data:
        if username == str(i[0]) and password == str(i[1]):
            print("you are logged in!....")
        conn.commit( )

response = input("""
                    1.Love stories
                    2.History
                    3.Technology
                    4.Horror
                    5.Mythological
                    """)

if response == "1":
        print("here are you go...!!!!come fall in  love ")
        try:
            con = pymysql.connect('localhost', 'root', '', 'bundel')
            import math, random
            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP
            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                           enter a valid OTP
                            TRY AGAIN......""")
                exit()
                cur = con.cursor()
            cur.execute("select * from love_stories")

            love_stories = cur.fetchall()
            print(love_stories[0])
            for i in love_stories:


                print(i)
                file = open('destination/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])

        except Exception as e:
            print(e)
elif response == "2":
        print("here you goo..!!!!!feel how ur ansistors struggeled and enjoed their freedom")
        try:
            con = pymysql.connect('localhost', 'root', '', 'bundel')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")

            cur = con.cursor()
            print("test")
            cur.execute("select * from history")

            history = cur.fetchall()
            print(history[0])
            for i in history:


                print(i)
                file = open('destination/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

elif response == "3":
        print("here you goo.....!!!!!explore the world to know how far it went without informing you")
        try:
            con = pymysql.connect('localhost', 'root', '', 'bundel')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")

            cur = con.cursor()
            print("test")
            cur.execute("select * from technology")

            history = cur.fetchall()
            print(history[0])
            for i in history:


                print(i)
                file = open('destination/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

elif response == "4":
        print("here you goo.......!!!!!experience the goosboms stay courage ")
        try:
            con = pymysql.connect('localhost', 'root', '', 'bundel')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")
                exit()
            cur = con.cursor()
            print("test")
            cur.execute("select * from horror")

            horror = cur.fetchall()
            print(horror[0])
            for i in horror:


                print(i)
                file = open('destination/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

elif response == "5":
        print("here you  gooo.....!!!!!feel the the myth ")
        try:
            con = pymysql.connect('localhost', 'root', '', 'bundel')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")
                exit()
            cur = con.cursor()
            print("test")
            cur.execute("select * from mythological")

            mythological = cur.fetchall()
            print(mythological[0])
            for i in mythological:

                print(i)
                file = open('destination/' + i[0] +"."+i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

else:
        print("invalid selection")

response = input("""
                 1.explore more catogiries 
                 2.singout
                  """)

if response == "1":
    print("explore for more catogiries re-login")
elif response == "2":
    print("ur singned out")
    files = os.listdir('destination')

    print(files)

    print(type(files))

    for i in range(len(files)):
        os.remove('destination/' + files[i])
        exit()
else:
    print("invalid selection")
    exit()
