"""
Tests Repository setup with mock function.
Goal is to see how linting and testing goes.
"""
def mock_function(message = 'message'):
    """
    Prints whatever message you put in the function.
    This is just a placeholder to test the setup.
    Parameters:
    - Message (str): Input message to print.
    Returns:
    - Prints message as output.
    """
    if message is not str:
        raise TypeError("Input not string.")
    return print(message)
