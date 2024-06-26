let Lang = ""

function En() {
    console.log("Translating")
    Lang = "English"
    document.querySelector('.question').innerHTML = "How Was Your Day ?"
}
function Fr() {
    console.log("Translating")
    Lang = "French"
    document.querySelector('.question').innerHTML = "Comment s'est passée ta journée ?"
}
function Jp() {
    console.log("Translating")
    Lang = "Japanese"
    document.querySelector('.question').innerHTML = "あなたの一日はどうでした ?"
}
function Ar() {
    console.log("Translating")
    Lang = "Arabic"
    document.querySelector('.question').innerHTML = "كيف كان يومك ؟"
}
function Playsounds() {
    if(Lang == "English") {
        document.getElementById('play-sound').addEventListener('click', function() {
            var sound = document.getElementById('soundEn');
            sound.play();
        });
    }
    if(Lang == "French") {
        document.getElementById('play-sound').addEventListener('click', function() {
            var sound = document.getElementById('soundFr');
            sound.play();
        });
    }
    if(Lang == "Japanese") {
        document.getElementById('play-sound').addEventListener('click', function() {
            var sound = document.getElementById('soundJp');
            sound.play();
        });
    }
    if(Lang == "Arabic") {
        document.getElementById('play-sound').addEventListener('click', function() {
            var sound = document.getElementById('soundAr');
            sound.play();
        });
    }
    else {
        document.querySelector('.question').innerHTML = "404"
    }
}