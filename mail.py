import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("swapnilkhairnar.78@gmail.com", "SHkhairnar1178") 
# message to be sent 
message = "Hey Developer, you make it and IT WORKS. "
# sending the mail 
s.sendmail("swapnilkhairnar.78@gmail.com", "swapnilkhairnar.78@gmail.com", message) 
# terminating the session 
s.quit()
