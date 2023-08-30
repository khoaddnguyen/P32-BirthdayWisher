from datetime import datetime
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText

SUBJECT = "Happy Birthday!"
BODY = "This is the body"
SENDER_EMAIL = "aaa@gmail.com"
RECIPIENT_EMAIL = ["bbb@yahoo.com"]
PASSWORD = "password"  # security application password, not account password

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# compare and see if today's month/day tuple matches one of the keys in birthday_dict
if (today_tuple) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    def send_email(SUBJECT, contents, SENDER_EMAIL, RECIPIENT_EMAIL, PASSWORD):
        msg = MIMEText(contents)
        msg["Subject"] = SUBJECT
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(RECIPIENT_EMAIL)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
           smtp_server.login(SENDER_EMAIL, PASSWORD)
           smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Message sent!")


    send_email(SUBJECT, contents, SENDER_EMAIL, RECIPIENT_EMAIL, PASSWORD)





