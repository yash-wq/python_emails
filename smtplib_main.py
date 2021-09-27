import os
import smtplib
import imghdr
from email.message import EmailMessage

def send_mail(reciever):

    EMAIL_ADDRESS = "cbdfjdbfgescyefg@gmail.com"
    EMAIL_pass = "qkktfpfjpgpvdndd"

    msg = EmailMessage()
    msg['Subject'] = '''SMTPLIB email'''
    msg['From'] = "Yash"
    msg['To'] = reciever
    msg.set_content('''
    Heyy,
    This email is sent via smtplib.
    An image is attached.
                -regards
    ''')

    with open('img1.jpg', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data,maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_pass)
        smtp.send_message(msg)

    print("Done")

send_mail('yhv.142@gmail.com')