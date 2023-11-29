import os
import subprocess
import pytest

# Specify the path to the provided filename - hardcode for dev only
# file_name = '002.py'

# Specify test cases
@pytest.mark.parametrize("input_value, expected_output", [
    ('\n', ''),
])

def test_submit_code(input_value, expected_output, request):
    file_name = request.config.getoption("--input-filename")

    # Get the current working directory
    cwd = os.getcwd()

    # Specify the path
    ref_path = './ref.py'
    # submit_path = os.path.join('Correct', file_name)
    submit_path = file_name

    # Run ref.py and capture its output
    ref_output = subprocess.check_output(['python', ref_path], input=input_value, text=True).strip()

    try:
        # Run the provided filename and capture its output
        my_output = subprocess.check_output(['python', submit_path], input=input_value, text=True).strip()

        # Compare the submit outputs with expected_output or ref_ouput or using both
        # assert my_output == expected_output
        assert my_output == ref_output

    except AssertionError:
        # Print a more informative error message
        # print(f"Output mismatch!\nInput: {input_value}\nReference output: {ref_output}\nYour output: {my_output}")
        # print(f"Output mismatch!\nInput: {input_value}\nExpected output: {expected_output}\nYour output: {my_output}")
        raise  # Re-raise the AssertionError to mark the test as failed
