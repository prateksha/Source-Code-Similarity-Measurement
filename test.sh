#!/bin/sh
CWS=$(pwd)
export PATH=$PATH:$(pwd)
TEST_PROGRAM=$1
REF_SOL=Datasets/$TEST_PROGRAM/ref.py
SUBMISSIONS=Datasets/$TEST_PROGRAM/Correct
python3 generate_ast.py 1 $REF_SOL
for f in $SUBMISSIONS/*
do
    echo "Testing $f "
    python3 generate_ast.py 2 $f
    python3 winnowing.py program1 program2
done
