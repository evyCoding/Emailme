import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
from_email = 'emailme.po@gmail.com'
password = 'tzep izyb nvhi ryla '
to_email = 'forcontact.we@gmail.com'


msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'Test Emailme'
body = 'This is a test email sent from Python'

try:
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection with TLS

    # Login to the server
    server.login(from_email, password)

    # Send the email
    server.send_message(msg)
    print('Email sent successfully')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Close the server connection
    server.quit()
