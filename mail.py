import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("sender mail id", "password") 
# message to be sent 
message = "Hey Developer, you make it and IT WORKS. "
# sending the mail 
s.sendmail("sender mail id", "recevier mail id", message) 
# terminating the session 
s.quit()
