import os
import pytest
import importlib
import io
import sys

# Specify the path to the provided filename - hardcode for dev only
# file_name = '002.py'

# Specify test cases
@pytest.mark.parametrize("input_value, expected_output", [
    ('hello', ''),
    ('minion', ''),
    ('test string', ''),
])

def test_submit_code(input_value, expected_output, request, monkeypatch):
    file_name = request.config.getoption("--input-filename")

    # Specify the path
    ref_path = './ref.py'
    # submit_path = os.path.join('Correct', file_name)
    submit_path = file_name

    # Call the minion_game function from the ref
    ref_module = importlib.import_module(ref_path)

    # Redirect stdout to capture printed output
    captured_output_ref = io.StringIO()
    sys.stdout = captured_output_ref

    # Call the minion_game function from the ref
    ref_module.minion_game(input_value)

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Get the captured output
    ref_output = captured_output_ref.getvalue().strip()


    try:
        # Import the module dynamically
        module = importlib.import_module(f'Submit_Code.{file_name[:-3]}')  # Assuming file_name ends with '.py'

        # if (hasattr(module, "minion_game")):
        # Redirect stdout to capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the minion_game function from the script
        module.minion_game(input_value)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        my_output = captured_output.getvalue().strip()

        # Compare the submit outputs
        assert my_output == ref_output

        # else:
        #     # Run the provided filename and capture its output
        #     my_output = subprocess.check_output(['python', submit_path], input=f"{input_value}\n", text=True).strip()
        #
        #     # Compare the submit outputs with expected_output or ref_ouput or using both
        #     # assert my_output == expected_output
        #     assert my_output == ref_output


    except AssertionError:
        # Print a more informative error message
        # print(f"Output mismatch!\nInput: {input_value}\nReference output: {ref_output}\nYour output: {my_output}")
        # print(f"Output mismatch!\nInput: {input_value}\nExpected output: {expected_output}\nYour output: {my_output}")
        raise  # Re-raise the AssertionError to mark the test as failed




