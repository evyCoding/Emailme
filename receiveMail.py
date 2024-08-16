import imaplib
import email
from email.header import decode_header
from writeAndReadMethods import *


imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("test@gmail.com", "password")
imap.select("inbox")


status, messages = imap.search(None, "ALL")
email_ids = messages[0].split()
email_ids.reverse()

load_dotenv()
MONGO_URI = os.environ.get(
    'link to the database')
Client = MongoClient(MONGO_URI)
db = Client['Emailme']
cursor = db['infos']


def get_decoded_header(header_value):
    """Decode email header to a human-readable format."""
    decoded_header = decode_header(header_value)[0][0]
    if isinstance(decoded_header, bytes):
        decoded_header = decoded_header.decode()
    return decoded_header


def getEmails(user, answer, i):
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
                                answer[i] += body
                    else:
                        if msg.get_content_type() == "text/plain":
                            body = msg.get_payload(decode=True).decode()
                            answer[i] += body


if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': []
    }

    Main(dbDict, cursor)
    for i in range(Count(cursor)):
        getEmails(dbDict['dbNames'][i], dbDict['dbAnswers'], i)

    for i in range(Count(cursor)):
        UpdateAnswers(dbDict['dbIds'][i], dbDict['dbAnswers'][i], cursor)

