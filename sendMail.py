import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from writeAndReadMethods import *

smtp_server = 'smtp.gmail.com'
smtp_port = 587
from_email = 'emailme.po@gmail.com'
password = 'tzep izyb nvhi ryla '

load_dotenv()
MONGODB_URI = os.environ.get(
    'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
client = MongoClient(MONGODB_URI)
db = client['Emailme']
cursor = db['infos']


def SendMail(Name, Email, content):
    to_email = Email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = Name + ' Daily email'
    Body = content
    msg.attach(MIMEText(Body, 'plain', 'utf-8'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(from_email, password)

        server.send_message(msg)
        print('Email sent successfully')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        server.quit()


if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': [],
        'dbLang': []
    }

    Main(dbDict, cursor)

    for i in range(Count(cursor)):
        SendMail(dbDict['dbNames'][i], dbDict['dbEmails'][i], getQuestion(dbDict['dbLang'][i]))
