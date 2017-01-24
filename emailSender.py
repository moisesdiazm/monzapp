
import smtplib

gmail_user = 'modim95@gmail.com'
gmail_pwd = 'dImm6oi737.dIaz'


class Email:

    def send_email(self,to_email):
        self.smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        self.smtpserver.ehlo()
        self.smtpserver.starttls()
        self.smtpserver.ehlo()
        self.smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to_email + '\n' + 'From: ' + "Caseta 1" + '\n' + 'Subject: Correspondencia Disponible \n'
        msg = header + '\n Pase a recoger su correspondencia a la caseta 1.  \n\n'
        self.smtpserver.sendmail(gmail_user, to_email, msg)
        print("email sended>> {} / {}".format(header, msg))
        self.smtpserver.close()

