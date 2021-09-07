from email.mime.text import MIMEText
import smtplib

def send_mail(email, height, avg_height, count):
    from_email="myfakeemail@fake.com"
    from_password="fakepassword"
    to_email=email

    subject="height data"
    message="your height is %s, average height of %s entries is %s." % (height, count, avg_height)
    print(message)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    #gmail.ehlo()
    #gmail.starttls()
    #gmail.login(from_email, from_password)
    #gmail.sendmail(msg)


