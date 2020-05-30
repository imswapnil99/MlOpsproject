import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("swapnilkhairnar.78@gmail.com", "SHkhairnar1178") 
# message to be sent 
message = "Hey Developer, Finally we got the model trained. "
# sending the mail 
s.sendmail("swapnilkhairnar.78@gmail.com", "swapnilkhairnar.78@gmail.com", message) 
# terminating the session 
s.quit()
