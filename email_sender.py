import smtplib
from email.mime.text import MIMEText

def send_email():
    sender_email = "ejohnlacsamana@gmail.com"
    sender_password = "icqg cqdm uake bsld"
    receiver_email = "ejohnlacsamana@outlook.com"
    body = "Test"
    message = MIMEText(body)
    message['Subject'] = "Today's Top Stories - Business Inquirer"
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

send_email()
