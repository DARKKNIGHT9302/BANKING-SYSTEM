import csv
import time
import random

def random_num():
    global r1
    r1 = random.randint(123456789123,321987654321)

def acc_num():
    with open('acc_num.csv','a',newline='') as k:
        writer2 = csv.writer(k,delimiter=',')
        with open('acc_num.csv','r') as f:
            reader2 = csv.reader(f,delimiter=',')
            rownum2 = 0
            for row2 in reader2:        
                if row2 == [r1]:
                    rownum2 = rownum2+1
                else:
                    continue
            if rownum2 == 1:
                random_num()
            else:
                writer2.writerow([r1])
                with open(username+'_customer.csv','a',newline='') as m:
                    writer3 = csv.writer(m,delimiter=':')
                    writer3.writerow([r1])
                    writer3.writerow(["Your UserName Is  ",username])
                    writer3.writerow(["Your Password Is  ",password])
                    writer3.writerow(["Your Address Is  ",address])

                with open(username+'_employee.csv','a',newline='') as n:
                    writer4 = csv.writer(n,delimiter=':')
                    writer4.writerow([r1])
                    writer4.writerow(["UserName  ",username])
                    writer4.writerow(["Address  ",address])

                acc_num_file()

def acc_num_file():
    with open(str(r1)+'.csv','a',newline='') as l:
        writer5 = csv.writer(l,delimiter=',')
        first_money = input("How much money do you want to add for the first time? (in ₹) : ")
        writer5.writerow([first_money])

def register():
    global username
    global password
    global address
    with open('users.csv','a',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        username = input("Create Username : ")
        password = input('Create Password : ')
        passwordc= input('Confirm Password : ')
        with open('users.csv','r') as f:
            reader = csv.reader(f,delimiter=',')
            rownum = 0
            for row in reader:        
                if row == [username, password]:
                    rownum = rownum+1
                else:
                    continue

            if rownum == 1:                               
                acc_exist()
                if inp == '1' or inp == 'login' or inp == 'Login' or inp == 'LOGIN':
                    login()
                elif inp == '2' or inp == 'new' or inp == 'New' or inp == 'NEW':
                    register()
                elif inp == '3' or inp == 'b' or inp == 'B' or inp == 'back' or inp == 'Back' or inp == 'BACK':
                    user_employee()
                else:
                    print("INVALID INPUT")
                    print("Please choose correct options....")
                    print('.................................')
                    time.sleep(2)
                    acc_exist()

            else:
                if password == passwordc:
                    address = input("Enter Your Adderess : ")
                    random_num()
                    acc_num()
                    writer.writerow([username,password])
                    print("Your Registration is Succesful!!")
                else:
                    print("Passwords don't match")
                    print("TRY AGAIN !!")
                    print('.................................')
                    register()

def login():
    usernamelog = input("Enter Your Username : ")
    passwordlog = input("Enter Your Password : ")
    with open('users.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        rownum = 0
        for row in reader:        
            if row == [usernamelog, passwordlog]:
                rownum = rownum+1
            else:
                continue
        if rownum == 1:                               
            print("Login Successfully")
        else:
            print("Incorrect Username or Password")
            print("Try one more Time....")
            print('.................................')
            usernamelog = input("Enter Your Username : ")
            passwordlog = input("Enter Your Password : ")
            with open('users.csv','r') as f:
                reader = csv.reader(f,delimiter=',')
                rownum = 0
                for row in reader:        
                    if row == [usernamelog, passwordlog]:
                        rownum = rownum+1
                    else:
                        continue

                if rownum == 1:                               
                    print("Login Successfully")
                else:
                    print("Incorrect Username or Password")

def acc_exist():
    global inp
    print("Account Already Exists!")
    time.sleep(1)
    print('.................................')
    time.sleep(1)
    print("Do you wanna login? Or wanna create a new Account? Or wanna go back?")
    print("1. login\n2. new\n3. back")
    inp = input("Choose : ")

def user_employee():
    global choose
    print("Choose your Occupation : \n--> 1. Customer\n--> 2. Employee")
    choose = input("Choose : ")
    if choose == '2' or choose == 'Employee' or choose == 'employee' or choose == 'EMPLOYEE':
        employee_login()
    elif choose == '1' or choose == 'Customer' or choose == 'customer' or choose == 'CUSTOMER':
        old_new_user()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        time.sleep(1)
        print("Please choose correct options....")
        print('.................................')
        time.sleep(1)
        user_employee()
    time.sleep(1)

def employee_login():
    global emp_name
    global emp_password
    a=0
    emp_name = input("Enter Your Name : ")
    emp_password = input("Enter Your Password : ")
    with open('employee_list.csv','r') as f:
        reader2 = csv.reader(f,delimiter=',')
        rownum2 = 0
        for row2 in reader2:        
            if row2 == [emp_name, emp_password]:
                rownum2 = rownum2+1
            else:
                continue
        if rownum2 == 1:
            print("Welcome Mr./Mrs. ",emp_name)
            print("Your Attendance has been recorded.")
            print('.................................')
            emp_work()
        else:
            print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
            a=a+1
            if a==1:
                print("Try Once more....")
                print("Remember that this is your last chance, So enter carefully...")
                print('.................................')
                emp_name = input("Enter Your Name : ")
                emp_password = input("Enter Your Password : ")
                with open('employee_list.csv','r') as f:
                    reader2 = csv.reader(f,delimiter=',')
                    rownum2 = 0
                    for row2 in reader2:        
                        if row2 == [emp_name, emp_password]:
                            rownum2 = rownum2+1
                        else:
                            continue
                    if rownum2 == 1:
                        print("Welcome Mr./Mrs. ",emp_name,"\nYour Attendece has been recorded.")
                        print('.................................')
                        emp_work()
                    else:
                        print(f"Name --> {emp_name} with Password --> {emp_password} doesn't exist.")
                        print("You are not an Employee of PCB !!")
                        print("Turn Off your computer before I call the Police!!")
                        print('.................................')

def emp_work():
    global emp_ask
    print(f"Mr./Mrs. {emp_name}, Choose your work :\n1. All Accounts \n2. Account Info \n3. back")
    emp_ask = input("Choose : ")
    if emp_ask == '1' or emp_ask == 'all accounts' or emp_ask == 'All Accounts' or emp_ask == 'ALL ACCOUNTS':
        emp_ask_1()
                
    elif emp_ask == 'b' or emp_ask == 'B' or emp_ask == 'back' or emp_ask == 'Back' or emp_ask == 'BACK':
        employee_login()

    else:
        emp_ask_2()

def emp_ask_1():
    if emp_ask == '1' or emp_ask == 'all accounts' or emp_ask == 'All Accounts' or emp_ask == 'ALL ACCOUNTS':
        with open('acc_num.csv','r') as f:
            cust_acc = csv.reader(f,delimiter='-')
            print("These are all Registered Accounts : ")
            for row in cust_acc:
                print(row)
            ask = input("Do you want to proceed to 'Account Info'? (yes /no /back) : ")
            if ask=='y'or ask=='Y' or ask=='yes'or ask=='Yes'or ask=='YES':
                emp_ask_2_1()
            elif ask=='n'or ask=='N' or ask=='no'or ask=='No'or ask=='NO':
                print("..")
                print("Thanks for using this system.!")
                print("Your work details has been Recorded and will be sent to Boss, Mr. SAURAV KUMAR")
            elif ask=='b'or ask=='B' or ask=='back'or ask=='Back'or ask=='BACK':
                print("Going back...")
                print("...")
                emp_work()
            else:
                print("INVALID INPUT\n...Try Again...")
                emp_ask_1()

def emp_ask_2():
    if emp_ask == '2' or emp_ask == 'account info' or emp_ask == 'Account Info' or emp_ask == 'ACCOUNT INFO' or emp_ask == 'Account info':
        ask_username = input("Enter Customer Username : ")
        ask_acc_num = input("Enter Account Number : ")
        with open('acc_num.csv','r') as f:
            reader5 = csv.reader(f,delimiter='-')
            rownum3 = 0
            for row3 in reader5:        
                if row3 == [ask_username,ask_acc_num]:
                    rownum3 = rownum3+1
                else:
                    continue
            if rownum3 == 1:
                with open(ask_username+'_employee.csv','r') as f:
                    reader6 = csv.reader(f,delimiter=',')
                    print(f"These are {ask_username}'s Information....")
                    for row1 in reader6:
                        print(row1)
                with open(ask_acc_num+'.csv','r') as g:
                    reader7 = csv.reader(g,delimiter=',')
                    for row2 in reader7:
                        print(f"current Balance : ₹{row2}")
            else:
                print("---->>>>  ERROR!!!  <<<<----")
                print(f"Usename -- {ask_username} and Account number -- {ask_acc_num} Doesn't Exists!\n....")
                a=0
                while True:
                    ent = input("1. Try again\n2. Back\nYour Choise? : ")
                    if ent == '2' or ent == 'b' or ent == 'B' or ent == 'back' or ent == 'Back' or ent == 'BACK':
                        emp_work()
                    elif ent == '1' or ent == 't' or ent == 'T' or ent == 'try again' or ent == 'Try again' or ent == 'Try Again' or ent == 'TRY AGAIN':
                        emp_ask_2()
                    else:
                        print("INVALID INPUT\n...\nTry Again\n....")
                        a=a+1
                        if a==2:
                            print("No!! No more chances!")
                            break
    else:
        print("INVALID INPUT\n...Try Again...\n...\n....")
        emp_work()

def emp_ask_2_1():
    ask_username = input("Enter Customer Username : ")
    ask_acc_num = input("Enter Account Number : ")
    with open('acc_num.csv','r') as f:
        reader5 = csv.reader(f,delimiter='-')
        rownum3 = 0
        for row3 in reader5:        
            if row3 == [ask_username,ask_acc_num]:
                rownum3 = rownum3+1
            else:
                continue
        if rownum3 == 1:
            with open(ask_username+'_employee.csv','r') as f:
                reader6 = csv.reader(f,delimiter=',')
                print(f"These are {ask_username}'s Information....")
                for row1 in reader6:
                    print(row1)
            with open(ask_acc_num+'.csv','r') as g:
                reader7 = csv.reader(g,delimiter=',')
                for row2 in reader7:
                    print(f"current Balance : ₹{row2}")
        else:
            print("---->>>>  ERROR!!!  <<<<----")
            print(f"Usename -- {ask_username} and Account number -- {ask_acc_num} Doesn't Exists!\n....")
            a=0
            while True:
                ent = input("1. Try again\n2. Back\nYour Choise? : ")
                if ent == '2' or ent == 'b' or ent == 'B' or ent == 'back' or ent == 'Back' or ent == 'BACK':
                    emp_work()
                elif ent == '1' or ent == 't' or ent == 'T' or ent == 'try again' or ent == 'Try again' or ent == 'Try Again' or ent == 'TRY AGAIN':
                    emp_ask_2()
                else:
                    print("INVALID INPUT\n...\nTry Again\n....")
                    a=a+1
                    if a==2:
                        print("No!! No more chances!")
                        break

def old_new_user():
    global acc
    naam = input("Please Enter Your Good Name Sir : ")
    time.sleep(2)
    print(f"Hello Mr. {naam}, WELCOME in ...🏦D.A.V STUDENT BANK🏦...")
    time.sleep(2)
    acc = input("Do you have an account? (yes / no / Back / Home / Exit) : ")
    if acc == 'yes' or acc == 'Yes' or acc == 'YES' or acc == 'y' or acc == 'Y':
        acc_yes()
    elif acc == 'n' or acc == 'N' or acc == 'NO' or acc == 'no' or acc == 'No':
        acc_no()
    elif acc == 'BACK' or acc == 'Back' or acc == 'back' or acc == 'B' or acc == 'b':
        back_2()
    elif acc == 'HOME' or acc == 'Home' or acc == 'home' or acc == 'h' or acc == 'H':
        home()
    elif acc == 'EXIT' or acc == 'Exit' or acc == 'exit' or acc == 'e' or acc == 'E':
        exit()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        time.sleep(1)
        print("Please choose correct options....")
        print('.................................')
        time.sleep(1)
        back_3()
    time.sleep(1)

def acc_yes():
    global yes1
    yes1 = input("Do you want to login (yes / no / Back / Home / Exit):")
    if yes1 == 'yes' or yes1 == 'Yes' or yes1 == 'YES' or yes1 == 'y' or yes1 == 'Y':
        login_system_yes()
    elif yes1 == 'no' or yes1 == 'NO' or yes1 == 'No' or yes1 == 'n' or yes1 == 'N':
        login_system_no()
    elif yes1 == 'back' or yes1 == 'Back' or yes1 == 'BACK' or yes1 == 'b' or yes1 =='B':
        back_3()
    elif yes1 == 'home' or yes1 == 'Home' or yes1 == 'HOME' or yes1 == 'h' or yes1 =='H':
        home()
    elif yes1 == 'exit' or yes1 == 'Exit' or yes1 == 'EXIT' or yes1 == 'e' or yes1 =='E':
        exit()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        time.sleep(1)
        print("Please choose correct options....")
        print('.................................')
        time.sleep(1)
        acc_yes()
        time.sleep(1)

def login_system_yes():
    time.sleep(1)
    print("Fetching the Login System for you......")
    time.sleep(1)
    print("Please Wait......")
    time.sleep(1)
    login()

def login_system_no():
    print('.................................')
    time.sleep(1)
    print("...🙏THANK YOU FOR VISITING ...🏦D.A.V STUDENT BANK🏦...")
    time.sleep(1)
    print("HOPE TO SEE YOU AGAIN")
    print('.................................')
    time.sleep(5)
       
def acc_no():
    global yes2
    yes2 = input("Do you want to Register sir? (yes / no / Back / Home / Exit) : ")
    if yes2 == 'yes' or yes2 == 'Yes' or yes2 == 'YES' or yes2 == 'y' or yes2 == 'Y':
        register_system_yes()
    elif yes2 == 'NO' or yes2 == 'No' or yes2 == 'no' or yes2 == 'n' or yes2 == 'N':
         register_system_no()
    elif yes2 == 'back' or yes2 == 'Back' or yes2 == 'BACK' or yes2 == 'B' or yes2 == 'b':
        back_3()
    elif yes2 == 'HOME' or yes2 == 'Home' or yes2 == 'home' or yes2 == 'H' or yes2 == 'h':
        home()
    elif yes2 == 'EXIT' or yes2 == 'Exit' or yes2 == 'exit' or yes2 == 'E' or yes2 == 'e':
        exit()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        time.sleep(1)
        print("Please choose correct options....")
        print('.................................')
        time.sleep(1)
        acc_no()
    time.sleep(1)
        
def register_system_yes():
    time.sleep(2)
    print("Fetching the Customer Registration System for you......")
    time.sleep(1)
    print("Please Wait......")
    time.sleep(1)
    register()
    time.sleep(1)
    login_want()

def register_system_no():
    time.sleep(2)
    print('.................................')
    time.sleep(1)
    print("...🙏THANK YOU FOR VISITING ...🏦D.A.V STUDENT BANK🏦...")
    time.sleep(1)
    print("HOPE TO SEE YOU AGAIN")
    time.sleep(5)
   
def login_want():
    global olog
    olog = input("Do You Want To Login Now? (yes / no / Home / Exit) : ")
    if olog == 'yes' or olog == 'Yes' or olog == 'YES' or olog == 'Y' or olog == 'y':
        login_want_yes()
    elif olog == 'No' or olog == 'NO' or olog == 'no' or olog == 'N' or olog == 'n':
        login_want_no()
    elif olog == 'HOME' or olog == 'Home' or olog == 'home' or olog == 'h' or olog == 'H':
        home()
    elif olog == 'EXIT' or olog == 'Exit' or olog == 'exit' or olog == 'E' or olog == 'e':
        exit()
    else:
        time.sleep(2)
        print("INVALID INPUT")
        time.sleep(1)
        print("Please choose correct options....")
        time.sleep(1)
        print('.................................')
        time.sleep(1)
        login_want()

def login_want_yes():
        time.sleep(2)
        print("Fetching the Login System for you......")
        time.sleep(1)
        print("Please Wait......")
        time.sleep(1)
        login()

def login_want_no():
        time.sleep(2)
        print("Thanks for registering in ...🏦D.A.V STUDENT BANK🏦...")
        time.sleep(5)

def back_1():
    print('.................................')
    time.sleep(0.8)
    print('.................................')
    time.sleep(0.8)
    print('.................................')
    time.sleep(0.8)
    print("SORRY Mr.", emp_name ,"You Are Not An Employee of 🏦D.A.V STUDENT BANK🏦' '(DSB) ")
    time.sleep(3)
    user_employee()

def back_2():
    user_employee()

def back_3():
    acc = input("Do you have an account? (yes / no / Back / Home / Exit) : ")
    if acc == 'yes' or acc == 'Yes' or acc == 'YES' or acc == 'y' or acc == 'Y':
        acc_yes()
    elif acc == 'n' or acc == 'N' or acc == 'NO' or acc == 'no' or acc == 'No':
        acc_no()
    elif acc == 'BACK' or acc == 'Back' or acc == 'back' or acc == 'B' or acc == 'b':
        back_2()
    elif acc == 'HOME' or acc == 'Home' or acc == 'home' or acc == 'h' or acc == 'H':
        home()
    elif acc == 'EXIT' or acc == 'Exit' or acc == 'exit' or acc == 'e' or acc == 'E':
        exit()
    else:
        print("INVALID INPUT")
        print("Please choose correct options....")
        print('.................................')
        time.sleep(2)
        back_3()  

def exit():
    time.sleep(2)
    print("THANKS FOR VISITING ...🏦D.A.V STUDENT BANK🏦...")
    time.sleep(1)
    print("HOPE TO SEE YOU AGAIN")
    time.sleep(1)
    print('.................................')
    time.sleep(1)
    print('.................................')
    time.sleep(1)
    print('.................................')
    time.sleep(1) 
    print('.................................')
    time.sleep(1) 
    print('.................................')
    time.sleep(5)

def home():
    time.sleep(2)
    print("Redirecting to Home")
    time.sleep(1)
    user_employee()
    time.sleep(5)

user_employee()
