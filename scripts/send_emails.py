import smtplib, ssl
from datetime import datetime


def send_emails(message):
    port = 465  # For SSL
    password = "********"
    sender_email = "gimel1987dev@gmail.com"
    receiver_email1 = "amitroth@gmail.com"
    receiver_email2 = "itayelia45@gmail.com"


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email1, message)
        server.sendmail(sender_email, receiver_email2, message)
        print(message)




