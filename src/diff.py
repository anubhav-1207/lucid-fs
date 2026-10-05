import difflib
from .storage import read_object
from .history import file_history

def diff(filename):
    """
    This function takes two strings as input and returns a list of differences between them.
    It uses the difflib library to generate a unified diff format.
    
    :param filename: The name of the file for which to generate differences
    :return: A string of the diff
    """
    versions = file_history(filename)
    current_version = versions[-1]
    current_version = read_object(current_version[1]).decode('utf-8').splitlines(keepends=True)  # Read the current version of the file
    previous_version = versions[-2] if len(versions) > 1 else None
    if previous_version:
        previous_version = read_object(previous_version[1]).decode('utf-8').splitlines(keepends=True)  # Read the previous version of the file

    print(previous_version)
    print(current_version)

    diff = difflib.unified_diff(previous_version, current_version)
    return "".join(diff)
