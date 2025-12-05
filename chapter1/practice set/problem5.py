#Label the program written in problem 4 with comments.

import os

def print_directory_contents(path='/'):
    """
    Print the names of files and directories in the given directory path.
    If path is not provided, it defaults to the current working directory.
    """
    try:
        entries = os.listdir(path)
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    # Example usage: list current directory
    print_directory_contents()

    # Example usage: list a given directory
    # Replace '/path/to/dir' with actual path
    # print_directory_contents('/path/to/dir')
