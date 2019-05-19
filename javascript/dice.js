// node.js exports
module.exports = {
    roll: function(param){
        roll(param)
    }
}

var antlr4 = require('antlr4');
var DiceLexer = require('./grammar/diceLexer.js').diceLexer;
var DiceParser = require('./grammar/diceParser.js').diceParser;
var diceListener = require('./grammar/diceListener.js').diceListener;


var dicePrinter = function() {
    diceListener.call(this);
    this.result = 2
    return this;
}
dicePrinter.prototype = Object.create(diceListener.prototype)
dicePrinter.prototype.constructor = dicePrinter;

dicePrinter.prototype.enterDie_roll = function(ctx){
    console.log("Begin");
    this.result = 20
    ctx.result = 30

}
dicePrinter.prototype.enterEveryRule = function(ctx){
    console.log("h")
    ctx.result = 20
    this.result=42
    dicePrinter.result = 22
}


function roll(str, fn){

    // var input = str;
    var input = "d4"
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

    console.log("Res:"+diceLogic.result)
    return diceLogic.result
}