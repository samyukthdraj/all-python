# Automated birthday wisher, incomplete because we'd need an email with two factor authentication to enable the password in hash.
# 
import smtplib
import datetime as dt
import random
my_mail = "edusmart500@gmail.com"
my_pass = "12345"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open ("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection: #Simple Mail Transfer Protocol is used for the connection.
        connection.starttls() #tls makes the connection more secure.
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs="samyukthterawe@gmail.com", msg="Subject: Hello\n\n This is the body of the email.")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrow()}



