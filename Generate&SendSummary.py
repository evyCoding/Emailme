from openai import OpenAI
from writeAndReadMethods import *
from sendMail import *
from receiveMail import *

client = OpenAI(
    api_key="NNAD6QIHFB0QW6CD9VYQG25LL1LXXP96M9DG6LNLL9VQG1B3V1IYLLCHVE434OMP",
    base_url='https://jamsapi.hackclub.dev/openai')

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("emailme.po@gmail.com", "tzep izyb nvhi ryla")
imap.select("inbox")
status, messages = imap.search(None, "ALL")
email_ids = messages[0].split()
email_ids.reverse()

smtp_server = 'smtp.gmail.com'
smtp_port = 587
from_email = 'emailme.po@gmail.com'
password = 'tzep izyb nvhi ryla '

load_dotenv()
MONGO_URI = os.environ.get('mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
Client = MongoClient(MONGO_URI)
db = Client['Emailme']
cursor = db['infos']

if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': [],
        'dbLang': [],
    }

    Main(dbDict, cursor)
    for i in range(Count(cursor)):
        getEmails(dbDict['dbNames'][i], dbDict['dbAnswers'], i)

    for i in range(Count(cursor)):
        Username = "The usename = " + dbDict['dbNames'][i]
        Lang = "answer should be in: " + dbDict['dbLang'][i]
        Standers = "First Of all You're a Critic" \
                   "The answer should be in a form of an email" \
                   "At the begning of the email you should mention the grade out of 10 you need to Be extremely strict " \
                   "about it" \
                   "First paragraph should focus on the Idea if it's well taken on the writing, +2.5 from the total " \
                   "grade" \
                   "Second paragraph should focus on the vocabulary used and how well it fits the sentence and suggest " \
                   "better vocabulary to use, +2.5 from the total grade" \
                   "Third paragraph should focus on the grammar side if the rules are well applied and well respected " \
                   "with correction, +2.5 from the total grade" \
                   "Last paragraph should focus on giving learning suggestions based on the mistakes made and also " \
                   "based " \
                   "on the language with real links" \
                   "Be more detailed I need a long email, if you highlight a mistake show it from the text, " \
                   "add suggestion with links+ add the name as 'emailme' at the end" \
                   ". Here is the text:   "
        Content = dbDict['dbAnswers'][i]

        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": Username + Lang + Standers + Content}],
            stream=False,
        )
        EmailSent = res.choices[0].message.content
        SendMail(dbDict['dbNames'][i], dbDict['dbEmails'][i], EmailSent)

imap.logout()