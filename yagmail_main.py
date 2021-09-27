import yagmail

yag = yagmail.SMTP(user='cbdfjdbfgescyefg@gmail.com',password='qkktfpfjpgpvdndd')
msg='''
    Heyy,
        This email is sent via yagmail.
        There is an image attached.
                                -regards
'''
yag.send(to=['yhv.142@gmail.com','prasad@atomicloops.com'], subject='Testing Yagmail', contents=msg, attachments=['img1.jpg']
)
print('DOne')
