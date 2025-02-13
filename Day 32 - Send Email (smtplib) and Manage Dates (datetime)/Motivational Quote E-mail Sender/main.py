"""
Lecture Notes: What is SMPT (Simple Mail Transfer Protocol)
- rules for how e-mails are received and passed over by mail servers, and how they are sent across the internet
- imagine mail services as post offices, and a personal computer as a mail box
    - SMPT is the postman who knows how to handle the e-mail, and transports it from office to office, until it is in a mailbox
- The smptlib library allows us to send our e-mail to any address on the internet
- connection.starttls()
    - tls stands for transport layer security
    - secures the connection to our e-mail server, encrypts message
- requires a specific app password to work, ordinary e-mail password will not do

"""


import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

quote_list = []
quotes = open('quotes.txt', 'r')
for line in quotes:
    quote_list.append(line.strip())

if day_of_week == 3: #send e-mail if it is Thursday
    my_email = input("Enter your e-mail address: ")
    app_password = input("Enter your password: ")
    to_email = input("Enter e-mail address of the receiver: ")
    quote = random.choice(quote_list)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls() #secures connection
        connection.login(my_email, app_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Hello!\n\n{quote}")

