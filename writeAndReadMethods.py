import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient


def extractId(str):
    str = str[18:]
    sub_str = "')}"
    return str.replace(sub_str, "")


def extractEmail(str):
    str = str[11:]
    sub_str = "'}"
    return str.replace(sub_str, "")


def extractName(str):
    str = str[10:]
    sub_str = "'}"
    return str.replace(sub_str, "")


def extractAnswers(str):
    str = str[13:]
    sub_str = "'}"
    return str.replace(sub_str, "")


def Main(dbDict, cur):
    for documentID in cur.find({}, {'_id': 1}):
        dbDict['dbIds'].append(extractId(str(documentID)))
    for documentName in cur.find({}, {'_id': 0, 'Name': 1}):
        dbDict['dbNames'].append(extractName(str(documentName)))
    for documentEmails in cur.find({}, {'_id': 0, 'email': 1}):
        dbDict['dbEmails'].append(extractEmail(str(documentEmails)))
    for documentAnswers in cur.find({}, {'_id': 0, 'answers': 1}):
        dbDict['dbAnswers'].append(extractAnswers(str(documentAnswers)))
    return dbDict


def Count(cur):
    return cur.count_documents({})


def UpdateAnswers(Id, replacementStr, cur):
    cur.update_one({'_id': ObjectId(Id)}, {'$set': {'answers': replacementStr}})


if __name__ == '__main__':
    """ Data base connection """

    load_dotenv()

    MONGO_URI = os.environ.get(
        'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')

    Client = MongoClient(MONGO_URI)

    db = Client['Emailme']

    cursor = db['infos']

    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': []
    }

    Main(dbDict, cursor)

    for i in range(Count(cursor)):
        UpdateAnswers(dbDict['dbIds'][i], "", cursor)
