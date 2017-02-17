##### This is a email sending function
##### !!Please make sure the SMTP service is up or authentication will be failed!! #####

def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    import smtplib
    """this is some test documentation in the function"""
    message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP(host=SERVER,port=25)
    # "New part"
    server.starttls()
    username = 'taoma@huajingsec.com'
    password = 'Huajingsec@2017'
    password = 'Matao_2012'
    server.login(username, password)
    server.sendmail(FROM, TO, message)
    server.quit()

sendMail('taoma@huajingsec.com','taoma@huajingsec.com','TEST','This is a test!','mail.huajingsec.com')

print("Email Sent!")

