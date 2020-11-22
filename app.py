from flask import Flask , render_template , request , redirect , session
import os
import sys

app = Flask(__name__)
app.secret_key = 'secret'


class User():
    def __init__(self , id , username , password):
        self.id = id 
        self.username = username
        self.password = password
    def __repr__(self):
        return f'username: {self.username} , password: {self.password} , id: {self.id}' 


users = []

users.append(User(id =1 , username = 'Aghilas' , password = '1'))

users.append(User(id =2 , username = 'Admin' , password = '2'))
print(users)
print(users[1].username)

user_string = str(users)
file = open('file.txt' , 'w')
file.write(user_string)
file.close()


def iExit():
    sys.clear()
    exit()

#====================home=====================

@app.route('/')
def home():
    return render_template('/home.html')











#====================================Register=============================
@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST' :
        try:

            Username_register = request.form['Username_register']
            Password_register = request.form['Password_register']
            #user_string = str(users)
            file = open('file.txt' , 'r')
            #file.write(user_string)

            r = file.readline()

            if Username_register in r:
                return 'Username Is Already Used'
                file.close()
            else:
                users.append(User(id =0 , username = Username_register , password = Password_register))
                user_string = str(users)
                file = open('file.txt' , 'w')
                file.write(user_string)
                file.write(' ')
                file.close()

            


            # try:
            #     # i = 0
            #     # j = len(users) + 2
                    
            #     while True:

            # if Username_register  in   users.username:
            #     return 'Username Is Already Used'
            
            # else:   

            #     users.append(User(id =0 , username = Username_register , password = Password_register))
            #     print('aaaaaaaaaaaaaa')
                




                    # else:
                    #     users.append(User(id =0 , username = Username_register , password = Password_register))
                    #     i = j
                    #     print('#############################')
                    #     i = j 
            #         #     break
            # except:
            #     return 'Error'





            # user_string = str(users)
            # file = open('file.txt' , 'w')
            # file.write(user_string)
            # file.write(' ')
            # file.close()







            try:


                i = 0
                j = len(users) + 1
            
                while i < j :
                        #try:
                    if Username_register in users[i].username and Password_register in users[i].password:
                                return render_template('register_confirme.html' , username = Username_register , password = Password_register)



                        # elif i == 0:
                        #     i += 1
                        # #     return  'OK Login Success   ===>    Your Username Is : {}  and Your Password Is : {} '.format(users[i].username , users[i].password )

                    #elif  Username_register not in users[i].username and Password not in users[i].password :
                               #i +=  1

                    else:
                        i += 1
                        #return 'Your Are Not Login  : {}'.format(users)
                        #         i = j
                        # except:
                        #     return 'our Are Not Login : {}'.format(users)
                        #     i = j
            except:
                return 'Registred Faild .... Try Again'





        except:
            return ' Error !' 

        file = open('file.txt' , 'r')
        r = file.readline()
        return r
        file.close()

    elif request.method == 'GET':
        return render_template('register.html')

    else:
        return 'Method Not Allowed'









































#======================Login======================================
@app.route('/login' , methods = ['POST' , 'GET'] )
def login():

    if request.method == 'POST' :
        session.pop('user_id' , None)
        
        Username = request.form['username']
        Password = request.form['password']


        i = 0
        j = len(users) + 1
    
        while i < j :
                try:
                    if users[i].username == Username and users[i].password == Password:
                        #return  'OK Login Success   ===>    Your Username Is : {}  and Your Password Is :   {} ====> <a href="/profil"> Clic Here To Redirect To Your profil</a>'.format(users[i].username , users[i].password ) 
                        #os.sleep(2)
                        return render_template('profil.html' , Username = users[i].username , Password = users[i].password  , users = users)
                        break
                # elif i == 0:
                #     i += 1
                #     return  'OK Login Success   ===>    Your Username Is : {}  and Your Password Is : {} '.format(users[i].username , users[i].password )

                    #elif users[i].username != Username and users[i].password != Password:
                        #i +=  1

                    else:
                        i +=  1
                        #return 'Username Or Password Incorrect :   {}'.format(users)
                        #i = j
                except:
                    return 'Username Or Password Incorrect :   {}'.format(users)
                    i = j



    elif request.method == 'GET':
        return render_template('login.html')

    else:
        return '<h1>Method Not Allowed</h1>'


#===================================================Profil==================================


@app.route('/profil')
def profil():

    return render_template('profil.html')




#============================================================================================



app.run(debug = True)