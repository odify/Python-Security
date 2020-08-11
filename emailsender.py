import smtplib




to=input("enter receiver email")
content=input("enter message for email")
sender=input("enter sender email")
pwd=input("enter password")


def email(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(sender,pwd)
    server.sendmail(sender,to,content)
    server.close()


email(to,content)
