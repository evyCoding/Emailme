import imaplib
import email
from email.header import decode_header

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("emailme.po@gmail.com", "tzep izyb nvhi ryla ")

imap.select("inbox")

status, messages = imap.search(None, "ALL")
email_ids = messages[0].split()
email_ids.reverse()


def get_decoded_header(header_value):
    decoded_header = decode_header(header_value)[0][0]
    if isinstance(decoded_header, bytes):
        decoded_header = decoded_header.decode()
    return decoded_header


def get_emails(users, user):
    for email_id in email_ids:
        status, msg_data = imap.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = get_decoded_header(msg["subject"])
                if user in subject:
                    print(f"Subject: {subject}")
                    print(f"From: {get_decoded_header(msg['from'])}")
                    print(f"To: {get_decoded_header(msg['to'])}")

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                print("Body:")
                                print(body)
                                users[user] = body
                                break
                    else:
                        if msg.get_content_type() == "text/plain":
                            body = msg.get_payload(decode=True).decode()
                            print("Body:")
                            print(body)

                    # imap.logout()
                    # exit()
