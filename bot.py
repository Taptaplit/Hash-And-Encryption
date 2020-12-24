import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

github_url = str("https://github.com/Taptaplit/email-bot")

name = str(input("\nWhat is your name: "))
from_email = str(input("\nYour Email: "))
send_to = str(input("\nEmail of who you want to send it to: "))
subject = str(input("\nWhat do you want the subject to be? "))
msg = str(input(f"\nMessage you want to send to {send_to}: "))

server.login('EMAIL', 'EMAIL-PASS')
server.sendmail(f'{from_email}',
                f'{send_to}',
                f'Subject: {subject}\n\nFrom: {name} | {name}`s Email: {from_email}\nMessage: {msg}\n\n Sent with: {github_url}\n **Note this is a bot, and they will not be reciving any replys from this conversation, so email them back on their own email!'
                )
