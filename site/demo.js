// Temporarily copied as a placeholder from https://jsfiddle.net/estelle/6d5Z6/

document.querySelector('input[type=button]').addEventListener('click', function(){rollTheDice();});

var rollTheDice = function() {
    var i,
        faceValue,
        output = '',
        diceCount = document.querySelector('input[type=text]').value || 1;
    for (i = 0; i < diceCount; i++) {
        faceValue = Math.floor(Math.random() * 6);
        output += "&#x268" + faceValue + "; ";
    }
    document.getElementById('dice').innerHTML = output;
}
