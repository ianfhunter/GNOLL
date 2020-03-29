#!/bin/bash

export CLASSPATH=".:external/antlr-$1-complete.jar:$CLASSPATH"

shopt -s expand_aliases


CUR_DIR="$(dirname $0)"
echo $CUR_DIR

alias antlr4='java -Xmx500M -cp "$CUR_DIR/external/antlr-$1-complete.jar:$CLASSPATH" org.antlr4.v4.Tool'

alias antlr4='java -Xmx500M -jar $CUR_DIR/external/antlr-$1-complete.jar '

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

type antlr4
echo "Please Manually add antlr alias to your .bashrc"
