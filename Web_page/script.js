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

function Submit() {
    var Email = document.getElementById('Email');
    var Name = document.getElementById('FullName');
    var Lang = document.getElementsByClassName('Lang');

    Email = Email.value;
    Name = Name.value;
    for(var i = 0; i < Lang.length; i++) {
        if(Lang[i].checked) {
            Lang = Lang[i].value;
            break;
        }
    }

    console.log(Email);
    console.log(Name);
    console.log(Lang);
}