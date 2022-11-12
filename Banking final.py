
import mysql.connector
import menu


conn=mysql.connector.connect(user='root',password='1234',host='localhost')
cursor=conn.cursor()
cursor.execute("CREATE DATABASE qwertxy")
cursor.execute("USE qwertxy")


cursor = conn.cursor()



conn.autocommit= True


for menu in range (9):


    print()
    print('1.ACCOUNTS')
    print()
    print('2.Credit/Debit')
    print()
    print('3.Customer Details')
    print()
    print('4.Delete Account')
    print()
    print('5.Exit')
    print()


    n=int(input("Enter Your Choice :"))
    print()


    
    if n==1:
        print("1.New Account")
        print()
        print("2.Login")
        print()
        x=int(input("Enter Your Choice :"))
        print()
        if x==1:
            cursor.execute("CREATE TABLE if not exists accounts(acc_no int(100),Name varchar(20),password int(20),user_name char (20),amount float(20),age int(10),gender char(10) ,address char(20),pincode int(20))")        
            acc_no=input("Enter Your Account No.: ")
            print()
            Name=input("Enter Your Name : ")
            print()
            password=input("Enter Your 4 Digit no. Password : ")
            print()
            user_name=input("Enter Your User Name : ")
            print()
            age=input("Enter Your Age : ")
            print()
            gender=input("Enter Your Gender (M/F) : ")
            print()
            amount=input("Enter Amount to be deposit : ")
            print()
            address=input("Enter Your Address : ")
            print()
            pincode=input("Enter Your Pincode : ")
            print()
            query="insert into accounts(acc_no,Name,password,user_name,amount,age,gender,address,pincode)values ({},'{}',{},'{}',{},{},'{}','{}',{})".format(acc_no,Name,password,user_name,amount,age,gender,address,pincode)
            cursor.execute(query)
            conn.commit()
            print()
            print('Accout Creation Successful')
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    
        elif x==2:
            user_name=input("Enter Your User Name: ")
            print()
            password=int(input("Enter Your Password: "))
            print()
            query="SELECT * FROM accounts WHERE user_name ='%s'" % (user_name)
            query= "SELECT * FROM accounts WHERE password =%d "%(password)
        
            cursor.execute(query)
            print()
            data=cursor.fetchone()
            print(data)
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    


    elif n==2:

        print()
        acc_no=int(input("Enter the Account no : "))
        print()
        query="SELECT * FROM accounts  WHERE acc_no=%d"%(acc_no)
        cursor.execute(query)
        data=cursor.fetchone()[4]
        print("Amount in Account: ",data)
        print()


        print('1.CREDIT')
        print()
        print('2.DEBIT')
        print()

        m=int(input("Enter Your Choice : "))
        print()

        if m==1:
            print()
            balance=float(input("Enter The Amount : "))
            print()
            x=balance+data
            print("Amount in Account",x)
            query2="UPDATE accounts SET amount=%d  where acc_no='%s'"%(x,acc_no)
            cursor.execute(query2)
            print()
            print("Amount Credited Successfully")
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        if m==2:
            print()
            balance=float(input("Enter The Amount : "))
            print()
            y=data-balance
            print()
            query2="UPDATE accounts SET amount=%d  where acc_no='%s'"%(y,acc_no)
            cursor.execute(query2)
            print()
            print("Amount in Account",y)
            print()
            print("Amount Debited Succesfully")
            print()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    
    elif n==3:

        x=int(input("Enter The ADMIN Code: "))
        print()
        code=897213
        if x==code:
            print()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM accounts")
            data=cursor.fetchall()
            count=cursor.rowcount
            print()
            for row in data:
                print(row)
                print()
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        else:
            print("Invalid")
            print()
    elif n==4:  
       print()
       acc_no=int(input("Enter The Accoun no : "))
       password=input("Enter The Password : ")
   
       query="DELETE FROM accounts where acc_no=%d"%(acc_no)
       x=input("Are You Sure You Want To Close Your Account? (Y/N) : ")
       cursor.execute(query)
       print()
       print("Your Account Has Been Closed")
       print()
       print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

else:
    print()
    import menu

    




















            
