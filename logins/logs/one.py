from smtplib import SMTP

def emailsent(otp,b):
    server=SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
    i=input("enter your mail id=")
    p=input("enter your mail id password=")
    try:
        server.login(i,p)
    except:
        print("WRONG PASSWORD")

    aa=b
    sent_from=i
    to=[aa]
    subject="otp"
    body=otp

    email_text="""
    From:%s
    To:%s
    subject:%s
    %s"""%(sent_from,','.join(to),subject,body)
    server.sendmail(sent_from,to,email_text)

    print("Email sent  SUCCESFULLY")

    server.quit()
