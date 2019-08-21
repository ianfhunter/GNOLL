// Temporarily copied as a placeholder from https://jsfiddle.net/estelle/6d5Z6/

document.querySelector('input[type=button]').addEventListener('click', function(){rollTheDice();});

// require(['../javascript/dice'], function (dice) {
//     //foo is now loaded.
//     a = dice.roll("1d4")
//     console.log("Result:" + a)

// });
// define(function (require) {
//     var dice = require('../javascript/dice');
//     a = dice.roll("1d4")
//     console.log("Result:" + a)
// });

// var dice = require('dice-tower/dice');
// var dice = Tarp.require({dice: "dice-tower/dice"});
var dice = require("dice-tower/dice", false);

console.log(dice)

// a = dice.roll("1d4")
// console.log("Result:" + a)


// requirejs.config({
//     baseUrl: '.',
//     paths: {
//         dice: '../javascript',
//         node: '../node_modules'
//     }
// });


// requirejs(["dice/dice"], function(dice) {
//     //This function is called when scripts/helper/util.js is loaded.
//     //If util.js calls define(), then this function is not fired until
//     //util's dependencies have loaded, and the util argument will hold
//     //the module value for "helper/util".
//     a = dice.roll("1d4")
//     console.log("Result:" + a)
// });


var rollTheDice = function() {
    console.log(dice)
    a = dice.roll("1d4")
    console.log("Result:" + a)

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
