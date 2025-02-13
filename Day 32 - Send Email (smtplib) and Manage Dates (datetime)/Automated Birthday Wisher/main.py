##################### Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv('birthdays.csv')

birthday_month = data['month']
birthday_day = data['day']
data_row = data['name']

#new dictionary to handle dates
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#does a birthday match todays date
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    #replace name in textfile with the real name
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = input("Enter your e-mail address: ")
        app_password = input("Enter your password: ")
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}")
        connection.close()




