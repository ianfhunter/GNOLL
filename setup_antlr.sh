#!/bin/bash

export CLASSPATH=".:external/antlr-$1-complete.jar:$CLASSPATH"

shopt -s expand_aliases

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
echo $DIR

alias antlr4='java -Xmx500M -cp "$DIR/external/antlr-$1-complete.jar:$CLASSPATH" org.antlr4.v4.Tool'

alias antlr4='java -Xmx500M -jar $DIR/external/antlr-$1-complete.jar '

alias antlr4

if [ "$2" == "Javascript" ]; then
    echo "==> Build Antlr for Javascript"
    antlr4 -Dlanguage=JavaScript dice.g4 -o javascript/grammar
elif [ "$2" == "Python3" ]; then
    echo "==> Build Antlr for Python"
    antlr4 dice.g4 -o python/grammar -Dlanguage=Python3
else
    echo "Error, Setup Incorrect Params: $1, $2"
    exit 1
fi