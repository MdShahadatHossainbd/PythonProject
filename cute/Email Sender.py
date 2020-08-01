import smtplib

to = input("Enter the email of recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shahadat@gmail.com','123456')
    server.sendmail('shahadat@gamil.com', to, content)
    server.close()

sendEmail(to, content)