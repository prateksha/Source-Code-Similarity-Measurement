# Source-Code-Similarity-Measurement

I. Follow these steps to run our proposed implementation :

Dependencies required :
- ast api
- astor
- nltk

Go to the directory Proposed_Work and :

1) run the command : python generate_ast.py <index_number> /path/to/program1
2) run the command : python generate_ast.py <index_number> /path/to/program2

Here, <index_number> refers to an integer value associated with a file. For simplicity choose 1 and 2 as your <index_numbers> for program 1 and program 2 respectively.

The test codes in the 'Test_Codes' folder can be used.

For eg.

- python3 generate_ast.py 1 Test_Codes/test1a.py
- python3 generate_ast.py 2 Test_Codes/test1b.py

3) run the command : python3 winnowing.py program<index_number> program<index_number>

Continued eg.

- python3 winnowing.py program1 program2

4) The output would display the final Similarity Score.

