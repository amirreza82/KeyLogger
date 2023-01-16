import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("pythonrezaie@gmail.com", "sgrowwyberbpnitp")
message = "the message"
To = ["82rezaeei@gmail.com"]
s.sendmail("82amirrezarezaeei@gmail.com", To, message)
s.quit()
