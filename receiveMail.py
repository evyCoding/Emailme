import imaplib
import email
from email.header import decode_header

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


def get_decoded_header(header_value):
    """Decode email header to a human-readable format."""
    decoded_header = decode_header(header_value)[0][0]
    if isinstance(decoded_header, bytes):
        decoded_header = decoded_header.decode()
    return decoded_header


def get_emails(users, user):
    """Fetch emails from the inbox and filter by user in subject."""
    for email_id in email_ids:
        status, msg_data = imap.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = get_decoded_header(msg["subject"])
                if (user + " Daily email").upper() in subject.upper():
                    # Conditions related to printing the body of the mail.
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                users[user] = body
                    else:
                        if msg.get_content_type() == "text/plain":
                            body = msg.get_payload(decode=True).decode()
                            users[user] = body

users = {
    'yahya chami': '',
    'fatima elmounjali': '',
    'khadija sammoudi': ''
}
for user in users:
    get_emails(users, user)
    print(users[user])

imap.logout()
