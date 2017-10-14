import time
from smtplib import*
#
#
# def main():
#     emails = ['testmpr@mail.ru', 'testmprtv@gmail.com']
#     for mail in emails:
#         send_email(mail)
#     time.sleep(60)
#     for mail in emails:
#         recieve_email(mail)

def send_email(mail):
    username = 'zabbix@m-pr.tv'
    user_pass = '565ts89%w()32'
    server = SMTP('mail.m-pr.tv')
    server.starttls()
    server.login(username, user_pass)
    server.sendmail(username, mail, 'it\'s work!')
    server.quit()

# def recieve_email(mail):
#     pass

send_email('testmpr@mail.ru')

