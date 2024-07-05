import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.environ.get(
    'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
Client = MongoClient(MONGO_URI)
db = Client['Emailme']
cursor = db['infos']


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


def extractLang(str):
    str = str[14:]
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
    for documentLang in cur.find({}, {'_id': 0, 'Language': 1}):
        dbDict['dbLang'].append(extractLang(str(documentLang)))
    return dbDict


def getQuestion(Lang):
    if Lang == "English":
        f = open("Questions/AngQuestions.txt", 'r', encoding='utf-8')
        AllLines = f.readlines()
        return AllLines[95]
    elif Lang == "Arabic":
        f = open("Questions/ArbQuestions.txt", 'r', encoding='utf-8')
        AllLines = f.readlines()
        return AllLines[95]
    elif Lang == "French":
        f = open("Questions/FrQuestions.txt", 'r', encoding='utf-8')
        AllLines = f.readlines()
        return AllLines[95]
    elif Lang == "Japanese":
        f = open("Questions/JapQuestions.txt", 'r', encoding='utf-8')
        AllLines = f.readlines()
        return AllLines[95]


def Count(cur):
    return cur.count_documents({})


def UpdateAnswers(Id, replacementStr, cur):
    cur.update_one({'_id': ObjectId(Id)}, {'$set': {'answers': replacementStr}})


if __name__ == "__main__":
    dbDict = {
        'dbIds': [],
        'dbNames': [],
        'dbEmails': [],
        'dbAnswers': [],
        'dbLang': []
    }

    Main(dbDict, cursor)
    print(dbDict['dbLang'])
