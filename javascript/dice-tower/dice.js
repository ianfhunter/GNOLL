// node.js exports

const isBrowser = this.window === this;

if(isBrowser){
    function dice(param){
        return roll(param);
    }
}else{
    module.exports = {
        roll: function(param){
            return roll(param)
        }
    }
}

function getRandInt(min, max){
    max = max + 1
    return Math.floor(Math.random() * (max - min)) + min;
}

if(isBrowser){
    var antlr4 = Tarp.require({main: "../node_modules/antlr4/index"});
    // var antlr4 = require('../node_modules/antlr4/index');
    // require(['antlr4'], function (foo) {
    //     var antlr4 = foo;
    // });

    // require(['grammar/diceLexer.js'], function (foo) {
    //     var DiceLexer = foo;
    // });
    // require(['grammar/diceParser.js'], function (foo) {
    //     var DiceParser = foo;
    // });
    // require(['grammar/diceListener.js'], function (foo) {
    //     var diceListener = foo;
    // });
}else{
    var antlr4 = require('antlr4');
    var DiceLexer = require('./grammar/diceLexer.js').diceLexer;
    var DiceParser = require('./grammar/diceParser.js').diceParser;
    var diceListener = require('./grammar/diceListener.js').diceListener;
}

var dicePrinter = function() {
    diceListener.call(this);
    this.result = 2
    return this;
}

var setupPrinter = function(){

    dicePrinter.prototype = Object.create(diceListener.prototype)
    dicePrinter.prototype.constructor = dicePrinter;

    dicePrinter.prototype.exitDie_roll = function(ctx){
        ctx.children.forEach(function(c){
            try{
                face = c.face
            }catch(e){ }
            try{
                amount = c.amount
            }catch(e){ }
        })
        if (amount == undefined){
            amount = 1
        }
        result = 0
        for(var a = 0; a != amount; a++){
            result += getRandInt(1, face)
        }
        this.result = result

    }

    dicePrinter.prototype.exitStandardFace = function(ctx){
        ctx.face=parseInt(ctx.getText())
        this.face=parseInt(ctx.getText())
    }

    function bubbleImportantValues(ctx){
        results = []
        ctx.children.forEach(function(c){
            ctx.result = c.result
        })
    }

    dicePrinter.prototype.enterEveryRule = function(ctx){
        bubbleImportantValues(ctx)
    }
}


var setup = 0
function roll(str, fn){
    if (! setup){
        setupPrinter();
        setup = 1
    }

    var input = str;
    // var input = "d4"
    var chars = new antlr4.InputStream(input);
    var lexer = new DiceLexer(chars);
    var tokens  = new antlr4.CommonTokenStream(lexer);
    var parser = new DiceParser(tokens);
    parser.buildParseTrees = true;
    var tree = parser.schema();

    diceLogic = new dicePrinter()
    // walker = ParseTreeWalker()
    // walker.walk(printer, tree)
    antlr4.tree.ParseTreeWalker.DEFAULT.walk(diceLogic, tree)

    return diceLogic.result
}