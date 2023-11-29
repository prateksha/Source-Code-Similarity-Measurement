import importlib
import pytest

# Specify test cases
@pytest.mark.parametrize("input_value, expected_output", [
    ('hello', ''),
    ('minion', ''),
    ('test string', ''),
])
def test_submit_code(input_value, expected_output, request):
    file_name = request.config.getoption("--input-filename")

    # Call the score_words function from the reference implementation
    # Specify the path
    ref_path = './ref.py'
    # submit_path = os.path.join('Correct', file_name)
    submit_path = file_name

    try:
        # Import the module dynamically
        module = importlib.import_module(f'Submit_Code.{file_name[:-3]}')  # Assuming file_name ends with '.py'

        # Call the score_words function from the submitted code
        my_output = module.score_words(input_value)

        print("check my: ", my_output, "check ref: ", ref_output)

        # Compare the submit outputs
        assert my_output == ref_output

    except AssertionError:
        # Print a more informative error message
        # print(f"Output mismatch!\nInput: {input_value}\nReference output: {ref_output}\nYour output: {my_output}")
        # print(f"Output mismatch!\nInput: {input_value}\nExpected output: {expected_output}\nYour output: {my_output}")
        raise  # Re-raise the AssertionError to mark the test as failed
