import os
import subprocess
import csv
from Test_program import winnowing
from io import StringIO
import pandas as pd

program1 = 'program1'
program2 = 'program2'

# import json
# from ast import parse  
# from ast2json import ast2json
# def test_ast2json():
#     ast = ast2json(parse(open('test_ast.py').read()))
#     with open('data.json', 'w') as f:
#         json.dump(ast, f, indent = "\t")

# def test_ast2json1():
#     ast = ast2json(parse(open('test_ast.py').read()))
#     with open('data1.json', 'w') as f:
#         json.dump(ast, f, indent = "\t")

def result(ref_file_path,file_path):
    row = winnowing.result_winnowing()
    try:
        subprocess.run(["flake8", file_path], check=True, capture_output=True)
        print(f"No linting issues found in {file_path}")
        issues = None
    except subprocess.CalledProcessError as e:
        print(f"Linting issues found in {file_path}. Return code: {e.returncode}")
        print(e.stdout.decode("utf-8"))
        issues = e.stdout.decode("utf-8")

        error_issues, warning_issues, failure_issues = categorize_flake8_issues(issues)




        score_failure = grade_flake8(len(failure_issues), 'failure')
        score_errors = grade_flake8(len(error_issues), 'error')
        score_warnings = grade_flake8(len(warning_issues), 'warning')

        row.extend([score_failure, score_errors, score_warnings])
        # row.extend(unitest(ref_file_path, file_path))

        write_csv(row)


def categorize_flake8_issues(issues):
    error_issues = []
    warning_issues = []
    failure_issues = []

    if issues:
        for line in issues.split('\n'):
            if ': E' in line:
                error_issues.append(line)
            elif ': W' in line:
                warning_issues.append(line)
            elif ': F' in line:
                failure_issues.append(line)

    return error_issues, warning_issues, failure_issues

def grade_flake8(issues, type):

    max_score = 100

    match type:
        case "failure":
            score = (max_score - (5)*issues ) if ((max_score - (5)*issues) >= 0) else 0

        case "error":
            score = (max_score - (2) * issues) if ((max_score - (2) * issues) >= 0) else 0

        case "warning":
            score = (max_score - (1) * issues) if ((max_score - (1) * issues) >= 0) else 0

        case _:
            return

    return score

def write_csv(row):
    csv_filename = "csv/Similarity_Syntax_Style_results.csv"
    with open(csv_filename, "a",newline='') as file:
        fieldnames = ['Ref Program', 'input_filename', 'Total Score Winnowing', 'Similarity Score', 'Score by num of failure', 'Score by num of error', 'Score by num of warning']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if file.tell() == 0:
            writer.writeheader()

        # writer.writerow({
        #     'input_filename': input_filename,
        #     'total_tests': total_amount,
        #     'passed_amount': passed_amount,
        #     'failed_amount': failed_amount
        # })
        csvwriter = csv.writer(file)
        csvwriter.writerow(row)
        print(f'Results written to {csv_filename}')

def generate_ast(file_name, numeric_value, file_path):
    try:
        subprocess.run(['python',file_name , numeric_value, file_path], check = True)
        print(f"Script executed successfully for file: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running the script for file: {file_path}")
        print(f"Return code: {e.returncode}")

def process_directory(ref_file_path, directory_path):
    generate_ast_file_path = 'Test_program/generate_ast.py'
    numeric_value = ['1','2']
    generate_ast(generate_ast_file_path,numeric_value[0], ref_file_path)
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(directory_path, file_name)
            print(f"Running tests for {file_path}")
            command = f"pytest --input-filename={file_name} --tb=no"
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while running tests for {file_path}: {e}")
            generate_ast(generate_ast_file_path,numeric_value[1], file_path)
            result(ref_file_path,file_path)


    data_similar = pd.read_csv('csv/Similarity_Syntax_Style_results.csv')
    data_unittest = pd.read_csv('csv/unittest_result.csv')

    data_merge = pd.merge(data_similar, data_unittest, on="input_filename", how="inner")
    data_merge.to_csv("csv/result.csv")

process_directory('ref.py','Correct')



