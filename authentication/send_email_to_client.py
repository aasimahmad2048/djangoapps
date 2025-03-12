 
from django.core.mail import send_mail
from django.conf import settings


class Send_mail_to_client:
    

    def  send(subject,email_body ,sender,recipient):
        

        send_mail(
            subject,
        email_body, 
        settings.EMAIL_HOST_USER,
        ((recipient,)), 

        fail_silently=False,
        )