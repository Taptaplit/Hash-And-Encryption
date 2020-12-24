import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

github_url = str("https://github.com/Taptaplit/email-bot")

name = str(input("\nWhat is your name: "))
from_email = str(input("\nYour Email: "))
send_to = str(input("\nEmail of who you want to send it to: "))
msg = str(input(f"\nMessage you want to send to {send_to}: "))

server.login('EMAIL', 'EMAIL-PASS')
server.sendmail(f'{from_email}',
                f'{send_to}',
                f'\nFrom: {name},{from_email}\nMessage: {msg}\n\n Sent with: {github_url}\n '
                )
