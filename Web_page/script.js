function En() {
    console.log("Translating")
    document.querySelector('.question').innerHTML = "How Was Your Day ?"
    document.getElementById('buttonen').addEventListener('click', function () {
        var sound = document.getElementById('soundEn');
        sound.play();
    });
}
function Fr() {
    console.log("Translating")
    document.querySelector('.question').innerHTML = "Comment s'est passée ta journée ?"
    document.getElementById('buttonfr').addEventListener('click', function () {
        var sound = document.getElementById('soundFr');
        sound.play();
    });
}
function Jp() {
    console.log("Translating")
    document.querySelector('.question').innerHTML = "あなたの一日はどうでした ?"
    document.getElementById('buttonjp').addEventListener('click', function () {
        var sound = document.getElementById('soundJp');
        sound.play();
    });
}
function Ar() {
    console.log("Translating")
    document.querySelector('.question').innerHTML = "كيف كان يومك ؟"
    document.getElementById('buttonar').addEventListener('click', function () {
        var sound = document.getElementById('soundAr');
        sound.play();
    });
}

// Functions to add Documents to the DataBase

async function documentExists(collection, query) {
    try {
        const document = await collection.findOne(query);
        return document !== null;
    } catch (err) {
        console.error('Error occurred while checking for document existence:', err);
        return false;
    }
}

async function AddDocuments(collectionName, Email, Name, Lang) {
        await client.connect();
        console.log('Connected successfully to server');
        const db = client.db(dbName);
        const collection = db.collection(collectionName);
        const exists = await documentExists(collection, { email: Email, Name: Name, Language: Lang});
        if (exists) {
            console.log('Document already exists in the collection.');
        } else {
            const insertResult = await collection.insertOne({
                Name: Name,
                email: Email,
                Language: Lang,
                answer: ""
            });
            console.log('Inserted document =>', insertResult);
        }
}

function Submit() {
    var Email = document.getElementById('Email');
    var Name = document.getElementById('FullName');
    var Lang = document.getElementsByClassName('Lang');
    Email = Email.value;
    Name = Name.value;
    for (var i = 0; i < Lang.length; i++) {
        if (Lang[i].checked) {
            Lang = Lang[i].value;
            break;
        }
    }
    const { MongoClient } = require('mongodb');
    const url = 'mongodb://127.0.0.1:27017/mongo?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6';
    const client = new MongoClient(url);
    const dbName = 'Emailme';
    AddDocuments("infos", Email, Name, Lang);
}
