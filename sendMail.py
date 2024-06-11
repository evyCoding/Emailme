import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from writeAndReadMethods import *

# configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
from_email = 'emailme.po@gmail.com'
password = 'tzep izyb nvhi ryla '

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ.get(
    'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# db refers to the collection
db = client['Emailme']

# names refers to the infos in infos
cursor = db['infos']


def SendMail(Name, Email):
    to_email = Email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = Name + ' Daily email'
    Body = "What song gives you butterflies?"
    msg.attach(MIMEText(Body, 'plain'))
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


if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': []
    }

    Main(dbDict, cursor)

    for i in range(Count(cursor)):
        SendMail(dbDict['dbNames'][i], dbDict['dbEmails'][i])
