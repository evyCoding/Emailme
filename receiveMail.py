import imaplib
import email
from email.header import decode_header
from writeAndReadMethods import *

# Establish connection to the IMAP server
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# Login to the server
imap.login("emailme.po@gmail.com", "tzep izyb nvhi ryla")

# Select the mailbox you want to check (inbox in this case)
imap.select("inbox")

# Search for all emails in the selected mailbox
status, messages = imap.search(None, "ALL")
email_ids = messages[0].split()
email_ids.reverse()

# load the env variables
load_dotenv()
# set up the connection
MONGO_URI = os.environ.get(
    'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
# select the database
Client = MongoClient(MONGO_URI)
# select the collection
db = Client['Emailme']
# select document
cursor = db['infos']


def get_decoded_header(header_value):
    """Decode email header to a human-readable format."""
    decoded_header = decode_header(header_value)[0][0]
    if isinstance(decoded_header, bytes):
        decoded_header = decoded_header.decode()
    return decoded_header


def getEmails(user, answer):
    """Fetch emails from the inbox and filter by user in subject."""
    for email_id in email_ids:
        status, msg_data = imap.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = get_decoded_header(msg["subject"])
                if (user + " Daily email").upper() in subject.upper() or (
                        'Re: ' + user + "Daily email").upper() in subject.upper():
                    # Conditions related to printing the body of the mail.
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                answer.append(body)
                    else:
                        if msg.get_content_type() == "text/plain":
                            body = msg.get_payload(decode=True).decode()
                            answer.append(body)


if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': []
    }

    Main(dbDict, cursor)

    for i in range(Count(cursor)):
        getEmails(dbDict['dbNames'][i], dbDict['dbAnswers'])

    for Value in dbDict['dbAnswers']:
        print(Value)

    for i in range(Count(cursor)):
        UpdateAnswers(dbDict['dbIds'][i], dbDict['dbAnswers'][i], cursor)


imap.logout()
