import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('yourEmailUsername', 'yourEmailPassword')
message = 'Hi, \nPython is awesome. :)\nThanks.'
server.sendmail("from.email@gmail.com", "to.email@example.com", message)
